from django.urls import path
from . import views

app_name='orders'
urlpatterns=[
	path('create/',views.create_order,name='create_order'),
	path('verify/<int:order_id>/',views.verify,name='verify'),
	path('admin/order/<int:order_id>/',views.admin_order_detail,name='admin_order_detail'),
]