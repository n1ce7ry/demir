from django.urls import path
from . import views


urlpatterns = [
    path('add/', views.add_proposal, name='add_proposal'),
    path('delete/<int:proposal_id>/', views.delete_proposal, name='delete_proposal'),
]