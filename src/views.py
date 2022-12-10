from django.shortcuts import render, redirect
from django.http import HttpResponse
from .import datas
"""
Sites pre-defining (HTML web pages)
"""

# Home page
def home(request):
   return render(request,'index.html')
def staff(request):
    return render(request, 'nhanvien.html')
# Staff management page
def staff_manage(request):
    return render(request, "src/staff_manage.html", {'missions': datas.missions})
def MCP(request):
    return render(request,'tramThuGom.html')
def vehicle(request):
    return render(request,'phuongTien.html')