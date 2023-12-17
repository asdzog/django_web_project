from django.urls import path
from .views import HomeView, ProductDetailView, ContactsPageView, ProductDetailView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts', ContactsPageView.as_view(), name='contacts'),
    path('product/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),

]