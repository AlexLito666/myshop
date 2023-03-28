from django.shortcuts import render, get_object_or_404
from .models import Category, Product


# пиредствление главная страница
def index(request):
    categories = Category.objects.all()
    context_dict = {'categories': categories}
    return render(request, 'shop/index.html', context_dict)


# предствление катеuории товара
def category_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context_dict = {'category': category,
                    'categories': categories,
                    'products': products}
    return render(request, 'shop/category_list.html', context_dict)


# предствлене товара
def product_detail(request, product_detail_slug):
    product = get_object_or_404(Product,
                                slug=product_detail_slug,
                                available=True)
    context_dict = {'product': product}
    return render(request, 'shop/product_detail.html', context_dict)
