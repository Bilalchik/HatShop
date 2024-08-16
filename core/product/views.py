from django.shortcuts import get_object_or_404
from django.db.models import F
from .models import Product, Banner, Brand, Category, Image

from rest_framework import status
from rest_framework.views import Response, APIView
from .serializers import (
    ProductListSerializer,
    ProductDetailSerializer,
    BannerListSerializer,
    BrandListSerializer,
    SpecialProductListSerializer
)


class ProductListView(APIView):
    def get(self, request):
        banners = Banner.objects.all()
        brands = Brand.objects.all()
        bestsellers = Product.objects.all()
        special_products = Product.objects.filter(discount_price__lt=F('price'))

        # Serializers
        banner_serializer = BannerListSerializer(banners, many=True)
        brand_serializer = BrandListSerializer(brands, many=True)
        bestsellers_serializer = ProductListSerializer(bestsellers, many=True)
        special_products_serializer = SpecialProductListSerializer(special_products, many=True)

        data = {
            "banners": banner_serializer.data,
            "brands": brand_serializer.data,
            "bestsellers": bestsellers_serializer.data,
            "special_products": special_products_serializer.data,
        }

        return Response(data)


class ProductDetailView(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        serializer = ProductDetailSerializer(product)

        return Response(serializer.data)


