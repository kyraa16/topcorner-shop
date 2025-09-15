from django.shortcuts import render, redirect, get_object_or_404
from .models import Product 
from .forms import ProductForm

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