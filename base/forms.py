from dataclasses import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Image

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class CreatePost(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
