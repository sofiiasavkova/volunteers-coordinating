from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import Coordinator

@admin.register(Coordinator)
class CoordinatorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("email", "first_name", "last_name")
    fieldsets = (*UserAdmin.fieldsets,)