from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
class Choice(models.Model):
    title = models.CharField(max_length=20)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    vites = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class MyUser(User):
    telephone = models.CharField(max_length=20)