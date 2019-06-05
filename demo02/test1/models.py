from django.db import models

# Create your models here.


class BookInfo(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField()

    # def __str__(self):
    #     return self.title


class HeroInfo(models.Model):
    name = models.CharField(max_length=20)
    content = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)