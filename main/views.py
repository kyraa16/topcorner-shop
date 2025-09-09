from django.shortcuts import render
from .models import Product 

# Create your views here.
def show_main(request):
    # ambil beberapa produk dari database
    products = Product.objects.all()[:5]  # ambil 5 produk pertama
    
    context = {
        'title': 'Topcorner Shop',
        'name': 'Kadek Chandra Rasmi',
        'npm': '2406426473',
        'class': 'PBP E',
        'products': products,
    }
    return render(request, "main.html", context)