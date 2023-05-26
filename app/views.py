from django.shortcuts import render
from .models import Product, Brand, Category, Warranty
from django.db.models import Q

# Create your views here.

def index(request):
    products = Product.objects.all()
    brands = Brand.objects.all()
    categories = Category.objects.all()
    warranties = Warranty.objects.all()

    context = {
        'products' : products,
        'brands': brands,
        'categories': categories,
        'warranties': warranties,
    }
    return render(request, 'index.html', context)

def product_list(request):
    selected_option = request.GET.get('sort_by')
    price_from = request.GET.get('price_from')
    price_to = request.GET.get('price_to')
    print(selected_option)
    brands = request.GET.getlist('brands[]')
    categories = request.GET.getlist('categories[]')
    warranties = request.GET.getlist('warranties[]')

    products = Product.objects.all()

    if price_from and price_to:
        products = products.filter(price__gte=price_from, price__lte=price_to)

    if brands:
        products = products.filter(brand__in=brands)

    if categories:
        products = products.filter(category__in=categories)

    if warranties:
        warranty_q = Q()
        for warranty in warranties:
            warranty_q |= Q(warranty=warranty)
        products = products.filter(warranty_q)

    if selected_option == 'low_to_high':
        products = products.order_by('price')
    elif selected_option == 'high_to_low':
        products = products.order_by('-price')
    # print(products)

    context = {
        'products': products
    }

    return render(request, 'product_list_partial.html', context)