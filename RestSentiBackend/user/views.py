from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def getAllUser(request):
    return JsonResponse({'message': 'Hello, world!'})

def register(request):
    return JsonResponse({'message': 'Reg!'})