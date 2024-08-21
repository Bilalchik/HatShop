from rest_framework import serializers

from .models import Category, Image, Brand, Product, Banner, Basket


class ImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


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


class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer()
    brands = BrandListSerializer(many=True)
    images = ImageListSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'brands',
            'category',
            'logo',
            'price',
            'discount_price',
            'description',
            'images',
            'get_size_display',
            'created_date',
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


class BrandCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ('logo', 'title')


class BasketCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Basket
        fields = (
            'user',
            'product',
            'quantity',
            'address',
        )

