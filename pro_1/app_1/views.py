from django.shortcuts import render
from django.http import HttpResponse

def main_home(request):
    return render(request, '../templates/base.html')

def password_que(request):
    return render(request, '../templates/password_que.html')

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")