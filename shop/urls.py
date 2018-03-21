from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='shop'
urlpatterns=[]

#urlpatterns for index view
urlpatterns+=[
	path('',views.index,name='index'), #default index view
	
]

#urlpatterns for product_detail view
urlpatterns+=[
	path('<int:product_id>/<slug:product_slug>/',views.product_detail,name='product_detail'),
]

#urlpatterns for products view
urlpatterns+=[
	path('products/',views.products,name='products'),
	path('products/<slug:category_slug>/',views.products,name='products_by_category'), #index view if caetegory is provided
	path('products/<slug:category_slug>/<slug:subcategory_slug>/',views.products,name='products_by_subcategory'), #index view if subcategory is provided
	path('products/manufacturer/<slug:manufacturer_slug>/',views.products,name='products_by_manufacturer'), #index view if manufacturer is provided
	path('products/seller/<slug:seller_slug>/',views.products,name='products_by_seller'), #index view if seller is provided
	path('products/<slug:offer_slug>/',views.products,name='products_by_offer'), #index view if offer is provided
]
#urlpatterns for search view
urlpatterns+=[
	path('search/',views.search,name='search'),
]

urlpatterns+=[
	path('like/<int:product_id>/<slug:product_slug>/',views.like,name='like'),
	path('dislike/<int:product_id>/<slug:product_slug>/',views.dislike,name='dislike'),
	path('faq/',views.faq,name='faq'),
	path('apply-to-sell/',views.apply_to_sell,name='apply_to_sell'),
	path('terms-and-conditions/',views.tac,name='tac'),
	path('return-policy/',views.return_policy,name='return_policy'),
	path('contact/',views.contact,name='contact'),
]

#Login and logout views
urlpatterns+=[
	path('login/',auth_views.login,name='login'),
	path('logout/',auth_views.logout,name='logout'),
	path('logout-then-login/',auth_views.logout_then_login,name='logout_then_login'),
	path('vendor_dashboard/',views.vendor_dashboard,name='vendor_dashboard'),
]

#Views to add and remove products by vendors
urlpatterns+=[
	path('add-product/',views.add_product,name='add_product'),
]