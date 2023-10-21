
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import *

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='category'),
    path('contact/', ContactsView.as_view(), name='contacts'),
    path('products/', ProductListView.as_view(), name='products'),
    path('<int:pk>/products/', ProductsCategoryListView.as_view(), name='category_product'),
    path('<int:pk>/position/', ProductDetailView.as_view(), name='position'),
    path('blogs/', BlogListView.as_view(), name='list'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete')
]

