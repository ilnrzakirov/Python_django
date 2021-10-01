from django.shortcuts import render, redirect
from .models import News, NewsComment, User
from django.views.generic import TemplateView, ListView, DetailView, View, CreateView, UpdateView
from .forms import *
from django.contrib.auth.views import LoginView, LogoutView


class NewsListView(ListView):
    model = News
    template_name = 'news/news.html'
    context_object_name = 'news'
    queryset = News.objects.all()


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

class NewsCreate(CreateView):
    form_class = NewsForm
    template_name = 'news/news_create.html'


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