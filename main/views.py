import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from .models import Product 
from .forms import ProductForm
from django.http import HttpResponse
from django.core import serializers

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.contrib.auth.models import User

import json
import requests

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)
    
    context = {
        'title': 'Topcorner Shop',
        'name': 'Kadek Chandra Rasmi',
        'username': request.user.username,
        'npm': '2406426473',
        'class': 'PBP E',
        'products': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html", context)

def crate_product(request):
    form = ProductForm(request.POST or None)
    
    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, 'create_product.html', context)

@login_required(login_url='/login')
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
    data = [
        {   
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'stock': product.stock,
            'brand': product.brand,
            'rating': product.rating,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'user_id': product.user_id,
        } 
        for product in product_list
    ]
    # json_data = serializers.serialize('json', product_list)
    # return HttpResponse(json_data, content_type='application/json') 
    return JsonResponse(data, safe=False)

def show_product_xml_by_id(request, id):
    try:
        product_item = Product.objects.filter(pk=id)
        xml_data = serializers.serialize('xml', product_item)
        return HttpResponse(xml_data, content_type='application/xml')
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_product_json_by_id(request, id):
    try:
        product_item = get_object_or_404(Product.objects.select_related('user'), pk=id)
        data = {   
            'id': str(product_item.id),
            'name': product_item.name,
            'price': product_item.price,
            'description': product_item.description,
            'thumbnail': product_item.thumbnail,
            'category': product_item.category,
            'is_featured': product_item.is_featured,
            'stock': product_item.stock,
            'brand': product_item.brand,
            'rating': product_item.rating,
            'created_at': product_item.created_at.isoformat() if product_item.created_at else None,
            'user_id': product_item.user.username if product_item.user_id else None,
            # return a clear key for username
            'user_username': product_item.user.username if product_item.user else None,
        } 
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response


def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))


@csrf_exempt
@require_POST
@login_required(login_url="/login")
def add_product_entry_ajax(request):
    # Ambil data dari form
    name = strip_tags(request.POST.get("name"))
    price = strip_tags(request.POST.get("price"))
    description = strip_tags(request.POST.get("description"))
    category = strip_tags(request.POST.get("category"))
    thumbnail = strip_tags(request.POST.get("thumbnail"))
    is_featured = request.POST.get("is_featured", "false").lower() == "true"
    stock = strip_tags(request.POST.get("stock"))
    brand = strip_tags(request.POST.get("brand"))
    rating = request.POST.get("rating") or 0
    user = request.user if request.user.is_authenticated else None

    new_product = Product(
        name=name,
        price=price,
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        stock=stock,
        brand=brand,
        rating=rating,
        user=user,
    )
    new_product.save()

    return HttpResponse(b"Product created successfully", status=201)

@require_POST
@login_required(login_url="/login")
def edit_product_entry_ajax(request):
    product_id = strip_tags(request.POST.get("id"))
    product = get_object_or_404(Product, pk=product_id)

    if request.user != product.user:
        return HttpResponse(b"Unauthorized", status=401)
    if product is None:
        return HttpResponse(b"Product not found", status=404)

    name = strip_tags(request.POST.get("name"))
    price = strip_tags(request.POST.get("price"))
    description = strip_tags(request.POST.get("description"))
    category = strip_tags(request.POST.get("category"))
    thumbnail = strip_tags(request.POST.get("thumbnail"))
    is_featured = request.POST.get("is_featured", "false").lower() == "true"
    stock = strip_tags(request.POST.get("stock"))
    brand = strip_tags(request.POST.get("brand"))
    rating = request.POST.get("rating", 0)

    product.name = name
    product.price = price
    product.description = description
    product.category = category
    product.thumbnail = thumbnail
    product.is_featured = is_featured
    product.stock = stock
    product.brand = brand
    product.rating = rating

    product.save()
    return HttpResponse(b"Product updated successfully", status=200)


@csrf_exempt
@require_POST
@login_required(login_url="/login")
def delete_product_entry_ajax(request):
    product_id = strip_tags(request.POST.get("id"))

    if not product_id:
        return HttpResponse(b"Product ID is required", status=400)

    product = get_object_or_404(Product, pk=product_id)

    if request.user != product.user:
        return HttpResponse(b"Unauthorized", status=401)
    if product is None:
        return HttpResponse(b"Product not found", status=404)

    product.delete()
    return HttpResponse(b"Product deleted successfully", status=200)

