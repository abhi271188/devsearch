from django.shortcuts import render
from .models import Profile, Skill

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
    context = {'profile' : profile, 'top_skills' : top_skills, 'other_skills' : other_skills}
    return render(request, 'users/profile.html', context)


