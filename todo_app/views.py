from django.shortcuts import render, redirect
from django.http import HttpResponse
from todo_app.models import Task
from todo_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def index (request):
    return render(request, "index.html")

@login_required
def todolist (request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage = request.user
            instance.save()
        messages.success(request,("New Task Added!"))
    else:
        all_tasks = Task.objects.filter(manage=request.user)
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get("pg")
        all_tasks = paginator.get_page(page)
        return render(request, "todolist.html",{"all_tasks": all_tasks})
    return redirect("todolist")

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if(task.manage == request.user):
        task.delete()
        messages.success(request,("Task Deleted Successfully"))
    else:
        messages.error(request,("Access Restricted, You are not Allowed."))
    return redirect("todolist")

@login_required
def edit_task(request, task_id):
    if request.method == "POST":
        task = Task.objects.get(pk=task_id)
        form = TaskForm(request.POST or None , instance = task)
        if form.is_valid():
            form.save()
        messages.success(request,("Task Updated!"))
        return redirect("todolist")
    else:
        task_obj = Task.objects.get(pk=task_id)
        return render(request, "edit.html",{"task_obj": task_obj})
        
@login_required
def complete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if(task.manage == request.user):
        task.done = True
        task.save()
    else:
        messages.error(request,"Access Restricted, You are not Allowed")
    return redirect("todolist")

@login_required
def pending_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if(task.manage == request.user):
        task.done = False
        task.save()
    else:
        messages.error(request,"Access Restricted, You are not Allowed")
    return redirect("todolist")

def about (request):
    context = {
        "about_text" : "Welcome to About Page"
    }
    return render(request, "about.html",context)

def contact (request):
    context = {
        "contact_text" : "Welcome to Contact Page"
    }
    return render(request, "contact.html",context)
