from django.db import models


class Catalog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, null=True)
    image = models.ImageField(upload_to='media', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = verbose_name


class Item(models.Model):
    title = models.CharField(max_length=100, blank=True)
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


