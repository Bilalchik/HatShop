from django.shortcuts import get_object_or_404
from .models import Cap

from rest_framework import status
from rest_framework.views import Response, APIView
from rest_framework.decorators import api_view
from .serializers import (
    ImageListSerializer,
    CategoryListSerializer,
    CapListSerializer,
    CapDetailSerializer
)


class CapListView(APIView):

    def get(self, request):
        caps = Cap.objects.all()

        serializer = CapListSerializer(caps, many=True)
        return Response(serializer.data)


class CapDetailView(APIView):

    def get(self, request, pk):
        cap = get_object_or_404(Cap, id=pk)
        serializer = CapDetailSerializer(cap)

        return Response(serializer.data)
