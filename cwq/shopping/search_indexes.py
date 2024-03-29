from haystack import indexes
from .models import GoodsInfo


# class GoodsIndex(indexes.SearchIndex, indexes.Indexable):
#     text = indexes.CharField(document=True, use_template=True)
#
#     def get_model(self):
#         return GoodsInfo
#
#     def index_queryset(self, using=None):
#         return self.get_model().objects.all()



class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    def get_model(self):
        return GoodsInfo
    def index_queryset(self, using=None):
        return self.get_model().objects.all()