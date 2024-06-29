from django.shortcuts import render
from django.http import HttpResponse

def data_view(request):
    return HttpResponse("<h1>Сведений не хватает</h1>")

def test_view(request):
    return HttpResponse("<h1>Тестируем до потери пульса</h1>")


