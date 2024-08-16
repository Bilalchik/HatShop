from rest_framework import serializers

from .models import Category, Image, Brand, Product, Banner


class BannerListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banner
        fields = '__all__'


class BrandListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ('id', 'logo', 'title')


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('title', )


class ProductListSerializers(serializers.ModelSerializer):
    category = CategoryListSerializer()

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'category',
            'logo',
            'price',
        )


class SpecialProductListSerializers(serializers.ModelSerializer):
    category = CategoryListSerializer()

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'category',
            'logo',
            'price',
            'discount_price'
        )
