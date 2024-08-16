from django.shortcuts import get_object_or_404
from rest_framework.views import Response, APIView
from rest_framework import status
from .models import MyUser
from .serializers import UserRegisterSerializer

class UserRegisterViews(APIView):
    def post(self, request):
        serializers = UserRegisterSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