# @csrf_exempt
@require_POST
def register_ajax(request):
    try:
        username = strip_tags(request.POST.get("username"))
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if not username or not password1 or not password2:
            return JsonResponse(
                {"success": False, "message": "All fields are required"}, status=400
            )

        if password1 != password2:
            return JsonResponse(
                {"success": False, "message": "Passwords do not match"}, status=400
            )

        if User.objects.filter(username=username).exists():
            return JsonResponse(
                {"success": False, "message": "Username already exists"}, status=400
            )

        form_data = {
            "username": username,
            "password1": password1,
            "password2": password2,
        }
        form = UserCreationForm(form_data)

        if form.is_valid():
            form.save()
            return JsonResponse(
                {
                    "success": True,
                    "message": "Your account has been successfully created!",
                    "redirect": reverse("main:login"),
                },
                status=201,
            )
        else:
            errors = []
            for field, field_errors in form.errors.items():
                for error in field_errors:
                    errors.append(f"{field}: {error}")

            return JsonResponse(
                {"success": False, "message": "; ".join(errors)}, status=400
            )

    except Exception:
        return JsonResponse(
            {"success": False, "message": "An error occurred during registration"},
            status=500,
        )


# @csrf_exempt
@require_POST
def login_ajax(request):
    try:
        username = strip_tags(request.POST.get("username"))
        password = request.POST.get("password")

        if not username or not password:
            return JsonResponse(
                {"success": False, "message": "Username and password are required"},
                status=400,
            )

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            response = JsonResponse(
                {
                    "success": True,
                    "message": "Login successful!",
                    "redirect": reverse("main:show_main"),
                    "user": {"id": user.id, "username": user.username},
                }
            )
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return response
        else:
            return JsonResponse(
                {"success": False, "message": "Invalid username or password"},
                status=401,
            )

    except Exception:
        return JsonResponse(
            {"success": False, "message": "An error occurred during login"}, status=500
        )


# @csrf_exempt
@require_POST
def logout_ajax(request):
    try:
        logout(request)
        response = JsonResponse(
            {
                "success": True,
                "message": "Logout successful!",
                "redirect": reverse("main:login"),
            }
        )
        response.delete_cookie("last_login")
        return response

    except Exception:
        return JsonResponse(
            {"success": False, "message": "An error occurred during logout"}, status=500
        )
    

def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)


@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Strip HTML tags untuk keamanan
            name = strip_tags(data.get("name", ""))
            description = strip_tags(data.get("description", ""))
            category = strip_tags(data.get("category", ""))
            brand = strip_tags(data.get("brand", ""))
            
            # Validasi field required
            if not name or not description:
                return JsonResponse({
                    "status": "error",
                    "message": "Name and description are required"
                }, status=400)
            
            # Get data lainnya
            price = data.get("price", 0)
            thumbnail = data.get("thumbnail", "")
            is_featured = data.get("is_featured", False)
            stock = data.get("stock", 0)
            rating = data.get("rating", 0)
            
            # Validasi dan konversi tipe data
            try:
                price = int(price)
                stock = int(stock)
                rating = float(rating) 
            except (ValueError, TypeError):
                return JsonResponse({
                    "status": "error",
                    "message": "Invalid data type for price, stock, or rating"
                }, status=400)
            
            # Validasi nilai
            if price < 0:
                return JsonResponse({
                    "status": "error",
                    "message": "Price cannot be negative"
                }, status=400)
            
            if stock < 0:
                return JsonResponse({
                    "status": "error",
                    "message": "Stock cannot be negative"
                }, status=400)
            
            if rating < 0 or rating > 5:
                return JsonResponse({
                    "status": "error",
                    "message": "Rating must be between 0 and 5"
                }, status=400)
            
            # Validasi category
            valid_categories = ['jersey', 'shoes', 'ball', 'accessories', 'equipment']
            if category and category not in valid_categories:
                return JsonResponse({
                    "status": "error",
                    "message": f"Invalid category. Must be one of: {', '.join(valid_categories)}"
                }, status=400)
            
            user = request.user
            
            # Buat produk baru
            new_product = Product(
                name=name,
                description=description,
                price=price,
                category=category if category else 'accessories',  # default category
                brand=brand if brand else "",
                thumbnail=thumbnail if thumbnail else None,
                is_featured=is_featured,
                stock=stock,
                rating=rating,
                user=user
            )
            new_product.save()
            
            return JsonResponse({
                "status": "success",
                "message": "Product created successfully",
                "product": {
                    "id": str(new_product.id), 
                    "name": new_product.name,
                    "price": new_product.price,
                    "category": new_product.category,
                    "brand": new_product.brand,
                    "stock": new_product.stock,
                    "rating": new_product.rating,
                    "is_featured": new_product.is_featured,
                }
            }, status=201)
            
        except json.JSONDecodeError:
            return JsonResponse({
                "status": "error",
                "message": "Invalid JSON format"
            }, status=400)
        except Exception as e:
            return JsonResponse({
                "status": "error",
                "message": f"An error occurred: {str(e)}"
            }, status=500)
    else:
        return JsonResponse({
            "status": "error",
            "message": "Only POST method is allowed"
        }, status=405)
    
@login_required(login_url='/login')
def show_my_products_json(request):
    product_list = Product.objects.filter(user=request.user)  # Filter by user
    data = [
        {   
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'stock': product.stock,
            'brand': product.brand,
            'rating': product.rating,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'user_id': product.user_id,
        } 
        for product in product_list
    ]
    return JsonResponse(data, safe=False)