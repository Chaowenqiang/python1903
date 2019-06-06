from django.contrib import admin
from .models import BookInfo,HeroInfo

# Register your models here.

# 关联类
class HeroInfoInlines(admin.StackedInline):
    # 关联的模型
    model = HeroInfo
    # 一次最多添加的关联表
    extra = 1


class BookInfoAdmin(admin.ModelAdmin):
    # 重写方法，显示字段
    list_display = ('title', 'pub_date')
    # filter 过滤器， 根据所填字段过滤
    list_filter = ('title',)
    # 每页显示几个信息
    list_per_page = 1
    # 关联表，添加此类时同时添加关联类的信息
    inlines = [HeroInfoInlines]


class HeroInfoAdmin(admin.ModelAdmin):
    # 重写方法，显示字段
    list_display = ('name', 'content')
    # 根据字段搜索
    search_fields = ('name',)


admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)
