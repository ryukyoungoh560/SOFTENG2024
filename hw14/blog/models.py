from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/' 



class Category(models.Model):
    
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'
    
    class Meta:
        verbose_name_plural = 'Categories'

class Post(models.Model):
    title = models.CharField(max_length=100)    #제목 -캐릭터필드 최대 100글자
    content = models.TextField()                #제한없이 길게 쓸 수 있음
    hook_text = models.CharField(max_length=100, blank=True, null=True)

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d', blank= True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d', blank= True)

    created_at = models.DateTimeField(auto_now_add=True)    #저장 , auto~ -> 시간 자동완성?
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)

    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):            #제목이름으로 post가 보이게
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    
