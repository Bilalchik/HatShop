from rest_framework import serializers
from .models import Brand, Banner, Image, Category, Product


class ImageListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('id', 'file')


class BannerListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banner
        fields = '__all__'


class BrandListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ('id', 'title', 'logo')


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('title', )


class ProductListSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer()

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'category',
            'photo',
            'price'
        )


class SpecialProductListSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer()

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'category',
            'photo',
            'price',
            'discount_price'
        )


class ProductDetailSerializer(serializers.ModelSerializer):
    images = ImageListSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'
