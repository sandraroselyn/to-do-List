from django.shortcuts import render,redirect
from .models import Data
# Create your views here.
def home(request):
    if request.method == "POST":
        name=request.POST.get('task-name')
        date=request.POST.get('task-date')
        Data.objects.create(task=name,date=date)
        return redirect('task_list')
    return render(request,'index.html')
def Delete_task(request,id):
    task=Data.objects.filter(id=id)
    task.delete()
    return redirect('task_list')
def task_list(request):
    task=Data.objects.all()
    return render(request,'task_list.html',{'task':task})

def update_task(request,id):
    a=Data.objects.get(id=id)
    if request.method == "POST":
        a.task=request.POST.get('task-name')
        a.date=request.POST.get('task-date')
        a.save()
        return redirect('task_list')
    return render(request,'update_task.html',{'a':a})