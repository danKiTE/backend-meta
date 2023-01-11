from django.urls import path, include
from . import views

urlpartterns = [
    path('home/', views.home, name = "home"),
]