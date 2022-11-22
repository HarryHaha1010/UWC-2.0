from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Django!")

def index(request, name):
    return render(
        request,
        "src/index.html",
        {
            'name': name
        }
    )