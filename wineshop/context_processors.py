from ShoppingCart.views import get_cart
from decimal import Decimal 

def cart(request):
    cart = get_cart(request)
    cart_total_price = sum(Decimal(item['price' ]) * item['quantity' ] for item in cart.values())
    return { 'shopping_cart_total' : cart_total_price, 'shopping_cart_num': len(cart) }