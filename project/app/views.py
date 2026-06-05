from django.shortcuts import render,redirect
from .models import Data
from django.contrib.auth.models import User
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

def login_page(request):
    return render(request,'login.html')

def register_page(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        password=request.POST.get('pass')
        User.objects.create_user(username=name,password=password)
        return redirect('login_page')
    return render(request,'register.html')