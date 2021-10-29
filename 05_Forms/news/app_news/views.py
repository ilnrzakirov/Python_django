import requests
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, redirect
from .models import News, NewsComment, User, Profile
from django.views.generic import TemplateView, ListView, DetailView, View, CreateView, UpdateView
from .forms import *
from django.contrib.auth.views import LoginView, LogoutView


class NewsListView(ListView):
    # model = News.objects.filter(categories=)
    template_name = 'news/news.html'
    context_object_name = 'news'
    queryset = News.objects.filter(status= 'a')

    def get_queryset(self):
        queryset = self.request.GET['category']
        return News.objects.filter(categories=queryset)


class NewsDetailFormView(View):


    def get(self, request, pk):
        news = News.objects.get(id=pk)
        history = NewsComment.objects.filter(news=news)
        comment = NewsCommentForm(instance=news)
        if request.user.is_authenticated:
            comment.fields['username'].initial = request.user.username
            comment.fields['username'].widget = forms.HiddenInput()
        return render(request, 'news/news_detail.html', context={'news': news, 'comment': history,
                                                                 'add_comment': comment, 'pk': pk})

    def post(self, request, pk):
        news = News.objects.get(id=pk)
        history = NewsComment.objects.filter(news=news)
        comment = NewsCommentForm(request.POST)
        comment.instance.news = news
        if comment.is_valid():
            comment.save()
            return redirect('news')
        return render(request, 'news/news_detail.html', context={'news': news, 'comment': history,
                                                                 'add_comment': comment, 'pk': pk})

class NewsCreate(UserPassesTestMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/news_create.html'
    success_url = '/news/'

    def test_func(self):
        return self.request.user.profile.verification == True


class NewsEdit(UpdateView):
    form_class = NewsForm
    model = News
    template_name = 'news/news_update_form.html'
    success_url = '/news/'



class LoginView(LoginView):
    template_name = 'news/login.html'


class LogoutView(LogoutView):
    #template_name = "news/logout.html"
    next_page ='/news/'


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            phone = form.cleaned_data.get('phone')
            city = form.cleaned_data.get('city')
            Profile.objects.create(
                user=user,
                city=city,
                phone=phone
            )
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/news/')
    else:
        form = RegisterForm()
    return render(request, 'news/register.html', context={'form': form})

def profile_view(request):
    form = Profile.objects.filter(user=request.user)
    return render(request, 'news/profile.html', context={'form': form})