from django.shortcuts import render, get_object_or_404
from .models import Category, Product


# пиредствление главная страница
def index(request):
    return render(request, 'shop/index.html')


# предствление каталога
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context_dict = {'category': category,
                    'categories': categories,
                    'products': products}
    return render(request, 'shop/product_list.html', context_dict)


# предствлене товара
def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    context_dict = {'product': product}
    return render(request, 'shop/product_detail.html', context_dict)
