from django.urls import path
from src import views

"""
Define path for HTML pages
"""

urlpatterns = [
    path("", views.home, name = "home"), 
    path("manage/<employee_id>", views.staff_manage, name = "staff_manage"),
    path("delete_mission/<mission_id><employee_id>",views.delete_mission,name="delete_mission"),
    path("update_mission/<mission_id><employee_id>",views.update_mission,name="update_mission"),
    path("staff",views.staff,name='staff'),
    path("update_employee/<employee_id>",views.update_employee,name="update_employee"),
    path("delete_employee/<employee_id>",views.delete_employee,name="delete_employee"),
    path("MCP",views.mcp,name="MCP"),
    path("vehicle",views.vehicle,name="vehicle"),
    path("update_vehicle/<vehicle_id>",views.update_vehicle,name="update_vehicle"),
    path("delete_vehicle/<vehicle_id>",views.delete_vehicle,name="delete_vehicle"),
    path("update_mcp/<mcp_id>",views.update_mcp,name="update_mcp"),
    path("delete_mcp/<mcp_id>",views.delete_mcp,name="delete_mcp"),
    ]