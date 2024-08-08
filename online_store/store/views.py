from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from online_store.cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    card_multipliers = range(2)
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {'category': category, 'categories': categories, 'products': products,
               'card_multipliers': card_multipliers}
    return render(request, 'store/product/list.html', context)


def product_detail(request, pk, slug):
    product = get_object_or_404(Product, pk=pk, slug=slug, available=True)
    # Добавляем кнопку добавить товар
    cart_product_form = CartAddProductForm()
    context = {'product': product, 'cart_product_form': cart_product_form}
    return render(request, 'store/product/detail.html', context)


def main_page(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'store/main_page.html', context)


def site_info(request):
    return render(request, 'store/site_info.html')



