from unittest import result
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from projects.utils import searchProjects, paginateProjects
from .models import Project
from .forms import ProjectForm, ReviewForm
from django.contrib import messages
# Create your views here.


def projects(request):
    projects, search_query = searchProjects(request)
    custom_range, projects = paginateProjects(request, projects, 6)
    context = {
        "projects": projects,
        "search_query": search_query,
        "custom_range": custom_range,
    }
    return render(request, "projects/projects.html", context)


def single_project(request, slug=None):
    projectObj = get_object_or_404(Project, pk=slug)
    form = ReviewForm()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()
        
        # Update project vote count
        
        projectObj.getVoteCount
        
        messages.success(request, 'Your review was successfully submitted')
        return redirect('single-project', slug=projectObj.id)
        
    context = {
        "project": projectObj,
        "form": form
    }
    return render(request, 'projects/single-project.html', context)

@login_required(login_url='login')
def create_project(request):
    profile = request.user.profile
    
    create_project_form = ProjectForm()
    
    if request.POST:
        create_project_form = ProjectForm(request.POST, request.FILES)
        if create_project_form.is_valid():
            project = create_project_form.save(commit = False)
            project.owner = profile
            project.save()
            return redirect('account')
    context = {
        "form": create_project_form
    }
    return render(request, "projects/project_form.html", context)


@login_required(login_url='login')
def update_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.POST:
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {
        "form": form
    }
    return render(request, "projects/project_form.html", context)


@login_required(login_url='login')
def delete_project(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    
    if request.POST:
        project.delete()
        return redirect('projects')
    
    context = {
        "object": project    
    }
    return render(request, 'delete_template.html', context)