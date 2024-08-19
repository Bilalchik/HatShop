from rest_framework.views import APIView, Response
from rest_framework import generics
from django.db.models import F

from .models import Category, Image, Brand, Product, Banner
from .serializers import (
    ProductListSerializers, BannerListSerializer, BrandListSerializer, SpecialProductListSerializers,
    BrandCreateSerializer, ProductDetailSerializer)


class ProductListView(APIView):

    def get(self, request):

        # Querysets
        banners = Banner.objects.all()
        brands = Brand.objects.all()
        bestsellers = Product.objects.all()
        special_products = Product.objects.filter(discount_price__lt=F('price'))

        # Serializers
        banner_serializer = BannerListSerializer(banners, many=True)
        brand_serializer = BrandListSerializer(brands, many=True)
        bestsellers_serializer = ProductListSerializers(bestsellers, many=True)
        special_products_serializer = SpecialProductListSerializers(special_products, many=True)

        data = {
            "banners": banner_serializer.data,
            "brands": brand_serializer.data,
            "bestsellers": bestsellers_serializer.data,
            "special_products": special_products_serializer.data,
        }

        return Response(data)


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

    def get(self, request, *args, **kwargs):
        product = self.queryset.first()

        product_serializer = ProductDetailSerializer(product)

        recommended_products = Product.objects.filter(category=product.category).exclude(id=product.id)

        recommended_products_serializer = ProductListSerializers(recommended_products, many=True)

        return Response({
            "detail": product_serializer.data,
            "recommended_products": recommended_products_serializer.data
        })


