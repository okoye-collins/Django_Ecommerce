from django.shortcuts import render
from .models import Item

# Create your views here.

def homePage(request):

    context = {
        'items': Item.objects.all()

    }
    return render(request, 'home.html', context)


def checkout(request):
    return render(request, 'checkout_page.html')

def productPage(request):
    return render(request, 'product_page.html')