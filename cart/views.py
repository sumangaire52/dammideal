from django.shortcuts import render, get_object_or_404, redirect
from shop.models import Product
from .cart import Cart 
from .forms import AddProductToCartForm
from django.views.decorators.http import require_POST


@require_POST
def add_to_cart(request,product_id):
	cart=Cart(request)
	form=AddProductToCartForm(request.POST)
	product=get_object_or_404(Product,id=product_id)
	if form.is_valid():
		cd=form.cleaned_data
		if cd['quantity'] > product.stock:
			error_message='Quantity is out of stock'
			form=AddProductToCartForm()
			return render(request,'shop/products/product_detail.html',{'product':product,'error_message':error_message,'form':form})
		
		# Checking if color and size is submitted through the form.
		if 'color' and 'size' in request.POST:
			cart.add(product=product,quantity=cd['quantity'],update_quantity=cd['update'],color=request.POST['color'],size=request.POST['size'])
		elif 'size' in request.POST:
			cart.add(product=product,quantity=cd['quantity'],update_quantity=cd['update'],size=request.POST['size'])
		elif 'color' in request.POST:
			cart.add(product=product,quantity=cd['quantity'],update_quantity=cd['update'],color=request.POST['color'])
		else:
			cart.add(product=product,quantity=cd['quantity'],update_quantity=cd['update'])
	return redirect('cart:cart_detail')

def remove_from_cart(request,product_id):
	cart=Cart(request)
	product=get_object_or_404(Product,id=product_id)
	cart.remove(product)
	return redirect('cart:cart_detail')

def cart_detail(request):
	cart=Cart(request)
	for item in cart:
		item['form_to_update_quantity']=AddProductToCartForm(initial={'quantity':item['quantity'],'update':True})
	return render(request,'cart/cart_detail.html',{'cart':cart})
