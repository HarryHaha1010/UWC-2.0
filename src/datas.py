from .models import WorkDay, Employee, Vehicle, MCP


# this template
missions = [('1', 'Cong viec hang ngay ne'), ('2', "Cong viec thu 2 ne")]

list_Emloyee = Employee.objects.all()
list_Vehicle = Vehicle.objects.all()
list_MCP = MCP.objects.all()
list_wd = WorkDay.objects.all()
result = 'MCP2 -> MCP3 -> MCP1 -> MCP2'
# list_task_report 