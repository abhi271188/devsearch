from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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

def paginateProjects(request, projects, result):
    page = request.GET.get('page')
    result = 3  
    paginator = Paginator(projects, result)
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)
    
    left_index = (int(page) - 4)
    if left_index < 1:
        left_index = 1
    
    right_index = (int(page) + 5)
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    return custom_range, projects