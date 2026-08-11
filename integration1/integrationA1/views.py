from django.shortcuts import render, HttpResponse
from . models import PomodoroTodo

def home(request):
    return render(request, 'home.html')

def todos(request):
    items = PomodoroTodo.objects.all()
    return render(request, 'todos.html', {'todos': items})