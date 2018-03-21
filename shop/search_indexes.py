from .models import Product
from haystack import indexes

class ProductIndex(indexes.SearchIndex, indexes.Indexable):
	text=indexes.CharField(document=True, use_template=True)
	updated_date=indexes.DateTimeField(model_attr='updated')

	def get_model(self):
		return Product

	def index_queryset(self,using=None):
		return self.get_model().objects.filter(available=True)