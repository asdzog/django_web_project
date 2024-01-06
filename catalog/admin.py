from django.contrib import admin
from catalog.models import Product, Category, Version


@admin.register(Product)
class StudentAdmin(admin.ModelAdmin):
	list_display = ('id', 'product_name', 'price', 'category', 'preview_icon')
	list_filter = ('category',)
	search_fields = ('product_name', 'product_description',)


@admin.register(Category)
class StudentAdmin(admin.ModelAdmin):
	list_display = ('id', 'category_name')


@admin.register(Version)
class VersioAdmin(admin.ModelAdmin):
	list_display = ('name_version', 'number_version',)
	list_filter = ('number_version', 'is_active', )
