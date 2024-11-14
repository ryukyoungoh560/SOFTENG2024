from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view(), name= 'post_detail'),
    path('', views.PostList.as_view(), name= 'post_list'),
    path('about_me/', views.about_page, name="about_me"),
    path('landing', views.landing_page, name='landing_page'),
]