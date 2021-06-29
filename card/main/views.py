from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def projects(request):
    return render(request, 'main/project.html')


def contacts(request):
    return render(request, 'main/contac.html')
