from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.NewsListView.as_view(), name='news'),
    path('news/<int:pk>', views.NewsDetailFormView.as_view(), name='news-detail'),
    path('news/create/', views.NewsCreate.as_view(), name='news-create'),
    path('news/edit/<int:pk>', views.NewsEdit.as_view(), name='news-edit'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile')
]
