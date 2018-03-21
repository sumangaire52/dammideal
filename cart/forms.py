from django import forms

class AddProductToCartForm(forms.Form):
	quantity=forms.IntegerField(min_value=1,initial=1,widget=forms.NumberInput(attrs={'class':'span1'}))
	update=forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)
