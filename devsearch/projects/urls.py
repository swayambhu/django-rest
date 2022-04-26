from django.urls import path
from .views import *
urlpatterns = [
    path('', projects, name="projects"),
    path('project/<slug:slug>/', single_project, name="single-project"),
    path('create-project/', create_project, name='create-project'),
    path('update-project/<str:pk>/',  update_project, name='update-project' ),
    path('delete-project/<str:pk>/',  delete_project, name='delete-project' ),
]
