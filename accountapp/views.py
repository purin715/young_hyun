from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accountapp.models import HelloWorld


def young(request):

    if request.method == 'POST':
        temp = request.POST.get('input')
        new_data = HelloWorld()
        new_data.text = temp
        new_data.save()

        return HttpResponseRedirect(reverse('accountapp:young'))
        # data_list = HelloWorld.objects.all()
        #
        # return render(request, 'accountapp/young.html', context={'data_list' : data_list})
    else:
        data_list = HelloWorld.objects.all()
        return render(request, 'accountapp/young.html', context={'data_list' : data_list})