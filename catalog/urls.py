
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import homepage, contacts, products, category_product, position

app_name = CatalogConfig.name

urlpatterns = [
    path('', homepage, name='homepage'),
    path('contacts/', contacts, name='contacts'),
    path('products/', products, name='products'),
    path('<int:pk>/products/', category_product, name='category_product'),
    path('<int:pk>/position/', position, name='position')
]

