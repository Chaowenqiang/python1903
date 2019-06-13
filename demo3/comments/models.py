from django.db import models
from blog.models import Article

# Create your models here.


class Comment(models.Model):
    author = models.CharField(max_length=20, verbose_name='名字')
    pub_time = models.DateTimeField(auto_now=True)
    email = models.EmailField(blank=True, null=True, verbose_name='邮箱')
    content = models.TextField(max_length=200, verbose_name='内容')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    url = models.URLField(blank=True, null=True, verbose_name='网址')

    def __str__(self):
        return self.author