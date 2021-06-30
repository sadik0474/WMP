from django.shortcuts import render,get_object_or_404
from .models import Category, Product
# Create your views here.


def product_all(request):
    return render(request ,'store/home.html' , {'products': Product.products.all()} )

def all_categories(request):
    return render(request, 'home.html', {'category1':Category.objects.all()})

def category_list(request, category_slug=None):
    print('inside category_list')

    category = get_object_or_404(Category, slug=category_slug)
    print(f'print :{category}')
    products = Product.objects.filter(category=category)
    print(f'print :{products}')

    return render(request, 'store/products/category.html', {'category': category, 'products': products})

def product_detail(request, slug):
    print('pro detail')
    product=get_object_or_404(Product , slug=slug)
    return render(request, 'store/products/detail.html', {'product': product})


