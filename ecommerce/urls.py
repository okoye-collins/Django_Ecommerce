from django.urls import path
from . import views

app_name = 'ecommerce'

urlpatterns = [
    path('', views.homePage, name = 'home_page'),
    path('checkout', views.checkout, name='checkout_page'),
    path('product/<slug:product>/', views.productPage, name='product_page'),
    path('add_to_cart/<slug:add_to_cart>/', views.add_to_cart, name='add_to_cart_page'),
]