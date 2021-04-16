from django.shortcuts import render

# Create your views here.
def list(request):
    return render(request, 'project/list.html', {})

def detail(request):
    return render(request, 'project/project-detail.html', {})
