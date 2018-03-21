from .models import Category, Carousal

def categories(request):
	return {'categories':Category.objects.all()}

def carousal_products(request):
	return {'carousal_products':Carousal.objects.all()}