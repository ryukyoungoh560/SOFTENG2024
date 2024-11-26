from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)    #제목 -캐릭터필드 최대 100글자
    content = models.TextField()                #제한없이 길게 쓸 수 있음

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d', blank= True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d', blank= True)

    created_at = models.DateTimeField(auto_now_add=True)    #저장 , auto~ -> 시간 자동완성?
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):            #제목이름으로 post가 보이게
        return f"[{self.pk}] {self.title}"

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'