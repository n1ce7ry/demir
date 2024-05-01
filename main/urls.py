from . import views
from django.urls import path
from .forms import LoginForm
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('catalog/', views.catalog, name='catalog'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('register/', views.registration, name='registration'),
    path(
        'login/', auth_views.LoginView.as_view(
            template_name='main/login.html',
            authentication_form=LoginForm,
        ), name='login'), 
    path('logout/', views.user_logout, name="logout"),
]