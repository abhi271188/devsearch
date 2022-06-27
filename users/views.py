from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Profile, Skill, Message
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm
from .forms import customUserCreationForm, ProfileForm, SkillForm
from django.db.models import Q
from .utils import paginateProfiles, searchProfiles
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def userLogin(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        #print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username = username)
        except:
            print('Username does not exist')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            print('Username/Password does not exist')
    context = {'page' : page}
    return render(request, 'users/login_register.html', context)

def userLogout(request):
    logout(request)
    return redirect('profiles')

def userRegister(request):
    page = 'register'
    form = customUserCreationForm()
    if request.method == 'POST':
        form = customUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            form.save()
            login(request, user)
            return redirect('update-profile')
    context = {'page' : page, 'form' : form}
    return render(request, 'users/login_register.html', context)

def Profiles(request):
    skills, profiles, search_query = searchProfiles(request)
    custom_range, profiles = paginateProfiles(request, profiles, 2)

    context = {'profiles' : profiles, 'skills' : skills, 'search_query' : search_query, 
    'custom_range' : custom_range}
    return render(request, 'users/profiles.html', context)

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    # the below code removes those skills that doesn't have any description in a spcific profile.
    top_skills = profile.skill_set.exclude(description__exact = '')
    # the below code filter those skills that doesn't have any description in a specific profile.
    other_skills = profile.skill_set.filter(description = '')
    projects = profile.project_set.all()
    context = {'profile' : profile, 'top_skills' : top_skills, 'other_skills' : other_skills, 
    'projects' : projects}
    return render(request, 'users/profile.html', context)

@login_required(login_url='login-register')
def userAccount(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    context = {'profile' : profile, 'skills' : skills, 'projects' : projects}
    return render(request, 'users/account.html', context)

@login_required(login_url='login-register')
def updateProfile(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form' : form}
    return render(request, 'users/profile_form.html', context)

@login_required(login_url='login-register')
def addSkill(request):
    profile = request.user.profile
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)   
            skill.owner = profile       
            form.save()
            return redirect('account')

    context = {'form' : form}
    return render(request, 'users/skill_form.html', context)

@login_required(login_url='login-register')
def updateSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance = skill)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance = skill)
        if form.is_valid():
            form.save()
            return redirect('account')
            
    context = {'form' : form}
    return render(request, 'users/skill_form.html', context)

@login_required(login_url='login-register')
def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == 'POST':
        skill.delete()
        return redirect('account')
        
    context = {'obj' : skill}
    return render(request, 'delete.html', context)

@login_required(login_url='login-register')
def userInbox(request):
    profile = request.user.profile
    messageRequests = profile.messages.all()
    messageCount = messageRequests.filter(is_read = False).count()
    context = {'messageRequests' : messageRequests, 'messageCount' : messageCount}
    return render(request, 'users/inbox.html', context)
    

