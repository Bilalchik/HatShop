from rest_framework import serializers
from .models import Cap, Image, Category


class ImageListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('id', 'file')


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'title')


class CapListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cap
        fields = ('id', 'title', 'photo')


class CapDetailSerializer(serializers.ModelSerializer):
    images = ImageListSerializer(many=True)

    class Meta:
        model = Cap
        fields = '__all__'
