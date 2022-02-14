from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.BlogListView.as_view(), name='blog'),
    path('register/', views.register_view, name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('blog/create/', views.Create.as_view(), name='create'),
    path('blog/<int:pk>', views.BlogDetailFormView.as_view(), name='blog-detail'),
    path('blog/edit/<int:pk>', views.BlogEdit.as_view(), name='blog-edit'),
    path('blog/profile_edit/<int:pk>', views.ProfileEdit, name='profile-edit'),
    path('blog/upload', views.UploadArtic.as_view(), name='upload-file'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)