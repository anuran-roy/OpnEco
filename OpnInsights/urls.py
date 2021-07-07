from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('results/', views.analyze),
]