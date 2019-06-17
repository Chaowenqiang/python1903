from django.contrib import admin
from .models import Article,Category,Tag,Img,MessageInfo

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Img)
admin.site.register(MessageInfo)