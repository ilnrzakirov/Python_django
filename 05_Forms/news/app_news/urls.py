from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.NewsListView.as_view(), name='news'),
    path('news/<int:pk>', views.NewsDetailFormView.as_view(), name='news-detail'),
    path('news/create/', views.NewsCreate.as_view(), name='news-create'),
]
