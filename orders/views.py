from django.shortcuts import render, get_object_or_404
from .forms import OrderForm, PhoneVerificationForm
from cart.cart import Cart 
from .models import OrderedItem, Order, Customer
from authy.api import AuthyApiClient
from django.views.decorators.http import require_POST
from django.contrib.admin.views.decorators import staff_member_required

authy_api=AuthyApiClient('vS0dpkDvF2eMcwdFkPrvqeXlvqT5Xt5I')
def create_order(request):
	cart=Cart(request)
	verification_form=PhoneVerificationForm()
	phone_list=Customer.objects.values_list('phone_number',flat=True)
	if cart.get_total_price() <= 5000:
		delivery_charge = 50
	else:
		delivery_charge = 0
	total_price=cart.get_total_price() + delivery_charge

	if request.method=='POST':
		form=OrderForm(request.POST)

		if form.is_valid():
			order=form.save()
			cd=form.cleaned_data
			phone_number=str(cd['phone_number'])
			request.session['phone_number']=phone_number
			request.session['full_name']=cd['full_name']
			authy_api.phones.verification_start(phone_number, '+977', via='sms')

			for item in cart:
				if 'color' and 'size' in item:
					OrderedItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'],color=item['color'],size=item['size'])
				elif 'color' in item:
					OrderedItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'],color=item['color'])
				elif 'size' in item:
					OrderedItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'],size=item['size'])
				else:
					OrderedItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])
			cart.clear()
			return render(request,'order/verify.html',{'order':order,'verification_form':verification_form})
	else:
		form=OrderForm()
		context={
			'form':form,
			'delivery_charge':delivery_charge,
			'total_price':total_price,
		}
	return render(request,'order/order.html',context)

@require_POST
def verify(request,order_id):
	order=get_object_or_404(Order,id=order_id)
	form=PhoneVerificationForm(request.POST)
	phone_list=Customer.objects.values_list('phone_number',flat=True)

	if form.is_valid():
		cd=form.cleaned_data
		code=cd['code']
		phone_number=request.session.get('phone_number')
		full_name=request.session.get('full_name')

		#Checking if code user has entered is correct or not

		if authy_api.phones.verification_check(phone_number, '+977', code).ok():
			order.phone_verified=True
			order.save()

			if phone_number not in phone_list:
				new_customer=Customer.objects.create(full_name=full_name,phone_number=phone_number)
				new_customer.frequency=1
				if order.get_total_cost()<=500:
					new_customer.points=25
				elif 501<=order.get_total_cost()<=1000:
					new_customer.points=50
				elif 1001<=order.get_total_cost()<=2000:
					new_customer.points=100
				elif 2001<=order.get_total_cost()<=5000:
					new_customer.points=300
				elif 5001<=order.get_total_cost()<=7000:
					new_customer.points=400
				elif 7001<=order.get_total_cost()<=10000:
					new_customer.points=450
				elif order.get_total_cost()>10000:
					new_customer.points=750
				new_customer.save()

			else:
				customer=get_object_or_404(Customer,phone_number=phone_number)
				customer.frequency+=1
				if order.get_total_cost()<=500:
					customer.points+=25
				elif 501<=order.get_total_cost()<=1000:
					customer.points+=50
				elif 1001<=order.get_total_cost()<=2000:
					customer.points+=100
				elif 2001<=order.get_total_cost()<=5000:
					customer.points+=300
				elif 5001<=order.get_total_cost()<=7000:
					customer.points+=400
				elif 7001<=order.get_total_cost()<=10000:
					customer.points+=450
				elif order.get_total_cost()>10000:
					customer.points+=750
				customer.save()

			return render(request,'order/ordered.html',{'order':order})

		else:
			error_message='Sorry that code did not work.'
			verification_form=PhoneVerificationForm()
			context={
				'error_message':error_message,
				'verification_form':verification_form,
			}
			return render(request,'order/verify.html',context)

#Customizing the order detail view of admin site
@staff_member_required
def admin_order_detail(request,order_id):
	order=get_object_or_404(Order,id=order_id)
	return render(request,'admin/orders/order/detail.html',{'order':order})
