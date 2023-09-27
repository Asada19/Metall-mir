# Generated by Django 4.2.5 on 2023-09-27 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_rename_catalog_item_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurClientsLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='clients_logo', verbose_name='изображение')),
            ],
            options={
                'verbose_name': 'Логитипы клиентов',
                'verbose_name_plural': 'Логитипы клиентов',
            },
        ),
        migrations.CreateModel(
            name='OurProvidersLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='providers_logo', verbose_name='изображение')),
            ],
            options={
                'verbose_name': 'Логитипы поставщиков',
                'verbose_name_plural': 'Логитипы поставщиков',
            },
        ),
        migrations.AddField(
            model_name='catalog',
            name='price_file',
            field=models.FileField(blank=True, upload_to='prices', verbose_name='Файл с ценами'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='description',
            field=models.TextField(max_length=1000, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='image',
            field=models.ImageField(blank=True, upload_to='media', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Название'),
        ),
    ]
