from django.shortcuts import render

from catalog.models import Product, Category


def home(request):
    context = {
        'products': Product.objects.all(),
        'categories': Category.objects.all(),
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
    return render(request, 'catalog/contacts.html')


def products(request):

    context = {
        'products': Product.objects.all(),
        'categories': Category.objects.all(),
    }
    return render(request, 'catalog/products.html', context)
