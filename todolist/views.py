from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages

# Create your views here.

def landing(request):
    return render(request,'index.html')

@login_required
def projects(request):
    projects = Project.objects.filter(user=request.user)
    return render(request,'projects/list.html',{
        "projects" : projects
    })

@login_required
def detailOfProject(request,project_id):
    project = get_object_or_404(Project, id=project_id) 
    tasks = Task.objects.filter(project_id=project_id)
    return render(request,'projects/detail.html',{
        "project": project,
        "tasks" : tasks
    })

@login_required
def showCreateProjectForm(request):
    return render(request,'projects/create.html')

@login_required
def storeProject(request):
    Project.objects.create(
        name=request.POST["name"],
        description=request.POST["description"],
        user=request.user
    )
    return redirect("projects.list")

@login_required
def showUpdateProjectForm(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request,'projects/update.html',{
        "project" : project
    })

@login_required
def updateProject(request,project_id):
    project = get_object_or_404(Project, id=project_id)
    project.name=request.POST["name"]
    project.description=request.POST["description"]
    
    project.save()
    return redirect('projects.list')

@login_required
def confirmDeleteProject(request,project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, "projects/delete.html", {
        "project": project
    })

@login_required
def destroyProject(request,project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return redirect('projects.list')

@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request,'tasks/list.html',{
        "tasks": tasks
    })

@login_required
def showCreateTaskForm(request):
    projects = Project.objects.filter(user=request.user)
    return render(request,'tasks/create.html',{
        "projects" : projects
    })

@login_required
def storeTask(request):
    Task.objects.create(
        title=request.POST['title'],
        description=request.POST['description'],
        project_id=request.POST['project_id'],
        user=request.user
    )

    return redirect('tasks.list')


@login_required
def showUpdateTaskForm(request, task_id):
    projects = Project.objects.filter(user=request.user)
    task = get_object_or_404(Task, id=task_id)
    return render(request,'tasks/update.html',{
        "projects" : projects,
        "task": task
    })

@login_required
def updateTask(request,task_id):
    task = get_object_or_404(Task, id=task_id)
    task.title=request.POST["title"]
    task.description=request.POST["description"]
    task.done=request.POST["done"]
    task.project_id=request.POST["project_id"]
    task.save()
    return redirect('tasks.list')

@login_required
def confirmDeleteTask(request,task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, "tasks/delete.html", {
        "task": task
    })

@login_required
def destroyTask(request,task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('tasks.list')

"""
Methods for users
"""

def showSignupForm(request):
    return render(request,"users/signup.html")

def signup(request):
    if (request.POST['password1'] == request.POST['password2']):
        try:
            user = User.objects.create_user(
                username=request.POST["username"],
                email=request.POST["email"],
                password=request.POST["password1"],
                first_name=request.POST["firstname"],
                last_name=request.POST["lastname"]
            )
            user.save()
            login(request,user)
            messages.add_message(request=request, level=messages.SUCCESS, message='User created succesfully')
            return redirect('tasks.list')
            
        except:
            return HttpResponse("The user already exists !!!")
    else:
        messages.add_message(request=request, level=messages.ERROR, message='Password fields no match')
        return redirect('signup.form')

def showLoginForm(request):
    return render(request,'users/login.html')

def startSession(request):
    user = authenticate(request=request, username=request.POST["username"],password=request.POST["password"])
    if(user is None):
        messages.add_message(request=request, level=messages.ERROR, message='Wrong credentials, try again')
        return redirect('login.form')
    else:
        login(request,user)
        return redirect('landing')

@login_required
def finishSession(request):
    logout(request)
    return redirect('landing')