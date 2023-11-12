from django.conf import settings
from django.core.cache import cache
from catalog.models import Category

def category_cache():
    key = 'categories_list'
    if settings.CACHE_ENABLED:
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.all()
            cache.set(key, category_list)
        else:
            category_list = Category.objects.all()
    return category_list