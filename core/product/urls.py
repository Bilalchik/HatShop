from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.MainPageView.as_view()),
    path('index/<int:pk>/', views.ProductDetailView.as_view()),
    path('basket_create/', views.BasketCreateView.as_view()),
    path('product_list/', views.ProductListView.as_view()),
]
