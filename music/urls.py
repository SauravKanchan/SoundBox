# -*- coding: utf-8 -*-
"""

@author: Saurav Kanchan

"""
from django.conf.urls import url
from .import views
app_name='music'

urlpatterns = [
    # /music/
    url(r'^$',views.index ,name='index'),

    #/music/2/
    # url(r'^(?P<album_id>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),

    url(r'^register/$',views.UserFormView.as_view(),name='register'),

    # /music/2/favourite/
    url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    url(r'^(?P<album_id>[0-9]+)/favoriteAlbum/$', views.favoriteAlbum, name='favoriteAlbum'),

    url(r'login/$', views.UserLoginView.as_view(), name='login'),
    url(r'search/$', views.search, name='search'),

    # music/album/add
    url(r'album/add/$',views.AlbumCreate.as_view(),name='album-add'),

    # music/album/2
    url(r'album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(),name='album-update'),

    # music/album/2/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

    url(r'logout/$',views.logoutUser,name='logout'),
    url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),

    # music/album/2/add-song
    url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),
    url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),

]