from django.db import models

# Create your models here.

# 对Manager重写方法
# class Manager(models.Manager):
#
#     def title(self):
#         return self.first()



class BookInfo(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField()

    # 创建对象
    # object = Manager()


    # def __str__(self):
    #     return self.title


class HeroInfo(models.Model):
    name = models.CharField(max_length=20)
    content = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

