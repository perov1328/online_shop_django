
from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import *

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='category'),
    path('contact/', ContactsView.as_view(), name='contacts'),
    path('products/', ProductListView.as_view(), name='products'),
    path('<int:pk>/products/', ProductsCategoryListView.as_view(), name='category_product'),
    path('<int:pk>/products/create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/position/update/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/position/updatemoderator/', ProductModeratorUpdateView.as_view(), name='product_update_moderator'),
    path('<int:pk>/position/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('<int:pk>/position/', cache_page(60)(ProductDetailView.as_view()), name='position'),
    path('blogs/', BlogListView.as_view(), name='list'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete')
]

