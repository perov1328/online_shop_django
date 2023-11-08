from django.contrib import admin
from catalog.models import Product, Category, Blog, Version

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Класс админки для категорий
    """
    list_display = ('id', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Класс админки для продуктов
    """
    list_display = ('id', 'name', 'purchase_price', 'category', 'is_published',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    """
    Класс админки для версии продукта
    """
    list_display = ('product', 'version_number', 'version_name', 'is_valid',)
    list_filter = ('product',)
    search_fields = ('product',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """
    Класс админки для продуктов
    """
    list_display = ('id', 'title', 'date_of_creation',)
    list_filter = ('title',)
