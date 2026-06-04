from django.contrib import admin
from django.urls import path
from .views import*
urlpatterns = [
    path("home",homepg),
    path("contact",contact),
    path("profile",profile)
]
