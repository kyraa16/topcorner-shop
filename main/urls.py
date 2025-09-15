from django.urls import path
from main.views import show_main, crate_product, show_product

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', crate_product, name='create_product'),
    path('product/<str:id>/', show_product, name='show_product'),
]
