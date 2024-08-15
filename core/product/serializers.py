from rest_framework import serializers

from .models import Cap, Category, Banner, Image, Brand, Size


class BannerListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banner
        fields = '__all__'

class BrandListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'

class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('title',)

class CapListSerializer(serializers.ModelSerializer):

    category = CategoryListSerializer(many=True)

    class Meta:
        model = Cap
        fields = (
            'id',
            'title',
            'price',
            'category',
            'logo'
        )


class DiscountListSerializer(serializers.ModelSerializer):

    category = CategoryListSerializer(many=True)


    class Meta:
        model = Cap
        fields = (
            'id',
            'title',
            'price',
            'discount_price',
            'category',
            'logo',
        )


class ImageDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('id',
                  'image'
                  )

class BrandDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('title',)

class SizeDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size
        fields = ('name',)

class CapDetailSerializer(serializers.ModelSerializer):

    category = CategoryListSerializer(many=True)
    images = ImageDetailSerializer(many=True)
    brands = BrandDetailSerializer(many=True)
    size = SizeDetailSerializer(many=True)

    class Meta:
        model = Cap
        fields = '__all__'