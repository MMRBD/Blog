from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(request, 'blog/home_page.html')
    # return HttpResponse('Home Page')


def about(request):
    return render(request, 'blog/about.html')
    # return HttpResponse('About Page')

