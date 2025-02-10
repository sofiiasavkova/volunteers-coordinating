from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from .forms import ProjectForm, TaskForm
from .models import Project, Task, Volunteer


class HomeView(TemplateView):
    template_name = "coordination/home.html"


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "coordination/project_detail.html"
    context_object_name = "project"

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .select_related("coordinator")
            .prefetch_related("tasks")
        )


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "coordination/projects_list.html"
    context_object_name = "projects"


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "coordination/project_form.html"
    success_url = reverse_lazy("coordination:all_projects")


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = "coordination/project_update_form.html"
    context_object_name = "project"

    def get_success_url(self):
        return reverse_lazy("coordination:all_projects")


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = "coordination/project_confirm_delete.html"
    context_object_name = "project"
    success_url = reverse_lazy("coordination:all_projects")


class VolunteerListView(LoginRequiredMixin, ListView):
    model = Volunteer
    template_name = "coordination/volunteers_list.html"
    context_object_name = "volunteers"


class VolunteerCreateView(LoginRequiredMixin, CreateView):
    model = Volunteer
    fields = ["first_name", "last_name", "email"]
    template_name = "coordination/volunteer_form.html"
    success_url = reverse_lazy("coordination:all_volunteers")

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


class VolunteerUpdateView(LoginRequiredMixin, UpdateView):
    model = Volunteer
    fields = ["first_name", "last_name", "email"]
    template_name = "coordination/volunteer_update_form.html"
    context_object_name = "volunteer"
    success_url = reverse_lazy("coordination:all_volunteers")


class VolunteerDeleteView(LoginRequiredMixin, DeleteView):
    model = Volunteer
    template_name = "coordination/volunteer_confirm_delete.html"
    context_object_name = "volunteer"
    success_url = reverse_lazy("coordination:all_volunteers")


class VolunteerDetailView(LoginRequiredMixin, DetailView):
    model = Volunteer
    template_name = "coordination/volunteer_detail.html"
    context_object_name = "volunteer"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.prefetch_related("assigned_volunteers").filter(
            assigned_volunteers=self.object
        )
        return context


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "coordination/tasks_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.select_related("project").prefetch_related(
            "assigned_volunteers"
        )


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "coordination/task_detail.html"
    context_object_name = "task"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["assigned_volunteers"] = (
            self.object.assigned_volunteers.prefetch_related("assigned_tasks").all()
        )
        return context

    def get_queryset(self):
        return Task.objects.select_related("project").prefetch_related(
            "assigned_volunteers__assigned_tasks"
        )


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "coordination/task_form.html"

    def get_success_url(self):
        return reverse_lazy("coordination:all_tasks")

    def form_valid(self, form):
        response = super().form_valid(form)
        print(f"Assigned Volunteers: {self.object.assigned_volunteers.all()}")
        return response


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "coordination/task_update_form.html"

    def get_success_url(self):
        return reverse_lazy("coordination:all_tasks")


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "coordination/task_confirm_delete.html"
    success_url = reverse_lazy("coordination:all_tasks")
