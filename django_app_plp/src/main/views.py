from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main_view(request):
    return render(request, "views/main.html", {"name" : "Hive"})
