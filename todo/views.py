from django.shortcuts import render, redirect
from .models import Task
from django.utils import timezone

# Create your views here.
def homepage(request):
    if request.method == 'POST':
        taskObj = Task()
        taskObj.title = request.POST.get('title')
        taskObj.description = request.POST.get('description')
        taskObj.tag = request.POST.get('tag')
        taskObj.status = request.POST.get('status')
        taskObj.created_date = timezone.now()
        taskObj.save()
        return render(request, 'todo/home.html', {'added': True})
    return render(request, 'todo/home.html')

def alltask(request):
    tasks = Task.objects.all()
    return render(request, 'todo/alltask.html', {'tasks' : tasks})

def update(request, task_id):
    taskDetails = Task.objects.filter(id=task_id)
    if request.method == 'POST':
        taskObj = Task.objects.get(id = task_id)
        taskObj.title = request.POST.get('title')
        taskObj.description = request.POST.get('description')
        taskObj.tag = request.POST.get('tag')
        taskObj.status = request.POST.get('status')
        taskObj.updated_date = timezone.now()
        taskObj.save()
        return redirect(alltask)
        # return render(request, 'todo/update.html', {'updated': True})
    return render(request, 'todo/update.html', {'task':taskDetails})
        
def delete(request, task_id):
    instance = Task.objects.get(id = task_id)
    instance.delete()
    return render(request, 'todo/alltask.html', {'deleted': True})

def incomplete(request):
    tasks = Task.objects.filter(status = 'Incomplete')
    return render(request, 'todo/incomplete.html', {'tasks' : tasks})

def tag(request):
    tasks = Task.objects.all()
    return render(request, 'todo/tag.html', {'tasks' : tasks})

def markcomplete(request, task_id):
    taskObj = Task.objects.get(id = task_id)
    if (taskObj.status == 'Completed'):
        taskObj.status = "Incomplete"
    elif (taskObj.status == 'Incomplete'):
        taskObj.status = "Completed"
    taskObj.save()
    tasks = Task.objects.all()
    return render(request, 'todo/alltask.html', {'tasks' : tasks})