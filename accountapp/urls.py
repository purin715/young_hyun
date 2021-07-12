from django.urls import path

from accountapp.views import young, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('young/', young, name='young'),

    path('create/', AccountCreateView, name='create')
]