from django.contrib import admin
from .models import Item, OrderItem, Order

# Register your models here.

admin.site.register(OrderItem)
admin.site.register(Order)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'slug')
    prepopulated_fields = {'slug': ('title',),}