from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Product, Brand


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    brand = BrandSerializer()

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        brand_data = validated_data.pop('brand')
        brand, created = Brand.objects.get_or_create(name=brand_data['name'])
        product = Product.objects.create(**validated_data, brand=brand)
        return product

    def update(self, instance, validated_data):
        try:
            brand_data = validated_data.get('brand')
            brand, created = Brand.objects.get_or_create(
                name=brand_data['name'])
        except TypeError:
            brand = instance.brand
        instance.brand = brand
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.color = validated_data.get('color', instance.color)
        instance.ram = validated_data.get('ram', instance.ram)
        instance.rom = validated_data.get('rom', instance.rom)
        instance.save()

        return instance
