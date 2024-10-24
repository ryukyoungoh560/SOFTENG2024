from django.shortcuts import render

# Create your views here.

def landing_page(request):
    return render(request, 'single_pages/landing.html', {'title':'home'})

def about_page(request):
    return render(request, 'single_pages/about_me.html', {'title':'About me'})

def blog_list(request):
    post_list=[
        {
            'title': 'first',
            'content': 'test'
        },
    ]
    return render(request, 'single_pages/blog.html', {'title':'Blog list', 'posts': post_list})
