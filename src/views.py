from django.shortcuts import render, redirect
from django.http import HttpResponse
from .import datas
"""
Sites pre-defining (HTML web pages)
"""

# Home page
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return HttpResponse("WELCOME TO UWC 2.0! This is our home page")

# Staff management page
def staff_manage(request):
    return render(request, "src/staff_manage.html", {'missions': datas.missions})
