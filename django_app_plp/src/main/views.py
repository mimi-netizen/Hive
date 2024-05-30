from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def main_view(request):
    return render(request, "views/main.html", {"name" : "Hive"})

@login_required
def home_view(request):
    return render(request, "views/home.html")
