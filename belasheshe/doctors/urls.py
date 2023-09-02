from django.urls import path
from . import views

urlpatterns = [
    path('medical_conditions/', views.member_medical_conditions, name='member_medical_conditions'),
]
