from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You are at the expenses index.")
# Create your views here.
