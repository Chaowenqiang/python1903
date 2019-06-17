from django.template import Library
from ..models import Article,Category,Tag,Img

register = Library()


@register.simple_tag
def get_latest_articles(num=3):

    return Article.objects.all().order_by('-create_time')[:num]


@register.simple_tag
def get_archives():

    return Article.objects.dates('create_time', 'month')


@register.simple_tag
def get_category():

    return Category.objects.all()


@register.simple_tag
def get_tags():

    return Tag.objects.all()


@register.simple_tag
def get_ads():

    return Img.objects.all()