from django.urls import path
from main.views import show_main, crate_product, show_product, show_products_xml, show_products_json, show_product_xml_by_id, show_product_json_by_id, register, login_user, logout_user, edit_product, delete_product, add_product_entry_ajax
from main.views import edit_product_entry_ajax, delete_product_entry_ajax, register_ajax, login_ajax, logout_ajax, proxy_image, create_product_flutter, show_my_products_json
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', crate_product, name='create_product'),
    path('product/<str:id>/', show_product, name='show_product'),
    path('xml/', show_products_xml, name='show_products_xml'),
    path('json/', show_products_json, name='show_products_json'),
    path('json/my-products/', show_my_products_json, name='show_my_products_json'),
    
    path('xml/<str:id>/', show_product_xml_by_id, name='show_product_xml_by_id'),
    path('json/<str:id>/', show_product_json_by_id, name='show_product_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),

    path("create-product-ajax/", add_product_entry_ajax, name="add_product_entry_ajax"),
    path("edit-product-ajax/", edit_product_entry_ajax, name="edit_product_ajax"),
    path("delete-product-ajax/", delete_product_entry_ajax, name="delete_product_ajax"),

    path("register-ajax/", register_ajax, name="register_ajax"),
    path("login-ajax/", login_ajax, name="login_ajax"),
    path("logout-ajax/", logout_ajax, name="logout_ajax"),

    path('proxy-image/', proxy_image, name='proxy_image'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]
