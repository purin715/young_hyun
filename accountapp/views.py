from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def young(request):
    if request.method == 'POST':
        return render(request, 'accountapp/young.html', context={'text':'POST METHOD!'})
    else:
        return render(request, 'accountapp/young.html', context={'text': 'GET METHOD!'})