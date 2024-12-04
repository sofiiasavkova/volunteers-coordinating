from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ProjectForm
from .models import Volunteer, Project, Task, Coordinator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth import logout
from django.urls import reverse_lazy

def home(request):
    return render(request, 'coordination/home.html')

class CoordinatorListView(ListView):
    model = Coordinator
    template_name = 'coordination/coordinators_list.html'
    context_object_name = 'coordinators'


class CoordinatorCreateView(LoginRequiredMixin, CreateView):
    model = Coordinator
    fields = ['username', 'first_name', 'last_name', 'email', 'password']
    template_name = 'coordination/coordinator_form.html'
    success_url = reverse_lazy('coordination:all_coordinators')

    def form_valid(self, form):
        coordinator = form.save(commit=False)
        coordinator.set_password(form.cleaned_data['password'])
        coordinator.save()
        return super().form_valid(form)


class CoordinatorUpdateView(LoginRequiredMixin, UpdateView):
    model = Coordinator
    fields = ['username', 'first_name', 'last_name', 'email']
    template_name = 'coordination/coordinator_update_form.html'
    context_object_name = 'coordinator'
    success_url = reverse_lazy('coordination:all_coordinators')


class CoordinatorDeleteView(LoginRequiredMixin, DeleteView):
    model = Coordinator
    template_name = 'coordination/coordinator_confirm_delete.html'
    context_object_name = 'coordinator'
    success_url = reverse_lazy('coordination:all_coordinators')


class CoordinatorDetailView(LoginRequiredMixin, DetailView):
    model = Coordinator
    template_name = 'coordination/coordinator_detail.html'
    context_object_name = 'coordinator'


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'coordination/project_detail.html'
    context_object_name = 'project'


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


class VolunteerCreateView(LoginRequiredMixin, CreateView):
    model = Volunteer
    fields = ['first_name', 'last_name', 'email', 'assigned_tasks']
    template_name = 'coordination/volunteer_form.html'
    success_url = reverse_lazy('coordination:all_volunteers')


class VolunteerUpdateView(LoginRequiredMixin, UpdateView):
    model = Volunteer
    fields = ['first_name', 'last_name', 'email', 'assigned_tasks']
    template_name = 'coordination/volunteer_update_form.html'
    context_object_name = 'volunteer'
    success_url = reverse_lazy('coordination:all_volunteers')


class VolunteerDeleteView(LoginRequiredMixin, DeleteView):
    model = Volunteer
    template_name = 'coordination/volunteer_confirm_delete.html'
    context_object_name = 'volunteer'
    success_url = reverse_lazy('coordination:all_volunteers')


class VolunteerDetailView(LoginRequiredMixin, DetailView):
    model = Volunteer
    template_name = 'coordination/volunteer_detail.html'
    context_object_name = 'volunteer'


class TaskListView(ListView):
    model = Task
    template_name = 'coordination/tasks_list.html'
    context_object_name = 'tasks'


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'coordination/task_detail.html'
    context_object_name = 'task'


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'status', 'deadline', 'assigned_volunteers', 'project', 'category']
    template_name = 'coordination/task_form.html'
    success_url = reverse_lazy('coordination:all_tasks')


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'status', 'deadline', 'assigned_volunteers', 'project', 'category']
    template_name = 'coordination/task_update_form.html'
    success_url = reverse_lazy('coordination:all_tasks')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'coordination/task_confirm_delete.html'
    success_url = reverse_lazy('coordination:all_tasks')

def custom_logout_view(request):
    logout(request)
    return render(request, "registration/logged_out.html")
