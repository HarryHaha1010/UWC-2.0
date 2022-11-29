from django.urls import path
from src import views

"""
Define path for HTML pages
"""

urlpatterns = [
    path("", views.home, name = "home"), 
    path("src/staff/manage", views.staff_manage, name = "staffs_manage"),
    path("src/staff", views.staff, name = "staff"),
    path("src/MCP", views.MCP, name = "MCP"),
    path("src/vehicle", views.vehicle, name = "vehicle"),
    ]