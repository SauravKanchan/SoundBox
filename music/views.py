# from django.shortcuts import render,get_object_or_404
# from django.http import HttpResponse
# from .models import Album
from django.template import loader
# from django.http import Http404
# # Create your views here.
def index(request):
    all_albums=Album.objects.all().filter(Q(acces="public")|Q(acces=get_user(request).username))
    # html=''
    # for album in all_albums:
    #     url='/music/{0}/'.format(album.id)
    #     html+="<h1><a  href='{0}'>{1}</a></h1><img src='{2}'> ".format(url,album.album_title,album.album_logo)
    # return HttpResponse(html)

    #
    template = loader.get_template('music/index.html')
    context={
        'all_albums':all_albums,
    }
    # return HttpResponse(template.render(context,request))
    #

    return render(request,'music/index.html',context)
# def detail(request,album_id):
#     # return HttpResponse("<h2>Details for album Id: {0}</h2>".format(album_id))
#     # try:
#     #     album=Album.objects.get(pk=album_id)
#     # except Album.DoesNotExist:
#     #     raise Http404("Album does not exists")
#     album=get_object_or_404(Album,pk=album_id)
#     return render(request,'music/detail.html',{'album':album})
#
# def favorite(request,album_id):
#     album=get_object_or_404(Album,pk=album_id)
#     try:
#         selected_song=album.songs_set.get(pk=request.POST['song'])
#     except KeyError:
#         return render(request,'music/detail.html',{'album':album,'error_message':"You did not selected a valid song"})
#     else:#if everything is fine
#         selected_song.is_favourite=not selected_song.is_favourite
#         selected_song.save()
#     return render(request, 'music/detail.html', {'album': album})
#

from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView #Whenver we want to make a object to make a form
from django.core.urlresolvers import reverse_lazy #take us to the url after deleting
from .models import Album,Songs
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
#authenticate:- takes a username and passwords and authentictes it
#login:- gives a session id so that we dont have to login in each page
from django.views.generic import View
from .forms import UserForm,LoginForm,SongForm,AlbumForm
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth import get_user

AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']

# class IndexView(generic.ListView):
#     template_name = 'music/index.html'
#     context_object_name = 'all_albums'
#     def get_queryset(self):
#         return Album.objects.all().filter(Q(acces='public'))

class DetailView(generic.DetailView):
    model = Album #Type of object
    template_name = 'music/detail.html'

class AlbumCreate(View):
    form_class = AlbumForm
    template_name = 'music/album_form.html'

    # Display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            album = form.save(commit=False)  # we are not actually stroing in the database

            # cleaned (normalized) data
            private = form.cleaned_data['keep_this_album_as_private']
            if private:
                album.acces=get_user(request).username
            album.name=get_user(request).username
            album.save()

        return render(request, 'music/index.html', {'all_albums': Album.objects.all().filter(Q(acces="public")|Q(acces=get_user(request).username))})

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo','keep_this_album_private']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class UserFormView(View):
    form_class=UserForm
    template_name='music/registration_form.html'

    # Display blank form
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    # process form data
    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)# we are not actually stroing in the database

            #cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns user objects if credentials are correct
            user = authenticate(username=username,password=password)#checks in database

            if user is not None:

                if user.is_active:

                    login(request,user)# logged in to our website
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})

class UserLoginView(View):
    form_class = LoginForm
    template_name='music/login.html'

    # Display blank form
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    # process form data
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('music:index')
        return render(request, self.template_name, {'error':"Invalid details",'form':self.form_class(None)})

def create_song(request, album_id):
    form = SongForm(request.POST or None, request.FILES or None)
    album = get_object_or_404(Album, pk=album_id)
    if form.is_valid():
        albums_songs = album.songs_set.all()
        for s in albums_songs:
            if s.song_title == form.cleaned_data.get("song_title"):
                context = {
                    'album': album,
                    'form': form,
                    'error_message': 'You already added that song',
                }
                return render(request, 'music/create_song.html', context)
        song = form.save(commit=False)
        song.album = album
        song.audio_file = request.FILES['audio_file']
        file_type = song.audio_file.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in AUDIO_FILE_TYPES:
            context = {
                'album': album,
                'form': form,
                'error_message': 'Audio file must be WAV, MP3, or OGG',
            }
            return render(request, 'music/create_song.html', context)

        song.save()
        return render(request, 'music/detail.html', {'album': album})
    context = {
        'album': album,
        'form': form,
    }
    return render(request, 'music/create_song.html', context)

def logoutUser(request):
    if request.user.is_authenticated():
        logout(request)
        return render(request, 'music/index.html', {})
    else:
        all_albums = Album.objects.all()
        return render(request, 'music/index.html', {'all_albums':all_albums})



def favorite(request, song_id):
    song = get_object_or_404(Songs, pk=song_id)

    if '|' +get_user(request).username+'|' in song.is_favorite:
        song.is_favorite = song.is_favorite.replace('|' +get_user(request).username+'|','')
    else:
        song.is_favorite = song.is_favorite+'|' +get_user(request).username+'|'
    song.save()
    return render(request,'music/detail.html',{'album':song.album})

def favoriteAlbum(request, album_id):
    album=get_object_or_404(Album,pk=album_id)
    if '|' +get_user(request).username+'|' in album.is_favorite:
        album.is_favorite = album.is_favorite.replace('|' +get_user(request).username+'|','')
    else:
        album.is_favorite = album.is_favorite+'|' +get_user(request).username+'|'
    album.save()
    return render(request, 'music/index.html', {'all_albums':Album.objects.all().filter(Q(acces="public")|Q(acces=get_user(request).username))})




def delete_song(request, album_id, song_id):
    album = get_object_or_404(Album, pk=album_id)
    song = Songs.objects.get(pk=song_id)
    song.delete()
    return render(request, 'music/detail.html', {'album': album})

def search(request):
    query=request.GET['q']
    albums=Album.objects.all().filter(Q(acces="public")|Q(acces=get_user(request).username))
    all_albums=albums.filter((Q(album_title__contains=query)|Q(artist__contains=query))&(Q(acces="public")|Q(acces=get_user(request).username)))
    songs=[]
    for album in albums:
        for song in album.songs_set.all().filter(Q(song_title__contains=query)):
            songs.append(song)
    return render(request,'music/search.html',{'all_albums':all_albums,'songs':songs})

def songs(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        try:
            song_ids = []
            for album in Album.objects.all().filter(Q(acces="public")|Q(acces=get_user(request).username)):
                for song in album.songs_set.all():
                    song_ids.append(song.pk)
            users_songs = Songs.objects.filter(pk__in=song_ids)
            if filter_by == 'favorites':
                users_songs = users_songs.filter(is_favorite__contains="|"+get_user(request).username+"|")
        except Album.DoesNotExist:
            users_songs = []
        return render(request, 'music/songs.html', {
            'song_list': users_songs,
            'filter_by': filter_by,
        })