from unicodedata import name
from django.urls import path
from . import views

app_name = 'ecommerce'

urlpatterns = [
    path('', views.homePage, name = 'home_page'),
    path('checkout', views.checkout, name='checkout_page'),
    path('product-page', views.productPage, name='product_page'),
]