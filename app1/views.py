from django.shortcuts import render

# Create your views here.


def india(request):
    return render(request, 'india.html')


def virat(request):
    return render(request,'virat.html')

def rohit(request):
    return render(request, 'rohit.html')

def sachin(request):
    return render(request,'sachin.html')


def gill(request):
    return render(request, 'gill.html')