from rest_framework import serializers
from .models import Catalog, Item, ItemField, MainPriceFile, OurClientsLogo, OurProvidersLogo


class CatalogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Catalog
        fields = '__all__'


class ItemFieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemField
        fields = ('title', 'value')


class ItemSerializer(serializers.ModelSerializer):
    fields = ItemFieldSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ('id', 'title', 'fields')


class CatalogDetailSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Catalog
        fields = ('id', 'title', 'items', 'price_file')


class CatalogDescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Catalog
        fields = ('id', 'title', 'description', 'image', 'price_file')


class OurClientsLogoSerializer(serializers.ModelSerializer):

    class Meta:
        model = OurClientsLogo
        fields = '__all__'


class OurProvidersLogoSerializer(serializers.ModelSerializer):

    class Meta:
        model = OurProvidersLogo
        fields = '__all__'


class MainPriceFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainPriceFile
        fields = '__all__'
