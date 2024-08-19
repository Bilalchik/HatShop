from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.ProductListView.as_view()),
    path('index/<int:pk>/', views.ProductDetailView.as_view()),
]
