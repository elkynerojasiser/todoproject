from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.

def landing(request):
    return render(request,'index.html')

def projects(request):
    projects = Project.objects.all()
    return render(request,'projects/list.html',{
        "projects" : projects
    })

def detailOfProject(request,project_id):
    project = get_object_or_404(Project, id=project_id) 
    tasks = Task.objects.filter(project_id=project_id)
    return render(request,'projects/detail.html',{
        "project": project,
        "tasks" : tasks
    })

def showCreateProjectForm(request):
    return render(request,'projects/create.html')

def storeProject(request):
    Project.objects.create(
        name=request.POST["name"],
        description=request.POST["description"]
    )
    return redirect("projects.list")

def showUpdateProjectForm(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request,'projects/update.html',{
        "project" : project
    })

def updateProject(request,project_id):
    project = get_object_or_404(Project, id=project_id)
    project.name=request.POST["name"]
    project.description=request.POST["description"]
    
    project.save()
    return redirect('projects.list')

def confirmDeleteProject(request,project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, "projects/delete.html", {
        "project": project
    })

def destroyProject(request,project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return redirect('projects.list')

def tasks(request):
    tasks = Task.objects.all()
    return render(request,'tasks/list.html',{
        "tasks": tasks
    })

def showCreateTaskForm(request):
    projects = Project.objects.all()
    return render(request,'tasks/create.html',{
        "projects" : projects
    })

def storeTask(request):
    Task.objects.create(
        title=request.POST['title'],
        description=request.POST['description'],
        project_id=request.POST['project_id']
    )

    return redirect('tasks.list')


def showUpdateTaskForm(request, task_id):
    projects = Project.objects.all()
    task = get_object_or_404(Task, id=task_id)
    return render(request,'tasks/update.html',{
        "projects" : projects,
        "task": task
    })

def updateTask(request,task_id):
    task = get_object_or_404(Task, id=task_id)
    task.title=request.POST["title"]
    task.description=request.POST["description"]
    task.done=request.POST["done"]
    task.project_id=request.POST["project_id"]
    task.save()
    return redirect('tasks.list')

def confirmDeleteTask(request,task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, "tasks/delete.html", {
        "task": task
    })

def destroyTask(request,task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('tasks.list')