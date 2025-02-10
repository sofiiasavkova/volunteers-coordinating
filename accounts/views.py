from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import CoordinatorRegistrationForm
from django.views.generic.edit import FormView

from accounts.models import Coordinator


class CoordinatorListView(LoginRequiredMixin, ListView):
    model = Coordinator
    template_name = "coordination/coordinators_list.html"
    context_object_name = "coordinators"


class CoordinatorCreateView(LoginRequiredMixin, CreateView):
    model = Coordinator
    fields = ["username", "first_name", "last_name", "email", "password"]
    template_name = "coordination/coordinator_form.html"
    success_url = reverse_lazy("accounts:all_coordinators")

    def form_valid(self, form):
        coordinator = form.save(commit=False)
        coordinator.set_password(form.cleaned_data["password"])
        coordinator.save()
        return super().form_valid(form)


class CoordinatorUpdateView(LoginRequiredMixin, UpdateView):
    model = Coordinator
    fields = ["username", "first_name", "last_name", "email"]
    template_name = "coordination/coordinator_update_form.html"
    context_object_name = "coordinator"
    success_url = reverse_lazy("accounts:all_coordinators")


class CoordinatorDeleteView(LoginRequiredMixin, DeleteView):
    model = Coordinator
    template_name = "coordination/coordinator_confirm_delete.html"
    context_object_name = "coordinator"
    success_url = reverse_lazy("accounts:all_coordinators")


class CoordinatorDetailView(LoginRequiredMixin, DetailView):
    model = Coordinator
    template_name = "coordination/coordinator_detail.html"
    context_object_name = "coordinator"


class LogoutView(View):
    template_name = "registration/logged_out.html"

    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        logout(request)
        return render(request, self.template_name)


class RegisterView(FormView):
    template_name = "registration/register.html"
    form_class = CoordinatorRegistrationForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)