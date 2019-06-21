from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 创建品牌  如：阿迪，耐克等
class Brand(models.Model):
    brand = models.CharField(max_length=20)

    def __str__(self):
        return self.brand


# 创建款式类  如：篮球鞋，足球鞋，休闲鞋，等
class Style(models.Model):
    style = models.CharField(max_length=100)

    def __str__(self):
        return self.style



# 创建适合人群表  如：男人、女人等
class Crow(models.Model):
    crow = models.CharField(max_length=20)
    crow_style = models.ManyToManyField(Style)

    def __str__(self):
        return self.crow


# 创建商品图片类
class Pic(models.Model):
    pic1 = models.ImageField(upload_to='')
    pic2 = models.ImageField(upload_to='')
    pic3 = models.ImageField(upload_to='')
    pic4 = models.ImageField(upload_to='')
    pic5 = models.ImageField(upload_to='')
    desc = models.CharField(max_length=20)

    def __str__(self):
        return self.desc


# 创建商品详情类
class GoodsInfo(models.Model):
    goods_name = models.CharField(max_length=20)
    goods_price = models.IntegerField()
    goods_size = models.IntegerField()
    goods_info = models.TextField(max_length=300)
    goods_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    goods_crow = models.ForeignKey(Crow, on_delete=models.CASCADE)
    goods_pic = models.ForeignKey(Pic, on_delete=models.CASCADE)
    goods_style = models.ForeignKey(Style, on_delete=models.CASCADE)


    def __str__(self):
        return self.goods_name


# 联系我们类
class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    content = models.TextField(max_length=300)

    def __str__(self):
        return self.name


# 小头像
class HeadPhoto(models.Model):
    pic = models.ImageField(upload_to='')

    # def __str__(self):
    #     return self.pic

# 用户存储
class UserInfo(User):
    pass
