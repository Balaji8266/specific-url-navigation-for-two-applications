from app1.views import *
from django.urls import path

app_name = 'anything'
urlpatterns=[
    path('india/',india,name='india'),
    path('virat/',virat,name='virat'),
    path('rohit/', rohit, name='rohit'),
    path('sachin/',sachin,name='sachin'),
    path('gill/',gill, name='gill'),
]