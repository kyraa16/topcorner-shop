from django.shortcuts import render, redirect, get_object_or_404
from .models import Product 
from .forms import ProductForm
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    # ambil beberapa produk dari database
    products_list = Product.objects.all() 
    
    context = {
        'title': 'Topcorner Shop',
        'name': 'Kadek Chandra Rasmi',
        'npm': '2406426473',
        'class': 'PBP E',
        'products': products_list,
    }
    return render(request, "main.html", context)

def crate_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, 'create_product.html', context)

def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)


# Function to return products in XML Format
def show_products_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize('xml', product_list)
    return HttpResponse(xml_data, content_type='application/xml')

# Function to return products in JSON Format
def show_products_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize('json', product_list)
    return HttpResponse(json_data, content_type='application/json') 

def show_product_xml_by_id(request, id):
    try:
        product_item = Product.objects.filter(pk=id)
        xml_data = serializers.serialize('xml', product_item)
        return HttpResponse(xml_data, content_type='application/xml')
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_product_json_by_id(request, id):
    try:
        product_item = Product.objects.filter(pk=id)
        json_data = serializers.serialize('json', product_item)
        return HttpResponse(json_data, content_type='application/json')
    except Product.DoesNotExist:
        return HttpResponse(status=404)