from django.shortcuts import get_object_or_404, redirect, render
from .models import Item, Order, OrderItem
from django.utils import timezone

# Create your views here.

def homePage(request):

    context = {
        'items': Item.objects.all()

    }
    return render(request, 'home.html', context)


def productPage(request, product):
    product = get_object_or_404(Item, slug=product)

    context = {
        'product': product
    }
    return render(request, 'product_page.html', context)


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item = OrderItem.objects.create(item=item)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists(): 
            order_item.quantity += 1
            order_item.save()
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date = ordered_date)
        order.items.add(order_item)
        return redirect ('ecommerce:product_page', slug=slug)
    return render(request)

def checkout(request):
    return render(request, 'checkout_page.html')