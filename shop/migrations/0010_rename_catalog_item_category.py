# Generated by Django 4.2.5 on 2023-09-22 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_rename_category_item_catalog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='catalog',
            new_name='category',
        ),
    ]