from django.urls import path

from .views import index,createProduct

app_name='produits'

urlpatterns=[
    path('', index, name='index'),
    path('create-produit/', createProduct.as_view(), name='create_produit')
] 