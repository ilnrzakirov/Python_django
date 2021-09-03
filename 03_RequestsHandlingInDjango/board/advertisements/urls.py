from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='advertisement_list'),
    path('advertisements/', views.Advertisement.as_view(), name='advertisements'),
    path('contacts/', views.Contacts.as_view(), name='contacts'),
    path('about/', views.About.as_view(), name='about'),
]
