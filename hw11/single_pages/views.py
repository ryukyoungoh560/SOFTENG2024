from django.shortcuts import render
import os
import pandas as pd
from django.conf import settings
# Create your views here.



def landing_page(request):
    return render(request, 'single_pages/landing.html', {'title':'home'})

def about_page(request):
    return render(request, 'single_pages/about_me.html', {'title':'About me'})



