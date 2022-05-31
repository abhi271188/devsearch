from django.shortcuts import render

def Profiles(request):
    context = {}
    return render(request, 'users/profiles.html', context)
