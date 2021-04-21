from project.models import Project
from django.shortcuts import render

# Create your views here.
def list(request):
    projects = Project.objects.all()
    return render(request, 'project/list.html', {'projects':projects})

def detail(request):
    return render(request, 'project/project-detail.html', {})
