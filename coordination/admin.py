from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Coordinator, Project, Task, Volunteer, Category


@admin.register(Coordinator)
class CoordinatorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("email", "first_name", "last_name")
    fieldsets = (
        *UserAdmin.fieldsets,
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "start_date", "end_date", "coordinator")
    search_fields = ("name",)
    list_filter = ("start_date", "end_date")
    autocomplete_fields = ("coordinator",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "deadline", "project", "category")
    search_fields = ("title",)
    list_filter = ("status", "deadline", "category")
    autocomplete_fields = ("project", "category")
    filter_horizontal = ("assigned_volunteers",)


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")
    filter_horizontal = ("assigned_tasks",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)
