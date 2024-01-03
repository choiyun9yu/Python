from django.urls import path, include
from . import views

urlpatterns = [
    path('food/<str:menu>', views.detail),
    path('', views.index),
]
