from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm
# Create your views here.


def projects(request):
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "projects/projects.html", context)


def single_project(request, slug=None):
    project = get_object_or_404(Project, pk=slug)
    context = {
        "project": project
    }
    return render(request, 'projects/single-project.html', context)


def create_project(request):
    create_project_form = ProjectForm()
    
    if request.POST:
        create_project_form = ProjectForm(request.POST)
        if create_project_form.is_valid():
            create_project_form.save()
            return redirect('projects')
    context = {
        "form": create_project_form
    }
    return render(request, "projects/project_form.html", context)


def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.POST:
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {
        "form": form
    }
    return render(request, "projects/project_form.html", context)

def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if request.POST:
        project.delete()
        return redirect('projects')
    
    context = {
        "object": project    
    }
    return render(request, 'projects/delete_template.html', context)