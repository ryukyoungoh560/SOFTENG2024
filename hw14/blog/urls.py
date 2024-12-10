from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('update_post/<int:pk>/', views. PostUpdate.as_view(), name='update_post'), 
    path('create_post/', views.PostCreate.as_view(), name='post_form'),
    path('tag/<str:slug>/', views.tag_page, name='tag_page'),
    path('category/<str:slug>/', views.category_page, name='category_page'),
    path('blog/<int:pk>/', views.PostDetail.as_view(), name= 'post_detail'),
    path('blog/', views.PostList.as_view(), name= 'post_list'),
    path('about_me/', views.about_page, name="about_me"),
    path('', views.landing_page, name='landing_page'),
]