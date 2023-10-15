from django.shortcuts import render
from catalog.models import Category, Product

# Create your views here.
def homepage(request):
    context = {
        'objects_list': Category.objects.all(),
        'title': 'Категории наших товаров'
    }
    return render(request, 'catalog/homepage.html', context)

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f"{name} ({phone}): {message}")

    return render(request, 'catalog/contact.html')

def products(request):
    context = {
        'objects_list': Product.objects.all(),
        'title': 'Полный список наших товаров'
    }
    return render(request, 'catalog/products.html', context)


def category_product(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'objects_list': Product.objects.filter(category_id=pk),
        'title': f'Товары из категории: {category_item.name}'
    }
    return render(request, 'catalog/products.html', context)

def position(request, pk):
    position_name = Product.objects.get(id=pk)
    context = {
        'objects_list': Product.objects.filter(id=pk),
        'title': f'{position_name.name}'
    }
    return render(request, 'catalog/position.html', context)
