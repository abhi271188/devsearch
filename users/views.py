from django.shortcuts import render
from .models import Profile, Skill

def Profiles(request):
    profiles = Profile.objects.all()
    skills = Skill.objects.all()
    context = {'profiles' : profiles, 'skills' : skills}
    return render(request, 'users/profiles.html', context)

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile' : profile}
    return render(request, 'users/profile.html', context)


