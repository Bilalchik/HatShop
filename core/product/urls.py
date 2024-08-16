from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.CapListViews.as_view(), name='index'),
    path('index/<int:pk>/',views.CapDetailViews.as_view(), name='detail'),

    path('index/profil/',views.UserProfilViews.as_view(), name='profil')
]
