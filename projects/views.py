from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

def projects(request):
    projects = Project.objects.all()
    context = {'projects' : projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    project = Project.objects.get(id = pk)
    tags = project.tag.all()
    context = {'project' : project, 'tags' : tags}
    return render(request, 'projects/project.html', context)

@login_required(login_url='login-register')
def addProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form' : form}
    return render(request, 'projects/add-project.html', context)

@login_required(login_url='login-register')
def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form' : form}
    return render(request, 'projects/add-project.html', context)

@login_required(login_url='login-register')
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'obj' : project}
    return render(request, 'projects/delete.html', context)



