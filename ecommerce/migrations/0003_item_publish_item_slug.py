# Generated by Django 4.1 on 2022-08-04 13:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("ecommerce", "0002_item_category_item_label"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="publish",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="item",
            name="slug",
            field=models.SlugField(
                default="test product", max_length=250, unique_for_date="publish"
            ),
            preserve_default=False,
        ),
    ]
