from django.db import models
from shop.models import Product
from django.utils import timezone

class Order(models.Model):

	CITY_CHOICES=(
		('kathmandu','Kathmandu'),
		('lalitpur','Lalitpur'),
		('bhaktapur','Bhaktapur'),)

	full_name=models.CharField(max_length=30)
	city=models.CharField(max_length=20,choices=CITY_CHOICES,default='kathmandu')
	address=models.CharField(max_length=100)
	nearest_place=models.CharField(max_length=30,blank=True)
	phone_number=models.CharField(max_length=10)
	delivered=models.BooleanField(default=False)
	phone_verified=models.BooleanField(default=False)
	ordered_date=models.DateTimeField(default=timezone.now)
	updated_date=models.DateTimeField(auto_now=True)

	def __str__(self):
		return 'Order {}'.format(self.id)

	def get_total_cost(self):
		if sum(item.get_cost() for item in self.ordered_items.all()) <= 5000:
			return sum(item.get_cost() for item in self.ordered_items.all()) + 50
		else:
			return sum(item.get_cost() for item in self.ordered_items.all())

class OrderedItem(models.Model):
	order=models.ForeignKey(Order,related_name='ordered_items',on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	price=models.DecimalField(max_digits=10,decimal_places=2)
	quantity=models.PositiveIntegerField()
	color=models.CharField(max_length=10,null=True)
	size=models.CharField(max_length=5,null=True)
	def __str__(self):
		return '{}'.format(self.id)

	def get_cost(self):
		return self.quantity * self.price

class Customer(models.Model):
	full_name=models.CharField(max_length=30,default="Not available")
	phone_number=models.CharField(max_length=10)
	frequency=models.PositiveIntegerField(default=0)
	points=models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.phone_number

	class Meta:
		ordering=['-frequency']
		verbose_name='Customer phonenumber'
		verbose_name_plural='Customer phonenumbers'