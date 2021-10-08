from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import News, NewsComment

class NewsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].empty_label = "Выбрать статус"

    class Meta:
        model = News
        fields = '__all__'
        widgets ={
            'description': forms.Textarea(attrs={'cols': 70, 'rows': 10})
        }

class NewsCommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].empty_label = "Автор не выбран"

    class Meta:
        model = NewsComment
        fields = ['username', 'comment_text']
        widgets = {
            'comment_text': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }

    def clean_news(self):
        data = self.cleaned_data['news']
        return data

    def clean_username(self):
        data = self.cleaned_data['username']
        return data


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=20, required=False, help_text='Фамилия')
    phone = forms.IntegerField(max_value=9999999999, min_value=1111111111, help_text='Номер телефона без 8')
    city = forms.CharField(max_length=20, required=False, help_text='Город')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phone', 'city', 'password1', 'password2')