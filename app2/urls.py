from app2.views import *
from django.urls import path

app_name = 'something'
urlpatterns  = [
    path('aus/',aus, name='aus'),
    path('starc/', starc, name='starc'),
    path('smith/',smith, name='smith'),
    path('cummins/', cummins, name='cummins'),
    path('head/',head,name='head'),
]