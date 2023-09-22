from rest_framework import serializers
from .models import Catalog, Item, ItemField, Parameters, Field


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


class FieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'


class ParametersSerializer(serializers.ModelSerializer):
    fields = FieldsSerializer(many=True, read_only=True)

    class Meta:
        model = Parameters
        fields = ('id', 'fields')


class CatalogDetailSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    parameters = ParametersSerializer(read_only=True)

    class Meta:
        model = Catalog
        fields = ('id', 'title', 'parameters', 'items')


class CatalogDescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Catalog
        fields = ('id', 'title', 'description', 'image')
