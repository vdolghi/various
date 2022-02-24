from django.urls import path
from .views import *    

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('accounts/signup', signupPage, name='account_signup'),
]
