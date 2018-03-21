from django.contrib import admin
from .models import Order, OrderedItem, Customer
import csv
import datetime
from django.http import HttpResponse
from django.urls import reverse
from django.utils.safestring import mark_safe

#Exporting the orders as csv file
def export_to_csv(modeladmin,request,queryset):
	opts=modeladmin.model._meta
	response=HttpResponse(content_type='text/csv')
	response['Content-Disposition']='attachment;filename={}.csv'.format(datetime.datetime.now().strftime("%d/%m/%Y"))
	writer=csv.writer(response)
	fields=[field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
	#Writing the first row with header information
	writer.writerow([field.verbose_name for field in fields]+['Total cost'])
	#Writing the rows
	for obj in queryset:
		data_row=[]
		for field in fields:
			value=getattr(obj,field.name)
			if isinstance(value,datetime.datetime):
				value=value.strftime('%d/%m/%Y')
			data_row.append(value)
		writer.writerow(data_row+[obj.get_total_cost()])
	return response
export_to_csv.short_description='Export as csv'

#Customizing the default admin view
def order_detail(order):
	return mark_safe("<a href='{}'>View </a>".format(reverse('orders:admin_order_detail',args=[order.id])))

class OrderedItemInline(admin.TabularInline):
	model=OrderedItem
	raw_id_fields=['product']
	extra=0

class OrderAdmin(admin.ModelAdmin):
	list_display=['id','full_name','phone_number','ordered_date','city','address','nearest_place','delivered','phone_verified',order_detail]
	list_editable=['delivered']
	list_filter=['delivered','phone_verified','ordered_date','updated_date']
	inlines=[OrderedItemInline]
	actions=[export_to_csv]

class CustomerAdmin(admin.ModelAdmin):
	list_display=['phone_number','frequency','points']

admin.site.register(Order,OrderAdmin)
admin.site.register(Customer,CustomerAdmin)