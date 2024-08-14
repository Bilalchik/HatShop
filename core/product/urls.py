from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.CapListView.as_view()),
    path('list/<int:pk>/', views.CapDetailView.as_view())
]
