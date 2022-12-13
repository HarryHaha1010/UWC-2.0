from django.shortcuts import render, redirect
from django.http import HttpResponse
from .import datas
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.db.models import Max
"""
Sites pre-defining (HTML web pages)
"""

# Home page
def home(request):
   return render(request,'index.html')

# Staff management page
def staff_manage(request, employee_id):
    employee = Employee.objects.get(pk = employee_id)
    if request.method  == "POST":
        form = MissionForm(request.POST)
        if form.is_valid():
            form.instance.route = form.cleaned_data['route'] = datas.result
            form.save()
            max = Mission.objects.all().aggregate(Max('id'))['id__max']
            if not max:
                max = 1
            employee.mission.add(Mission.objects.get(pk = max))
            missions = employee.mission.all()
            return HttpResponseRedirect('/manage/%s' % employee_id)
    else:
        form = MissionForm
    missions = employee.mission.all()
    return render(request, 'manage.html', {'employee':employee, 'form': form, 'missions':missions})

def delete_mission(request, mission_id, employee_id):
    mission = Mission.objects.get(pk=mission_id)
    mission.delete()
    return HttpResponseRedirect('/manage/%s' % employee_id)
def update_mission(request, mission_id, employee_id):
    mission = Mission.objects.get(pk=mission_id)
    form = MissionForm(request.POST or None, instance=mission)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/manage/%s' % employee_id)
    return render(request, 'update_smt.html', {'form': form})
    

def staff(request):
    employees = Employee.objects.all()
    if request.method  == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/staff')
    else:
        form = EmployeeForm
    return render(request, 'danhSachNhanVien.html', {'employees':employees, 'form': form})


def delete_employee(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    employee.delete()
    return redirect('staff') 

def update_employee(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('staff') 
    return render(request, 'update_smt.html', {'form': form})


def mcp(request):
    MCPs = MCP.objects.all()
    if request.method  == "POST":
        form = MCPForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/MCP')
    else:
        form = MCPForm
    return render(request,'tramThuGom.html', {'MCPs': MCPs, 'form': form})

def update_mcp(request, mcp_id):
    mcp = MCP.objects.get(pk=mcp_id)
    form = MCPForm(request.POST or None, instance=mcp)
    if form.is_valid():
        form.save()
        return redirect('MCP') 
    return render(request, 'update_smt.html', {'form': form})

def delete_mcp(request, mcp_id):
    mcp = MCP.objects.get(pk=mcp_id)
    mcp.delete()
    return redirect('MCP') 

def vehicle(request):
    vehicles = Vehicle.objects.all()
    if request.method  == "POST":
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/vehicle')
    else:
        form = VehicleForm
    return render(request,'phuongTien.html', {'vehicles': vehicles, 'form': form})

def update_vehicle(request, vehicle_id):
    vehicle = Vehicle.objects.get(pk=vehicle_id)
    form = VehicleForm(request.POST or None, instance=vehicle)
    if form.is_valid():
        form.save()
        return redirect('vehicle') 
    return render(request, 'update_smt.html', {'form': form})

def delete_vehicle(request, vehicle_id):
    vehicle = Vehicle.objects.get(pk=vehicle_id)
    vehicle.delete()
    return redirect('vehicle') 