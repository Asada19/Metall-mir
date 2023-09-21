from django.db import models


class CallBack(models.Model):
    name = models.CharField(max_length=256, verbose_name='Имя')
    phone_number = models.IntegerField(verbose_name='Номер телефона')
    message = models.TextField(max_length=1000, blank=True, verbose_name='Сообщение')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    checked = models.BooleanField(default=False, verbose_name='Перезовнили')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = verbose_name


class Contacts(models.Model):
    address = models.CharField(max_length=300, blank=True, verbose_name='Адресс')
    maps_link = models.URLField(blank=True, verbose_name='Ссылка на адресс')
    email = models.EmailField(blank=True, verbose_name='Почта')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = verbose_name


class PhoneNumber(models.Model):
    phone_number = models.CharField(max_length=30, default='+996 (...) .. .. .. ', verbose_name='Номер')
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE, related_name='phone_numbers', verbose_name='Телефонные номера', blank=True)


class SocialMedia(models.Model):
    whatsapp = models.CharField(max_length=30, blank=True, verbose_name='WhatsApp')
    telegram = models.CharField(max_length=30, blank=True, verbose_name='Telegram')
    instagram = models.CharField(max_length=100, blank=True, verbose_name='Instagram')

    def save(self, *args, **kwargs):
        if self.whatsapp and 'http' not in self.whatsapp:
            self.whatsapp = f'https://wa.me/{self.whatsapp}/'
        if self.telegram and 'http' not in self.telegram:
            self.telegram = f'https://t.me/{self.telegram}/'
        if self.instagram and 'http' not in self.instagram:
            self.instagram = f'https://www.instagram.com/{self.instagram}/'

        super(SocialMedia, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Социальные сети'
        verbose_name_plural = verbose_name
