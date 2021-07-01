from django.urls import path

from accountapp.views import young

app_name = 'accountapp'

urlpatterns = [
    path('young/', young, name='young')
]