from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Profile, Skill
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm
from .forms import customUserCreationForm


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
            return redirect('profiles')
    context = {'page' : page, 'form' : form}
    return render(request, 'users/login_register.html', context)

def Profiles(request):
    profiles = Profile.objects.all()
    skills = Skill.objects.all()
    context = {'profiles' : profiles, 'skills' : skills}
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

def userAccount(request):
    context = {}
    return render(request, 'users/account.html', context)




