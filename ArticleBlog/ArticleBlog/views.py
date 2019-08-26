# from django.http import HttpResponse
from django.shortcuts import HttpResponse, render, redirect


def index(request):
    return HttpResponse('<h1 style="color: skyblue;">Hello World</h1>')


def login(request):
    return render(request, 'login.html')


def show(request):
    return redirect("https://github.com/bestwishfang")


def introduce(request, name, num):
    return HttpResponse('<h1 style="color: blue;">Hello name: {}, number: {}</h1>'.format(name, num))
