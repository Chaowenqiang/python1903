from django.db import models

# Create your models here.


class Questions(models.Model):
    question = models.CharField(max_length=50)


class Votes(models.Model):
    name = models.CharField(max_length=20)
    votes = models.IntegerField()
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
