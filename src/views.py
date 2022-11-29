from django.shortcuts import render, redirect
from django.http import HttpResponse

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
    return render(
        request,
        "src/staff_manage.html"
    )

# Staff main page
def staff(request):
    return HttpResponse("This is staff main page")

# MCPs main page
def MCP(request):
    return HttpResponse("This is MCPs main page")

# Vehicle main page
def vehicle(request):
    return HttpResponse("This is vehicle main page")

