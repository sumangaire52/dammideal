import datetime
from django.db import models
from taggit.managers import TaggableManager
from django import forms
from django.urls import reverse
from django.utils import timezone
from django_resized import ResizedImageField
from django.contrib.auth.models import User

class Category(models.Model):
	name=models.CharField(max_length=20)
	slug=models.SlugField(max_length=25)

	class Meta:
		ordering=['name']
		verbose_name='category'
		verbose_name_plural='categories'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('shop:products_by_category',args=[self.slug])

class Subcategory(models.Model):
	category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='subcategories')
	name=models.CharField(max_length=20)
	slug=models.SlugField(max_length=25)

	class Meta:
		ordering=['name']
		verbose_name='subcategory'
		verbose_name_plural='subcategories'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('shop:products_by_subcategory',args=[self.category.slug,self.slug])

class Manufacturer(models.Model):
	name=models.CharField(max_length=30)
	slug=models.SlugField(max_length=35)
	brand_image=models.ImageField(blank=True,upload_to='manufacturers/')
	tags=TaggableManager()
	class Meta:
		ordering=['name']

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('shop:index_by_manufacturer',args=[self.slug])

class Offer(models.Model):
	name=models.CharField(max_length=100)
	slug=models.SlugField(max_length=110)
	duration=models.DurationField(default=datetime.timedelta(30))
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('shop:index_by_offer',args=[self.slug])

class Color(models.Model):
	name=models.CharField(max_length=10)

	def __str__(self):
		return self.name
class Size(models.Model):
	SIZE_CHOICES=(
		('xxs','XXS'),
		('xs','XS'),
		('s','S'),
		('m','M'),
		('l','L'),
		('xl','XL'),
		('xxl','XXL'),
		('xxxl','XXXL'),
		)
	size=models.CharField(max_length=5,choices=SIZE_CHOICES)

	def __str__(self):
		return self.size

class Product(models.Model):
	category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
	sub_category=models.ForeignKey(Subcategory,on_delete=models.SET_NULL,related_name='products',blank=True,null=True)
	vendor=models.ForeignKey(User,on_delete=models.CASCADE,related_name='products',blank=True,null=True)
	manufactured_by=models.ForeignKey(Manufacturer,on_delete=models.SET_NULL,related_name='products',blank=True,null=True)
	offer=models.ForeignKey(Offer,on_delete=models.SET_NULL,related_name='products',blank=True,null=True)
	name=models.CharField(max_length=300)
	slug=models.SlugField(max_length=350)
	price=models.DecimalField(max_digits=10,decimal_places=2)
	discount_price=models.DecimalField(blank=True,null=True,max_digits=10,decimal_places=2)
	available_colors=models.ManyToManyField(Color,blank=True)
	size=models.ManyToManyField(Size,blank=True)
	image1=ResizedImageField(size=[1024,720],quality=100,upload_to='products/%Y/%m/%d')
	image2=ResizedImageField(size=[1024,720],quality=100,upload_to='products/%Y/%m/%d')
	image3=ResizedImageField(size=[1024,720],quality=100,blank=True,upload_to='products/%Y/%m/%d')
	image4=ResizedImageField(size=[1024,720],quality=100,blank=True,upload_to='products/%Y/%m/%d')
	image5=ResizedImageField(size=[1024,720],quality=100,blank=True,upload_to='products/%Y/%m/%d')
	stock=models.PositiveIntegerField()
	for_sale=models.CharField(max_length=3,choices=(('yes','Yes'),('no','No')),default='no')
	add_to_featured_products=models.BooleanField(default=False)
	total_sells=models.PositiveIntegerField(default=0)
	short_description=models.CharField(max_length=350,blank=True)
	description=models.TextField()
	features=models.TextField(blank=True)
	available=models.BooleanField(default=True)
	tags=TaggableManager()
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	likes=models.PositiveIntegerField(default=0)
	dislikes=models.PositiveIntegerField(default=0)
	stars=models.PositiveIntegerField(default=0)
	def __str__(self):
		return self.name

	class Meta:
		ordering=['name']

	def is_for_sale(self):
		if self.for_sale=='yes':
			return True
		else:
			return False
	def is_new_product(self):
		if timezone.now()>self.created>(timezone.now()-datetime.timedelta(10)):
			return True
		else:
			return False

	def get_absolute_url(self):
		return reverse('shop:product_detail',args=[self.id,self.slug])

class Carousal(models.Model):
	name=models.CharField(max_length=300)
	slug=models.SlugField(max_length=350)
	image1=ResizedImageField(size=[1170,480],quality=100)
	image2=models.ImageField(blank=True)
	image3=models.ImageField(blank=True)
	image4=models.ImageField(blank=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name='Products for carousal'
		verbose_name_plural='Products for carousal'

class Application(models.Model):
	CITY_CHOICES=(
		('kathmandu','Kathmandu'),
		('bhaktapur','Bhaktapur'),
		('lalitpur','Lalitpur'),
		)
	name_of_shop=models.CharField(max_length=30)
	type_of_shop=models.CharField(max_length=30)
	location_of_shop=models.CharField(max_length=30)
	city=models.CharField(max_length=10,choices=CITY_CHOICES,default='kathmandu')
	contact_no=models.CharField(max_length=10)
	first_name_of_owner=models.CharField(max_length=30)
	last_name_of_owner=models.CharField(max_length=30)
	contact_no_of_owner=models.CharField(max_length=10)
	percent_of_share_willing_to_give=models.CharField(max_length=3)
	delivery_by_self=models.CharField(max_length=3,choices=(('yes','Yes'),('no','No')),default='no')
	can_make_brand_image_for_shop=models.CharField(max_length=3,choices=(('yes','Yes'),('no','No')),blank=True)
	question=models.TextField(blank=True)
	accepts_tac=models.BooleanField(default=True)
	applied_date=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name_of_shop

	class Meta:
		ordering=['-applied_date']

class VendorAddedProducts(models.Model):
	category=models.CharField(max_length=25)
	subcategory=models.CharField(max_length=25)
	vendor=models.ForeignKey(User,on_delete=models.CASCADE)
	name=models.CharField(max_length=300)
	manufactured_by=models.CharField(max_length=50)
	price=models.DecimalField(max_digits=10,decimal_places=2)
	available_colors=models.CharField(max_length=50)
	available_sizes=models.CharField(max_length=50)
	image1=models.ImageField(upload_to='vendor_added_products/%Y/%m/%d')
	image2=models.ImageField(blank=True,upload_to='vendor_added_products/%Y/%m/%d')
	image3=models.ImageField(blank=True,upload_to='vendor_added_products/%Y/%m/%d')
	image4=models.ImageField(blank=True,upload_to='vendor_added_products/%Y/%m/%d')
	image5=models.ImageField(blank=True,upload_to='vendor_added_products/%Y/%m/%d')
	stock=models.PositiveIntegerField()
	for_sale=models.CharField(max_length=3,choices=(('yes','Yes'),('no','No')),default='no')
	short_description=models.CharField(max_length=350,blank=True)
	description=models.TextField()
	features=models.TextField()
	created=models.DateTimeField(auto_now_add=True)
	added_to_products=models.BooleanField(default=False)
	def __str__(self):
		return self.name

	class Meta:
		ordering=['-created']