from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.

def landing_page(request):
    return render(request, 'blog/landing.html', {'title':'home'})

def about_page(request):
    return render(request, 'blog/about_me.html', {'title':'About me'})

#싱글페이지 꺼
def index_page(request):
    return render(request, 'blog/index.html', {'title':'index'})

class PostList(ListView):
    model = Post
    ordering = '-pk'


class PostDetail(DetailView):
    model = Post
