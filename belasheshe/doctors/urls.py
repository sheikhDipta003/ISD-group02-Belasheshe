from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/<int:doctor_id>/<str:date>/', views.DashboardView.as_view(), name='doctor_dashboard'),
    # path('dashboard/', views.DashboardView.as_view(), name='doctor_dashboard'), # testing
    path('add_prescription/', views.addSuggesions.as_view(), name='add_prescription'),
    path('create_appointment/', views.createAppointment.as_view(), name='create_appointment'),
]
