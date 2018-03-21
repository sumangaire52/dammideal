from django.shortcuts import render,get_object_or_404
from .models import Category, Subcategory, Manufacturer,Offer, Product, Carousal, Application
from django.db.models import Count
from .forms import ApplyToSellForm, AddProductForm
from cart.forms import AddProductToCartForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from haystack.query import SearchQuerySet
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
	carousal_products=Carousal.objects.all()
	return render(request,'shop/products/index.html',{'carousal_products':carousal_products})


def product_detail(request,product_id,product_slug):
	product=get_object_or_404(Product,id=product_id,slug=product_slug)

	#Retrieving similar products using number of tags they share with the product
	product_tags_ids=product.tags.values_list('id',flat=True)
	similar_products=Product.objects.filter(available=True,tags__in=product_tags_ids).exclude(id=product.id)
	similar_products=similar_products.annotate(same_tags=Count('tags')).order_by('-same_tags','-updated')[:6]
	form=AddProductToCartForm()
	context={
		'product':product,
		'similar_products':similar_products,
		'form':form,
	}

	return render(request,'shop/products/product_detail.html',context)



def products(request,category_slug=None,subcategory_slug=None):
	subcategory=None

	sorting=request.GET.get('sorting')
	popularity_sorting=request.GET.get('popularity-sorting')

	# Sorting products according to the price 
	if sorting == 'lowest-first':
		object_list=Product.objects.filter(available=True).order_by('price')
	elif sorting == 'highest-first':
		object_list = Product.objects.filter(available=True).order_by('-price')
	else:
		object_list = Product.objects.filter(available=True)

	# Sorting products according to the popularity
	if popularity_sorting == 'best-selling-first':
		object_list=object_list.order_by('-total_sells')
	elif popularity_sorting == 'most-liked-first':
		object_list=object_list.order_by('-likes')
	else:
		object_list=object_list

	if subcategory_slug:
		subcategory= get_object_or_404(Subcategory,slug=subcategory_slug)
		object_list=object_list.filter(sub_category=subcategory)

	paginator=Paginator(object_list,9)
	page=request.GET.get('page')
	try:
		products=paginator.page(page)
	except PageNotAnInteger:
		products=paginator.page(1)
	except EmptyPage:
		products=paginator.page(paginator.num_pages)

	context={
		'products':products,
		'subcategory':subcategory,
		'object_list':object_list,
		'page':page,
		'sorting':sorting,
		'popularity_sorting':popularity_sorting,
	}
	return render(request,'shop/products/all_products.html',context)



def search(request):
		search_query=request.GET['query']
		object_list=SearchQuerySet().models(Product).filter(content=search_query).load_all()
		total_results=object_list.count()
		paginator=Paginator(object_list,6)
		page=request.GET.get('page')
		try:
			results=paginator.page(page)
		except PageNotAnInteger:
			results=paginator.page(1)
		except EmptyPage:
			results=paginator.page(paginator.num_pages)
		context={'results':results,'search_query':search_query,'page':page,'total_results':total_results}
		return render(request,'shop/products/search_result.html',context)


def like(request,product_id,product_slug):
	product=get_object_or_404(Product,id=product_id,slug=product_slug)
	product.likes+=1
	product.save()
	return HttpResponseRedirect(reverse('shop:product_detail',args=[product.id,product.slug]))

def dislike(request,product_id,product_slug):
	product=get_object_or_404(Product,id=product_id,slug=product_slug)
	product.dislikes+=1
	product.save()
	return HttpResponseRedirect(reverse('shop:product_detail',args=[product.id,product.slug]))

def faq(request):
	return render(request,'shop/products/faq.html')

def apply_to_sell(request):
	if request.method=='POST':
		form=ApplyToSellForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request,'shop/products/application_received.html')
	else:
		form=ApplyToSellForm()
		return render(request,'shop/products/apply_to_sell.html',{'form':form})

def tac(request):
	return render(request,'shop/products/tac.html')

def return_policy(request):
	return render(request,'shop/products/return.html')

def contact(request):
	return render(request,'shop/products/contact.html')


@login_required
def vendor_dashboard(request):
	return render(request,'account/vendor_dashboard.html',{})

@login_required
def add_product(request):
	form=AddProductForm()
	user=request.user.username
	vendor=get_object_or_404(User,username=user)
	if request.method=='POST':
		form=AddProductForm(request.POST)
		if form.is_valid():
			new_product=form.save(commit=False)
			new_product.vendor=vendor
			new_product.save()
			return render(request,'account/new_product_added.html',{})
	return render(request,'account/add_new_product.html',{'form':form})