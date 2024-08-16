from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.ProductListView.as_view())
]
