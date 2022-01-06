from django.shortcuts import render

def main_home(request):
    return render(request, '../templates/base.html')


"""
from django.http import HttpResponse
def main_home(request):
    return HttpResponse("Hello, world. You're at the polls index.")"""