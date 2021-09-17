from django.urls import path
from . import views

urlpatterns = [
    path('advertisements/', views.AdvertisementsListView.as_view(), name='advertisement'),
    path('advertisements/<int:pk>', views.AdvertisementDetailView.as_view(), name='advertisement-detail'),
]
