# Generated by Django 4.1 on 2022-08-04 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce", "0006_item_quantity"),
    ]

    operations = [
        migrations.RemoveField(model_name="item", name="quantity",),
        migrations.AddField(
            model_name="orderitem",
            name="quantity",
            field=models.IntegerField(default=1),
        ),
    ]
