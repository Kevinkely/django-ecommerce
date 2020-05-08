import datetime
from haystack import indexes
from .models import Item, Category

class ItemIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    price = indexes.FloatField(model_attr='price')
    discount_price = indexes.FloatField(model_attr='discount_price')
    category = indexes.CharField(model_attr='category')
    label = indexes.CharField(model_attr='label')
    #image = indexes.ImageField(model_attr='image')

    def get_model(self):
        return Item

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
