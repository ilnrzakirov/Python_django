from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
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
    path('blog/profile_edit/<int:pk>', views.ProfileNewEdit.as_view(), name='profile-edit'),
    path('blog/upload/', views.UploadArtic.as_view(), name='upload-file'),
    path('i18n', include('django.conf.urls.i18n')),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)