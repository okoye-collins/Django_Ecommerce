from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from django.db import models

# Create your models here.

CATEGORY_CHOICES = (
    ('', ''),
    ('SHIRT', 'Shrit'),
    ('SPORT_WARE', 'Sport ware'),
    ('OUTWARE', 'Outware')
)

LABEL_CHOICES = (
    ('', ''),
    ('PRIMARY', 'primary'),
    ('SECONDARY', 'secondary'),
    ('Danger', 'danger')
)
class Item(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField(null=True, blank=True)
    description = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='')
    label = models.CharField(max_length=30, choices=LABEL_CHOICES, default= '')
    publish = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("ecommerce:product_page", args=[self.slug])

    def get_add_to_cart_url(self):
        return reverse("ecommerce:add_to_cart_page", args=[self.slug])


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items =  models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date =  models.DateTimeField()
    ordered = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username