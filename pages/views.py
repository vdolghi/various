from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from allauth.account.views import SignupView
from ShoppingCart.views import shopping_cart_add
from .forms import CustomUserCreationForm, ProductReviewForm
from ShoppingCart.forms import ShoppingCartAddProductForm
from django.contrib import messages
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage

class CustomSignUpView(SignupView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('account_login')
    template_name = 'account/signup.html'

def home_page_view(request):
    prod_nr = Product.objects.count()
    vendor_nr = len(Product.objects.all().values('vendor').distinct())
    stock_nr = sum([i.get('stock') for i in Product.objects.values('stock')])

    return render(request, 'home.html', {'prod_nr': prod_nr, 'vendor_nr': vendor_nr, 'stock_nr': stock_nr})

def privacy_policy_view(request):

    return render(request,'privacy.html')

def shipping_returns_view(request):

    return render(request,'shipping.html')

def accessibility_statement_view(request):

    return render(request,'accessibility.html')

def tos_view(request):

    return render(request,'terms.html')

def product_grid_view(request, category='all', availability='all', order='newest', pagination=50, page=1):
    
    product_images = ProductImage.objects.all()
    products = Product.objects.all()

    if category=='all':
        pass
    if category=='red':
        products = products.filter(category=Product.Category.RED)
    if category=='white':
        products = products.filter(category=Product.Category.WHITE)
    if category=='rose':
        products = products.filter(category=Product.Category.ROSE)

    if availability=='all':
        pass
    if availability=='outofstock':
        products = products.filter(stock=0)
    if availability=='lastproducts':
        products = products.filter(Q(stock__gt=0) & Q(stock__lte=10))
    if availability=='limited':
        products = products.filter(Q(stock__gt=10) & Q(stock__lte=25))
    if availability=='sufficient':
        products = products.filter(Q(stock__gte=25))

    if order=='newest':
        products = products.order_by('created_at')
    if order=='price_asc':
        products = products.order_by('price')
    if order=='price_desc':
        products = products.order_by('-price')
    if order=='popularity':
        pass # TBD
    if order=='discount':
        products = products.order_by('-discount')
    if order=='reviews':
        pass # TBD

    paginator = Paginator(products, pagination) # 50 products per page is the default
    try:
        page_obj = paginator.page(page)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
            
    return render(request, 'product_grid.html', { 'products': page_obj, 'product_images': product_images, 'category': category, 'availability': availability, 
                                                  'order': order, 'pagination': pagination, 'page': page })

def search_result_view(request):
    
    product_images = ProductImage.objects.all()
    products = Product.objects.all()

    if 'search' in request.GET:
        products = products.filter(name__icontains=request.GET['search'])

    return render(request, 'search_results.html', { 'search_results': products, 'product_images': product_images, 'query': request.GET['search'] })

def product_page_view(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug) 
    not_yet_reviewed = not product.review_exists_for_user(request.user.id)

    if request.method == 'POST' :
        form = ProductReviewForm(request.POST) 
        if form.is_valid():
            data = form.cleaned_data
            try:
                ProductReview.objects.get(product=product, user=request.user).delete()
            except ProductReview.DoesNotExist:
                pass # do nothing
            finally:
                ProductReview.objects.update_or_create(product = product, user = request.user, title = data['title'], content = data['content'], rating = data['rating'])

        return redirect('product_page', product_slug=product_slug)
    else:
        form = ProductReviewForm()
        shopping_cart_add_form = ShoppingCartAddProductForm()

    return render(request, 'product_page.html', {'product': product, 'not_yet_reviewed': not_yet_reviewed, 'review_form': form, 'cart_product_form': shopping_cart_add_form})

def my_reviews_view(request, obj_id=None):

    reviews = ProductReview.objects.filter(user = request.user)

    if 'delete' in request.build_absolute_uri():
         get_object_or_404(ProductReview, pk=obj_id).delete()
         return redirect('my_reviews')

    return render(request, 'my_review_list.html', {'reviews':reviews})

def signupPage(request):        
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('first_name') + form.cleaned_data.get('last_name')
            messages.success(request, 'Account was created for ' + user)
            return redirect('account_login')
    else:
        form = CustomUserCreationForm()
    context = {'form':form}
    return render(request, 'account/signup.html', context)