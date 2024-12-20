from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk'


class PostDetail(DetailView):
    model = Post

# def blog_list(request):
#     posts = Post.objects.all().order_by('-pk')

#     return render(request, 'blog/blog.html', {'title':'Blog list', 'posts': posts})

# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)

#     return render(request, 'blog/single_post_page.html', {'title':'single_post_page', 'post': post})
