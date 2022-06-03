from http import HTTPStatus
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import task as Task
from django.core import serializers
import json

# Create your views here.
def home(request):
    return HttpResponse("working!")

@csrf_exempt
def addTask(request):

    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['description']
        email = request.POST['email']

        newTask = Task(name=name, description=desc, email=email)
        newTask.save()

        return HttpResponse("Task Added Successfully!", status=200)

    else:
        return HttpResponse(status=404)

def viewTasks(request):

    if request.method == 'GET':
        values = list(Task.objects.values())
        return JsonResponse(values, safe=False)

    else:
        return HttpResponse("Invalid Request!", status=404)