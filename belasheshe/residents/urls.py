from django.urls import path
from .views import DashboardView, ResidentPhyStatusView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('phy_status/<str:member_id>/', ResidentPhyStatusView.as_view(), name='phy_status'),
]
