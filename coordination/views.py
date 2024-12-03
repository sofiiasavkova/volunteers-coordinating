from django.shortcuts import render
from .models import Volunteer, Project, Task, Coordinator
from django.views.generic import ListView

def home(request):
    return render(request, 'coordination/home.html')

class CoordinatorListView(ListView):
    model = Coordinator
    template_name = 'coordination/coordinators_list.html'
    context_object_name = 'coordinators'


class ProjectListView(ListView):
    model = Project
    template_name = 'coordination/projects_list.html'
    context_object_name = 'projects'


class VolunteerListView(ListView):
    model = Volunteer
    template_name = 'coordination/volunteers_list.html'
    context_object_name = 'volunteers'


class TaskListView(ListView):
    model = Task
    template_name = 'coordination/tasks_list.html'
    context_object_name = 'tasks'

