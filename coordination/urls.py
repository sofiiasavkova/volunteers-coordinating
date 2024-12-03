from django.urls import path
from . import views
from .views import (
    VolunteerListView,
    ProjectListView,
    TaskListView,
    CoordinatorListView
)

urlpatterns = [
    path('', views.home, name='home'),
    path('volunteers/', VolunteerListView.as_view(), name='all_volunteers'),
    path('projects/', ProjectListView.as_view(), name='all_projects'),
    path('tasks/', TaskListView.as_view(), name='all_tasks'),
    path('coordinators/', CoordinatorListView.as_view(), name='all_coordinators'),
]