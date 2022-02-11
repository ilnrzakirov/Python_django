from _csv import reader

from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
import requests
from django.template.defaultfilters import truncatechars
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Blog, Profile, File
from .forms import RegisterForm, BlogForm, ProfileForm, UploadArticForm


class BlogListView(ListView):
    template_name = 'blog/blog.html'
    context_object_name = 'blog'
    queryset = Blog.objects.order_by('created_at')


class Create(UserPassesTestMixin, CreateView):
    form_class = BlogForm
    model = Blog
    template_name = 'blog/blog_form.html'
    widgets = {
        'description': forms.Textarea(attrs={'cols': 70, 'rows': 10})
    }
    success_url = '/blog/'

    def test_func(self):
        return self.request.user.profile.verification == True

    def form_valid(self, form):
        files = self.request.FILES.getlist('file')
        name = form.cleaned_data['name']
        form.save()
        id = form.instance
        for item in files:
            instance = File(blog=id, file=item)
            instance.save()
        return super().form_valid(form)

class LoginView(LoginView):
    template_name = 'blog/login.html'
    next_page = '/blog/'

class LogoutView(LogoutView):
    next_page = '/blog/'

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            avatar = form.cleaned_data['avatar']
            raw_password = form.cleaned_data.get('password1')
            phone = form.cleaned_data.get('phone')
            city = form.cleaned_data.get('city')
            Profile.objects.create(
                user=user,
                city=city,
                phone=phone,
                avatar=avatar
            )
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/blog/')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', context={'form': form})

def profile_view(request):
    form = Profile.objects.filter(user=request.user)
    return render(request, 'blog/profile.html', context={'form': form})

class BlogDetailFormView(View):
    def get(self, request, pk):
        blog = Blog.objects.get(id=pk)
        image = File.objects.filter(blog=blog)
        return render(request, 'blog/blog_detail.html', context={'blog' : blog, 'pk' : pk, 'image': image})

class BlogEdit(UserPassesTestMixin, UpdateView):
    form_class = BlogForm
    model = Blog
    template_name = 'blog/blog_update_form.html'
    success_url = '/blog/'

    def test_func(self):
        return self.request.user.profile.verification == True

def ProfileEdit(request, pk):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user.username)
            profile = Profile.objects.get(user=user)
            raw_password = form.cleaned_data.get('password1')
            phone = form.cleaned_data.get('phone')
            city = form.cleaned_data.get('city')
            profile.phone = phone
            profile.city = city
            user.set_password(raw_password)
            user.save()
            profile.save()
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/blog/')
    else:
        form = ProfileForm()
    return render(request, 'blog/prfile_update_form.html', context={'form': form})


def upload_artic(request):
    if request.method == 'POST':
        upload_file = UploadArticForm(request.POST, request.FILES)
        if upload_file.is_valid():
            file = upload_file.cleaned_data['file'].read()
            artic = file.decode('utf-8').split('\n')
            csv_f = reader(artic, delimiter=",", quotechar='"')
            for row in csv_f:
                Blog.objects.create(name=row[0], description=row[1])
            return redirect('/blog/')
    else:
        upload_file = UploadArticForm()
    contex = {'form': UploadArticForm}
    return render(request, 'blog/upload_artic_csv.html', context=contex)
