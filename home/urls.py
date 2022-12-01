from django.urls import path
from home.views import index,preview,player

urlpatterns = [
    path('', index),
    path('movie/<str:mid>',preview),
    path('player/<str:mid>',player)
]