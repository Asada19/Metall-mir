from rest_framework import serializers
from .models import Contacts, CallBack, PhoneNumber, SocialMedia


class CallBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallBack
        fields = '__all__'
        read_only_fields = ('checked',)


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ('phone_number', )


class ContactsSerializer(serializers.ModelSerializer):
    phone_numbers = PhoneNumberSerializer(many=True, read_only=True)

    class Meta:
        model = Contacts
        fields = ('address', 'email', 'maps_link', 'phone_numbers')


class SocialMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = SocialMedia
        fields = '__all__'
