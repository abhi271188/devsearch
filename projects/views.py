from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Project, Reviews, Tags
from .forms import ProjectForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from users.models import Profile
from .utils import paginateProjects, searchProjects
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def projects(request):
    search_query, projects = searchProjects(request)
    custom_range, projects = paginateProjects(request, projects, 3)

    context = {'projects' : projects, 'search_query' : search_query,
     'custom_range' : custom_range}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    project = Project.objects.get(id = pk)
    tags = project.tag.all()
    form = ReviewForm()
    reviews = Reviews.objects.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = project
        review.owner = request.user.profile
        form.save()
        project.getVoteCount
        return redirect('project', pk=project.id)

    context = {'project' : project, 'tags' : tags, 'form' : form, 'reviews' : reviews}
    return render(request, 'projects/project.html', context)

@login_required(login_url='login-register')
def addProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            form.save()
            return redirect('account')

    context = {'form' : form}
    return render(request, 'projects/add-project.html', context)

@login_required(login_url='login-register')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form' : form}
    return render(request, 'projects/add-project.html', context)

@login_required(login_url='login-register')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('account')
    context = {'obj' : project}
    return render(request, 'delete.html', context)

    



