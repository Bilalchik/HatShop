from rest_framework.views import APIView, Response
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from django.db.models import F
from django_filters import rest_framework as filters

from .models import Category, Image, Brand, Product, Banner, Basket
from .serializers import (
    ProductListSerializers, BannerListSerializer, BrandListSerializer, SpecialProductListSerializers,
    BrandCreateSerializer, ProductDetailSerializer, BasketCreateSerializer)
from .filters import ProductListFilter
from .paginations import ProductPagination


class MainPageView(APIView):

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


class BasketCreateView(generics.CreateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketCreateSerializer


class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializers
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = ProductListFilter
    ordering_fields = ['created_date', 'price']
    search_fields = ['title']
    pagination_class = ProductPagination

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True)

        return queryset


