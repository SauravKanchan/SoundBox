# -*- coding: utf-8 -*-
"""

@author: Saurav Kanchan

"""
from django.contrib.auth.models import User #This is gonna give us base user class
from django import forms
from .models import Album, Songs


class UserForm(forms.ModelForm):#make a blueprint
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:#Information about the class
        model = User
        fields = ['username','email','password']


class LoginForm(forms.ModelForm):  # make a blueprint
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:  # Information about the class
        model = User
        fields = ['username', 'password']


class SongForm(forms.ModelForm):
    class Meta:
        model = Songs
        fields = ['song_title', 'audio_file']

class AlbumForm(forms.ModelForm):
    class Meta:
        model =Album
        fields = ['artist', 'album_title', 'genre', 'album_logo', 'keep_this_album_as_private']


