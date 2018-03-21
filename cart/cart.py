from shop.models import Product
from django.conf import settings
from decimal import Decimal 

class Cart(object):

	def __init__(self,request):

		self.session = request.session
		cart= self.session.get(settings.CART_SESSION_ID)

		#Initialize the session with empty cart if cart is none
		if not cart:
			cart=self.session[settings.CART_SESSION_ID]={}

		self.cart=cart

	#Function to add or update products in the cart
	def add(self,product,quantity=1,update_quantity=False,color=None,size=None):

		product_id=str(product.id)
		if product_id not in self.cart:
			self.cart[product_id]={
				'quantity':0,
				'price':str(product.price),
			}
		if update_quantity:
			self.cart[product_id]['quantity']=quantity
		else:
			self.cart[product_id]['quantity']+=quantity

		if color:
			self.cart[product_id]['color']=color
		if size:
			self.cart[product_id]['size']=size
		self.save()

	#Function to remove products from the cart
	def remove(self,product):

		product_id=str(product.id)
		if product_id in self.cart:
			del self.cart[product_id]
			self.save()

	def save(self):
		self.session[settings.CART_SESSION_ID]=self.cart
		self.session.modified=True

	def __iter__(self):

		product_ids=self.cart.keys()
		products=Product.objects.filter(id__in=product_ids)

		for product in products:
			self.cart[str(product.id)]['product']=product

		for item in self.cart.values():
			item['price']=Decimal(item['price'])
			item['total_price']=item['quantity']*item['price']
			yield item

	def __len__(self):
		# Counting all the items in the cart
		return sum(item['quantity'] for item in self.cart.values())

	def get_total_price(self):
		#Getting the total cost of all the products

		return Decimal(sum(item['quantity']*Decimal(item['price']) for item in self.cart.values()))

	# Function to clear the cart session when the user checkouts
	def clear(self):
		del self.session[settings.CART_SESSION_ID]
		self.session.modified=True