from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('catalog/', views.catalog, name='catalog'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
]