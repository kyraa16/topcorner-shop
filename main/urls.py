from django.urls import path
from main.views import show_main, crate_product, show_product, show_products_xml, show_products_json, show_product_xml_by_id, show_product_json_by_id, register, login_user, logout_user, edit_product, delete_product

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', crate_product, name='create_product'),
    path('product/<str:id>/', show_product, name='show_product'),
    path('xml/', show_products_xml, name='show_products_xml'),
    path('json/', show_products_json, name='show_products_json'),
    path('xml/<str:id>/', show_product_xml_by_id, name='show_product_xml_by_id'),
    path('json/<str:id>/', show_product_json_by_id, name='show_product_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
]
