from django.db import models

# Create your models here.


class Book_info(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField()

class Hero_info(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=True)
    content = models.CharField(max_length=100)
    book_id = models.ForeignKey(Book_info, on_delete=models.CASCADE)