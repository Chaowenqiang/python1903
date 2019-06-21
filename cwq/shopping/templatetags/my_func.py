from ..models import Crow,GoodsInfo,Brand,Style,HeadPhoto
from django.template import Library

register = Library()


@register.simple_tag
def get_corws():

    return Crow.objects.all()

@register.simple_tag
def get_styles():

        return Style.objects.all()[:5]

@register.simple_tag
def get_brands():

    return Brand.objects.all()[:5]

@register.simple_tag
def get_head_photoes():

    return HeadPhoto.objects.all()

@register.simple_tag
def get_goodses():

    return GoodsInfo.objects.all()[:5]
