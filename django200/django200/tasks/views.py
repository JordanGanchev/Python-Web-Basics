
from django import http
from django.shortcuts import render

from django200.tasks.models import Task


def index_2(request):
    return http.HttpResponse('It works')


def get_all_tasks(request):
    all_tasks = Task.objects.order_by('priority').all()
    result = ', '.join(f'{t.name}({t.priority})' for t in all_tasks)
    return http.HttpResponse(result)


def index(request):
    all_tasks = Task.objects.all()
    result = ', '.join(f'{t.name}({t.age})' for t in all_tasks)
    context = {
        'title': 'The tasks app!',
        'tasks': result,
    }
    return render(request, 'index.html', context)
