from django.contrib import admin
from .models import Category, Subcategory, Manufacturer,Offer, Product, Carousal, Color, Size, Application
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
	list_display=['name']
	prepopulated_fields={'slug':('name',)}

class SubcategoryAdmin(admin.ModelAdmin):
	list_display=['name']
	prepopulated_fields={'slug':('name',)}

class ManufacturerAdmin(admin.ModelAdmin):
	list_display=['name']
	prepopulated_fields={'slug':('name',)}

'''class VendorAdmin(admin.ModelAdmin):
	list_display=['name']
	prepopulated_fields={'slug':('name',)}'''

class OfferAdmin(admin.ModelAdmin):
	list_display=['name','duration']
	prepopulated_fields={'slug':('name',)}

class ProductAdmin(admin.ModelAdmin):
	list_display=['name','id','price','stock','discount_price','for_sale','total_sells','available','created']
	list_editable=['price','stock','for_sale','available']
	list_filter=['created','updated','category','sub_category','vendor','manufactured_by','offer','available']
	prepopulated_fields={'slug':('name',)}

class CarousalAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':('name',)}

class ApplicationAdmin(admin.ModelAdmin):
	list_display=['name_of_shop','applied_date']

admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Subcategory,SubcategoryAdmin)
admin.site.register(Manufacturer,ManufacturerAdmin)
#admin.site.register(Vendor,VendorAdmin)
admin.site.register(Offer,OfferAdmin)
admin.site.register(Carousal,CarousalAdmin)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Application,ApplicationAdmin)