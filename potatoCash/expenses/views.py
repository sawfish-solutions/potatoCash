from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Expenses

def index(request):
    allExpenses = Expenses.objects.all().values()
    template = loader.get_template('index-bulma.html')
    context = {
        'allExpenses': allExpenses,
    }
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))