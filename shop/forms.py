from django import forms
from .models import Application, VendorAddedProducts

class ApplyToSellForm(forms.ModelForm):
	class Meta:
		model=Application
		fields=['name_of_shop','type_of_shop','location_of_shop','city','contact_no','first_name_of_owner','last_name_of_owner','contact_no_of_owner','percent_of_share_willing_to_give','delivery_by_self','can_make_brand_image_for_shop','question','accepts_tac']

		widgets={
			'type_of_shop':forms.TextInput(attrs={'placeholder':'Eg. electronics'}),
			'location_of_shop':forms.TextInput(attrs={'placeholder':'Eg. New Baneshwor Chowk'}),
			'city':forms.Select(attrs={'class':'span2'}),
			'percent_of_share_willing_to_give':forms.TextInput(attrs={'class':'span1'}),
			'delivery_by_self':forms.Select(attrs={'class':'span1'}),
			'can_make_brand_image_for_shop':forms.Select(attrs={'class':'span1'}),
			'question':forms.Textarea(attrs={'rows':5,'placeholder':'Your question here...'})
			}

class AddProductForm(forms.ModelForm):
	class Meta:
		model=VendorAddedProducts
		exclude=['added_to_products','vendor']