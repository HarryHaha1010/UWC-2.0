from django.contrib import admin
from .models import Employee, MCP, Vehicle, WorkDay
from . import datas

class WorkDayAdmin(admin.ModelAdmin):
    list_display = ("work_day",)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name",'age','phone_num', 'address','curr_status', 'work_day')

class MCPsAdmin(admin.ModelAdmin):
    list_display = ('address', 'capacity', 'curr_status')

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('weight', 'capacity', 'fuel_capacity', 'curr_status')



admin.site.register(Employee, EmployeeAdmin)
admin.site.register(MCP, MCPsAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(WorkDay, WorkDayAdmin)