from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('blog/<int:pk>/', views.PostDetail.as_view(), name= 'post_detail'),
    path('blog/', views.PostList.as_view(), name= 'post_list'),
    path('about_me/', views.about_page, name="about_me"),
    path('', views.landing_page, name='landing_page'),
    path('blog/index/', views.index_page, name="index")
]