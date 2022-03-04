from django.conf import settings 
from django.shortcuts import render, redirect, get_object_or_404
from pages.models import Product
from .forms import ShoppingCartAddProductForm
from decimal import Decimal
from django.core.mail import send_mail
from django.utils.html import strip_tags

def get_cart(request):
    shopping_cart = request.session.get(settings.CART_ID)
    if not shopping_cart:
        shopping_cart = request.session[settings.CART_ID] = {}
    return shopping_cart

def shopping_cart_add(request, product_id):
    shopping_cart = get_cart(request)
    product = get_object_or_404(Product, id=product_id)
    product_id = str(product.id)
    form = ShoppingCartAddProductForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data 
        if product_id not in shopping_cart:
            shopping_cart[product_id] = {'quantity' : 0, 'price' : str(product.price)} 
        if request.POST.get('overwrite_qty' ):
            shopping_cart[product_id]['quantity'] = data['quantity']
        else:
            shopping_cart[product_id]['quantity'] += data['quantity' ] 
        request.session.modified = True  
    else:
        if product_id not in shopping_cart:
            shopping_cart[product_id] = {'quantity' : 1, 'price' : str(product.price)}
        else:
            shopping_cart[product_id]['quantity'] += 1
        request.session.modified = True 
    return redirect('cart:shopping_cart_detail' )

def shopping_cart_detail(request):
    shopping_cart = get_cart(request)
    product_ids = shopping_cart.keys()
    cart_total = Decimal(0.0)
    products = Product.objects.filter(id__in=product_ids)
    temp_cart = shopping_cart.copy() 
    for product in products:
        cart_item = temp_cart[str(product.id)]
        cart_item['product'] = product
        cart_item['total'] = (Decimal(cart_item['price']) * cart_item['quantity' ])
        cart_total += cart_item['total']
        cart_item['update_quantity_form'] = ShoppingCartAddProductForm(initial={'quantity' : cart_item['quantity']})
    return render(request, 'detail.html', { 'shopping_cart': temp_cart.values(), 'shopping_cart_total' : cart_total})

def shopping_cart_remove(request, product_id):
    shopping_cart = get_cart(request)
    product_id = str(product_id)
    if product_id in shopping_cart:
        del shopping_cart[product_id] 
        request.session.modified = True  
        return redirect('cart:shopping_cart_detail' )

def shopping_cart_clear(request):
    del request.session[settings.CART_ID]

def send_order_email(request):
    shopping_cart = get_cart(request)
    product_ids = shopping_cart.keys()
    cart_total = Decimal(0.0)
    products = Product.objects.filter(id__in=product_ids)
    temp_cart = shopping_cart.copy()
    message=f"<h4>Order for customer {request.user.first_name} {request.user.last_name}</h4"
    message += f"<br>"
    message += f"<p><strong>Products:</strong></p>"
    for product in products: 
        cart_item = temp_cart[str(product.id)]
        cart_item['product'] = product
        cart_item['total'] = (Decimal(cart_item['price']) * cart_item['quantity'])
        message += f"<p>{product.name} X {cart_item['quantity']} items =======> {cart_item['total']} &euro;</p>"
        cart_total += cart_item['total']
        message += f"<br>"
        message += f"<p><strong>Total: {cart_total} &euro;</strong></p>"
    
    plain_message = strip_tags(message)
    send_mail(f"New order from {request.user.first_name} {request.user.last_name}", plain_message, 'madcoder@vineyard.com', [settings.DEFAULT_FROM_EMAIL], html_message=message)
    request.session[settings.CART_ID] = {}
    return render(request, 'home.html') 
    


        
