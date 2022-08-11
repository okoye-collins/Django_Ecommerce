from django.shortcuts import get_object_or_404, redirect, render
from .models import Item, Order, OrderItem
from django.utils import timezone
from django.contrib import messages

# Create your views here.

def homePage(request):

    context = {
        'items': Item.objects.all()

    }
    return render(request, 'home.html', context)


def productPage(request, slug):
    product = get_object_or_404(Item, slug=slug)

    context = {
        'product': product
    }
    return render(request, 'product_page.html', context)


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        print('======= remove',order.items.filter(item__slug=item.slug))
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists(): 
            order_item.quantity += 1
            order_item.save()
            messages.info(request, f'{item} was quantity has been updated')
        else:
            messages.info(request, f'{item} was added to your cart')
            order.items.add(order_item) 
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date = ordered_date)
        order.items.add(order_item)
        messages.info(request, f'{item} was added to your cart')
    return redirect ('ecommerce:product_page', slug=slug)


def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item =  OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
            order.items.remove(order_item)  
            messages.info(request, f'{item} have remove from your cart')           
        else:
            messages.info(request, f'{item} was not in your cart')
            return redirect ('ecommerce:product_page', slug=slug)           
    else:
        messages.info(request, f'You does not have an active order')
        return redirect ('ecommerce:product_page', slug=slug)

    return redirect ('ecommerce:product_page', slug=slug)


def checkout(request):
    return render(request, 'checkout_page.html')