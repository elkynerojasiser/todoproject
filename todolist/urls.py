
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name="landing"),
    path('projects/',views.projects, name="projects.list"),
    path('project-detail/<int:project_id>/',views.detailOfProject, name="projects.detail"),
    path('project-create/',views.showCreateProjectForm, name="projects.create"),
    path('project-store/',views.storeProject, name="projects.store"),
    path('project-edit/<int:project_id>/',views.showUpdateProjectForm, name="projects.edit"),
    path('project-update/<int:project_id>/',views.updateProject, name="projects.update"),
    path('project-delete/<int:project_id>/',views.confirmDeleteProject, name="projects.delete"),
    path('projects-destroy/<int:project_id>/',views.destroyProject, name="projects.destroy"),
    path('tasks/',views.tasks, name="tasks.list"),
    path('task-create/',views.showCreateTaskForm, name="tasks.create"),
    path('task-store/',views.storeTask, name="tasks.store"),
    path('task-edit/<int:task_id>/',views.showUpdateTaskForm, name="tasks.edit"),
    path('task-update/<int:task_id>/',views.updateTask, name="tasks.update"),
    path('task-delete/<int:task_id>/',views.confirmDeleteTask, name="tasks.delete"),
    path('task-destroy/<int:task_id>/',views.destroyTask, name="tasks.destroy"),
    path('signup-form/',views.showSignupForm,name="signup.form"),
    path('signup/',views.signup, name="signup.store"),
    path('login-form/',views.showLoginForm, name="login.form"),
    path('login/',views.startSession, name="login.store"),
    path('logout/',views.finishSession, name="logout")
]
