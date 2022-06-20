from django.db.models import Q
from users.models import Profile
from .models import Tags, Project

def searchProjects(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    profile = Profile.objects.filter(name__icontains = search_query)
    tags = Tags.objects.filter(name__icontains = search_query)

    projects = Project.objects.distinct().filter(
        Q(title__icontains = search_query) |
        Q(owner__in = profile) |
        Q(tag__in = tags)
    )

    return search_query, projects