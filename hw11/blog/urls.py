from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view(), name= 'post_detail'),
    path('', views.PostList.as_view(), name= 'post_list'),
    # path('', views.blog_list, name='blog_list'),
]

