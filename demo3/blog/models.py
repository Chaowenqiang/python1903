from django.db import models
# 引入富文本格式
from tinymce.models import HTMLField

# Create your models here.

# 标签表
class Tag(models.Model):
    '''
    多对多
    '''
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

# 分类表
class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

# 文章表
class Article(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    create_time = models.DateTimeField(auto_now=True)
    update_time = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


# 图片数据库
class Img(models.Model):
    pic = models.ImageField(upload_to='')
    desc = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.desc


class MessageInfo(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    content = HTMLField()

    def __str__(self):
        return self.content

