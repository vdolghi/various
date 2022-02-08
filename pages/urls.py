from nturl2path import url2pathname
from django.urls import path
from .views import AboutPageView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]
