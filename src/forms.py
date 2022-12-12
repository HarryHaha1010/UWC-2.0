from django import forms
from django.forms import ModelForm
from .models import *

class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = "__all__"
        labels = {
            'weight' : 'Trọng lượng',
            'capacity' : 'Sức chứa',
            'fuel_capacity' : 'Xăng tiêu thụ',
            'curr_status'  : 'Trạng thái'
        }
        widgets = {
            'weight' : forms.TextInput(attrs={'class':'form-control'}),
            'capacity' : forms.TextInput(attrs={'class':'form-control'}),
            'fuel_capacity' : forms.TextInput(attrs={'class':'form-control'}),
            'curr_status'  : forms.Select()
        }

class MCPForm(ModelForm):
    class Meta:
        model = MCP
        fields = "__all__"
        labels = {
            'name' : 'Tên',
            'address' : 'Địa chỉ',
            'capacity' : 'Sức chứa',
            'curr_status'  : 'Trạng thái'
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'address' : forms.TextInput(attrs={'class':'form-control'}),
            'capacity' : forms.TextInput(attrs={'class':'form-control'}),
            'curr_status'  : forms.Select()
        }

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = {'name', 'age', 'phone_num', 'address', 'curr_status'}
        labels = {
            'name' : 'Tên Nhân Viên',
            'age': 'Tuổi',
            'phone_num' : 'Số điện Thoại',
            'address' : 'Địa chỉ',
            'curr_status'  : ' 	Trình trạng hoạt động'
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'age' : forms.TextInput(attrs={'class':'form-control'}),
            'phone_num' : forms.TextInput(attrs={'class':'form-control'}),
            'address' : forms.TextInput(attrs={'class':'form-control'}),
            'curr_status'  : forms.Select()
        }

class MissionForm(ModelForm):
    class Meta:
        model = Mission
        fields = '__all__'
        # fields = {'name', 'age', 'phone_num', 'address', 'curr_status'}
        labels = {
            'name' : 'Tên Công Việc',
            'description': 'Mô tả công việc',
            'MCP' : 'MCP',
            'vehicle' : 'Phương Tiện',
            'Route'  : 'Tuyến đường'
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.TextInput(attrs={'class':'form-control'}),
            'MCP': forms.Select(),
            'vehicle': forms.Select(),
            'Route' : forms.TextInput(attrs={'class':'form-control'}),
        }