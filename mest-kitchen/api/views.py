from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def print_hello_world(request):
    return HttpResponse("<h2> hello world </h2>")

def print_json(request):
    return JsonResponse({"key": "value"})