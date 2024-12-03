from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ProjectForm
from .models import Volunteer, Project, Task, Coordinator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth import logout
from django.urls import reverse_lazy

def home(request):
    return render(request, 'coordination/home.html')

class CoordinatorListView(ListView):
    model = Coordinator
    template_name = 'coordination/coordinators_list.html'
    context_object_name = 'coordinators'


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'coordination/projects_list.html'
    context_object_name = 'projects'

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'coordination/project_form.html'
    success_url = reverse_lazy('coordination:all_projects')


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'coordination/project_update_form.html'
    context_object_name = 'project'

    def get_success_url(self):
        return reverse_lazy('coordination:all_projects')


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'coordination/project_confirm_delete.html'
    context_object_name = 'project'
    success_url = reverse_lazy('coordination:all_projects')

class VolunteerListView(ListView):
    model = Volunteer
    template_name = 'coordination/volunteers_list.html'
    context_object_name = 'volunteers'


class TaskListView(ListView):
    model = Task
    template_name = 'coordination/tasks_list.html'
    context_object_name = 'tasks'

def custom_logout_view(request):
    logout(request)
    return render(request, "registration/logged_out.html")
