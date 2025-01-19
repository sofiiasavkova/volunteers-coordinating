from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Coordinator, Project, Task, Volunteer


class TaskForm(forms.ModelForm):
    assigned_volunteers = forms.ModelMultipleChoiceField(
        queryset=Volunteer.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Assigned Volunteers",
    )

    class Meta:
        model = Task
        fields = [
            "title",
            "status",
            "deadline",
            "project",
            "category",
            "assigned_volunteers",
        ]


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description", "start_date", "end_date", "coordinator"]


class CoordinatorRegistrationForm(UserCreationForm):
    class Meta:
        model = Coordinator
        fields = ["username", "email", "first_name", "last_name"]
