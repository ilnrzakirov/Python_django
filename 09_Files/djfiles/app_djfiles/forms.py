from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import inlineformset_factory

from .models import Blog, Profile


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=20, required=False, help_text='Фамилия')
    phone = forms.IntegerField(max_value=9999999999, min_value=1111111111, help_text='Номер телефона без 8')
    city = forms.CharField(max_length=20, required=False, help_text='Город')
    avatar = forms.FileField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phone', 'city', 'password1', 'password2', 'avatar')


class BlogForm(forms.ModelForm):
    file = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Blog
        fields = ['name', 'description', 'file']


class ProfileForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=20, required=False, help_text='Фамилия')
    phone = forms.IntegerField(max_value=9999999999, min_value=1111111111, help_text='Номер телефона без 8')
    city = forms.CharField(max_length=20, required=False, help_text='Город')
    avatar = forms.ImageField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone', 'city', 'password1', 'password2', 'avatar')


class UploadArticForm(forms.Form):
    file = forms.FileField()

class ProfileNewForm(forms.ModelForm):
    phone = forms.IntegerField(max_value=9999999999, min_value=1111111111, help_text='Номер телефона без 8')
    city = forms.CharField(max_length=20, required=False, help_text='Город')
    avatar = forms.ImageField()

    class Meta:
        model = Profile
        fields = ('city', 'phone', 'avatar')

class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=20, required=False, help_text='Фамилия')
    password = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'password')