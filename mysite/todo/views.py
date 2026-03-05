from django.shortcuts import render
from .models import todo
from django.views import View
from django.views.generic import ListView

def todo_list(request):
    todos = todo.objects.all()
    return render(request, "todo.html", {"todos": todos})
