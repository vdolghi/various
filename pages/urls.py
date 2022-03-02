from django.urls import path
from .views import *    

urlpatterns = [
    path('', home_page_view, name='home'),
    path('accounts/signup', signupPage, name='account_signup'),
    path('products/<str:category>/<str:availability>/<str:order>/<int:pagination>/<int:page>/', product_grid_view, name='product_grid'),
    path('products/<slug:product_slug>/', product_page_view, name= 'product_page'), 
    path('privacy', privacy_policy_view, name='privacy_policy'),
    path('shipping', shipping_returns_view, name='shipping_returns'),
    path('accessibility', accessibility_statement_view, name='accessibility'),
    path('terms', tos_view, name='terms_of_service'),
    path('reviews', my_reviews_view, name='my_reviews'),
    path('reviews/delete/<int:obj_id>', my_reviews_view, name='my_reviews'),
    path('reviews/update/<int:obj_id>', my_reviews_view, name='my_reviews'),
    path('search', search_result_view, name='search_results'),
]
