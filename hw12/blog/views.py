from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.

def landing_page(request):
    return render(request, 'blog/landing.html', {'title':'home'})

def about_page(request):
    return render(request, 'blog/about_me.html', {'title':'About me'})

class PostList(ListView):
    model = Post
    ordering = '-pk'


class PostDetail(DetailView):
    model = Post
