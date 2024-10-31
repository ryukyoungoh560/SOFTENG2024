from django.shortcuts import render
import os
import pandas as pd
from django.conf import settings

def blog_list(request):
    csv_path = os.path.join(settings.BASE_DIR, "blog", "static", "blog", "csv", "data.csv")

    df = pd.read_csv(csv_path)
    post_list = df.to_dict(orient="records")

    return render(request, 'blog/blog.html', {'title':'Blog list', 'posts': post_list})