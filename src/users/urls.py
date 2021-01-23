from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import *

# users/
urlpatterns = [
    path('register/', RegisterAPI.as_view()),
]