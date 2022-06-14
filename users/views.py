from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Profile, Skill
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

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

def userLogin(request):
    if request.method == 'POST':
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
    context = {}
    return render(request, 'users/login_register.html', context)


