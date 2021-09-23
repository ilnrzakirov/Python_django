from django.shortcuts import render, redirect
from .models import News, NewsComment
from django.views.generic import TemplateView, ListView, DetailView, View
from .forms import *


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
        return render(request, 'news/news_detail.html', context={'news': news, 'comment': history,
                                                                 'add_comment': comment, 'pk': pk})

    def post(self, request, pk):
        news = News.objects.get(id=pk)
        history = NewsComment.objects.filter(news=news)
        comment = NewsCommentForm(request.POST)
        if comment.is_valid():
            comment.save()
            return redirect('news')
        return render(request, 'news/news_detail.html', context={'news': news, 'comment': history,
                                                                 'add_comment': comment, 'pk': pk})

class NewsCreate(View):

    def get(self, request):
        form = NewsForm()
        return render(request, 'news/news_create.html', context={'form': form})