from django import template
from ..models import Product

register=template.Library()

@register.inclusion_tag('shop/products/featured_products.html')
def retrieve_featured_products(x,y):
	featured_products=Product.objects.filter(add_to_featured_products=True)[x:y]
	return {'featured_products':featured_products}

@register.inclusion_tag('shop/products/latest_products.html')
def retrieve_latest_products(x,y):
	latest_products=Product.objects.order_by('-updated')[x:y]
	return {'latest_products':latest_products}

@register.inclusion_tag('shop/products/best_selling_products.html')
def retrieve_best_selling_products(x,y):
	best_selling_products=Product.objects.order_by('-total_sells')[x:y]
	return {'best_selling_products':best_selling_products}