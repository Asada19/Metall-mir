from django.db import models


class Catalog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=1000, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='media', blank=True, verbose_name='Изображение')
    price_file = models.FileField(upload_to='prices', blank=True, verbose_name='Файл с ценами')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = verbose_name


class Item(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Название')
    category = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name='items', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = verbose_name


class ItemField(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Поле')
    value = models.CharField(max_length=100, blank=True, verbose_name='Значение')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='fields', blank=True)

    def __str__(self):
        return f'{self.title}:{self.value}'

    class Meta:
        verbose_name = 'Поле со значением'
        verbose_name_plural = verbose_name


class OurClientsLogo(models.Model):
    image = models.ImageField(upload_to='clients_logo', verbose_name='изображение')

    def __str__(self):
        return self.image.__str__()

    class Meta:
        verbose_name = 'Логитипы клиентов'
        verbose_name_plural = verbose_name


class OurProvidersLogo(models.Model):
    image = models.ImageField(upload_to='providers_logo', verbose_name='изображение')

    def __str__(self):
        return self.image.__str__()

    class Meta:
        verbose_name = 'Логитипы поставщиков'
        verbose_name_plural = verbose_name
