from django.shortcuts import render

# Create your views here.


def aus(request):
    return render(request,'aus.html')

def starc(request):
    return render(request,'starc.html')


def smith(request):
    return render(request, 'smith.html')

def cummins(request):
    return render(request, 'cummins.html')

def head(request):
    return render(request,'head.html')