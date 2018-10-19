from rest_framework import serializers

from ..models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'date', 'latitud', 'longitud', 'image', 'created')


class ProductSerializerPost(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'price', 'date', 'latitud', 'longitud')
