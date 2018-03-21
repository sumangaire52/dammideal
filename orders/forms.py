from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
	class Meta:
		model=Order
		fields=['full_name','address','city','nearest_place','phone_number']
		widgets= {
			'phone_number': forms.NumberInput(attrs={'placeholder':'Eg. 9861950320'}),
			'address':forms.Textarea(attrs={'rows':5,'placeholder':'Eg. Ranibari Chowk, Samakhushi, Kathmandu'}),
			'nearest_place':forms.Textarea(attrs={'rows':5,'placeholder':'Eg. Ranibari police station'})
		}

class PhoneVerificationForm(forms.Form):
	code=forms.CharField(max_length=5,widget=forms.NumberInput(attrs={'placeholder':'Enter code here'}))