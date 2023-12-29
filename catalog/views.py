from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product, Category


class HomeView(TemplateView):
    model = Product
    template_name = 'catalog/home.html'
    extra_context = {
        'title': 'home'
    }

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['products'] = Product.objects.all()
        return context


class ContactsPageView(View):

    def get(self, request):
        context = {'title': 'Контакты'}
        return render(request, 'catalog/contacts.html', context)

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
        context = {'title': 'Контакты'}
        return render(request, 'catalog/contacts.html', context)


class ProductDetailView(ListView):

    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        context = {
            'product': product,
            'title': f'{product.product_name}'
        }
        return render(request, 'catalog/product_detail.html', context)


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    # def get_success_url(self):
    #     return reverse('catalog/product_details.html', args=[self.object.pk])


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')

