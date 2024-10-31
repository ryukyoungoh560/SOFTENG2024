from django.shortcuts import render
import os
import pandas as pd
from django.conf import settings
# Create your views here.



def landing_page(request):
    return render(request, 'single_pages/landing.html', {'title':'home'})

def about_page(request):
    return render(request, 'single_pages/about_me.html', {'title':'About me'})

def blog_list(request):
    csv_path = os.path.join(settings.BASE_DIR, "single_pages", "static", "single_pages", "csv", "data.csv")

    df = pd.read_csv(csv_path)
    post_list = df.to_dict(orient="records")

    return render(request, 'single_pages/blog.html', {'title':'Blog list', 'posts': post_list})

