from django.shortcuts import redirect, render
from .models import TaskList
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, 'index.html')

@login_required
def todolist(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.manager=request.user#by adding commit as argument we have delayed the form saving
            instance.save()
            messages.success(request, ("New Task Added"))
            return redirect('todolist') 
    else:
        all_tasks = TaskList.objects.filter(manager=request.user).order_by('id')
        paginator=Paginator(all_tasks,5)
        page=request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        context = {
            'all_tasks': all_tasks,
        }
        return render(request, 'todolist.html', context)


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')

@login_required
def delete_task(request, task_id):
    task=TaskList.objects.get(pk=task_id)
    if task.manager==request.user:
       task.delete()
       return redirect('todolist')


@login_required
def edit_task(request, task_id):  
    if request.method == 'POST':
        task=TaskList.objects.get(pk=task_id)
        form=TaskForm(request.POST or None,instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, ("Task Edited"))
            return redirect('todolist')
    else:
        task_obj = TaskList.objects.get(pk=task_id)
    context = {
        'task_obj': task_obj,
    }
    return render(request, 'edit.html', context)  


@login_required
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manager==request.user:
        task.done=True   
        task.save() 
        return redirect('todolist')

@login_required
def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manager==request.user:
        task.done=False 
        task.save()    
        return redirect('todolist') 

