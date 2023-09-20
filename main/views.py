from rest_framework import generics
from .serializers import ContactsSerializer, SocialMediaSerializer, CallBackSerializer
from .models import Contacts, CallBack, SocialMedia


class CallBackCreateAPIView(generics.CreateAPIView):
    """ Форма обрртной связи """
    model = CallBack
    serializer_class = CallBackSerializer
    queryset = CallBack.objects.all()


class ContactsAPIView(generics.ListAPIView):
    """ Контакты для связи """
    model = Contacts
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()


class SocialMediaAPIView(generics.ListAPIView):
    """ Социальные сети """
    model = SocialMedia
    serializer_class = SocialMediaSerializer
    queryset = SocialMedia.objects.all()
