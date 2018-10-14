from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(request, 'home_page.html')
    # return HttpResponse('Home Page')


def about(request):
    return render(request, 'about.html')
    # return HttpResponse('About Page')

