from rest_framework.views import APIView, Response
from django.db.models import F

from .models import Category, Image, Brand, Product, Banner
from .serializers import (
    ProductListSerializers, BannerListSerializer, BrandListSerializer, SpecialProductListSerializers)


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

