from django.contrib import admin
from catalog.models import Product, Category


@admin.register(Product)
class StudentAdmin(admin.ModelAdmin):
	list_display = ('id', 'product_name', 'price', 'category', 'preview_icon')
	list_filter = ('category',)
	search_fields = ('product_name', 'product_description',)


@admin.register(Category)
class StudentAdmin(admin.ModelAdmin):
	list_display = ('id', 'category_name')
