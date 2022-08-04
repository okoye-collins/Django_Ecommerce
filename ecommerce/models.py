from unicodedata import category
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
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='')
    label = models.CharField(max_length=30, choices=LABEL_CHOICES, default= '')

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items =  models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date =  models.DateTimeField()
    ordered = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username