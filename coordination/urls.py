from django.urls import path, include
from . import views
from .views import (
    VolunteerListView,
    ProjectListView,
    ProjectCreateView,
    TaskListView,
    CoordinatorListView,
    custom_logout_view,
    ProjectUpdateView,
    ProjectDeleteView,
)

app_name = 'coordination'

urlpatterns = [
    path('', views.home, name='home'),
    path('volunteers/', VolunteerListView.as_view(), name='all_volunteers'),
    path('projects/', ProjectListView.as_view(), name='all_projects'),
    path('projects/create/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
    path('tasks/', TaskListView.as_view(), name='all_tasks'),
    path('coordinators/', CoordinatorListView.as_view(), name='all_coordinators'),
    path("logout/", custom_logout_view, name="logout"),
    ]
