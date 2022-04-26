from django.forms import ModelForm, forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ['vote_total', 'vote_ratio']
        