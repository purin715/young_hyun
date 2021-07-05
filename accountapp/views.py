from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def young(request):
    return render(request, 'accountapp/young.html')