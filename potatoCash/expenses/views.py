from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Expenses

def index(request):
    allExpenses = Expenses.objects.all().values()
    template = loader.get_template('exp_index.html')
    context = {
        'allExpenses': allExpenses,
    }
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addexpense(request):
    a = request.POST['user_name']
    b = request.POST['first_name']
    c = request.POST['last_name']
    d = request.POST['exp_category']
    e = request.POST['exp_value']
    expense = Expenses(username=a, firstname=b, lastname=c, expcategory=d, expvalue=e)
    expense.save()
    return HttpResponseRedirect(reverse('exp_index'))

def delete(request, id):
    expense = Expenses.objects.get(id=id)
    expense.delete()
    return HttpResponseRedirect(reverse('exp_index'))