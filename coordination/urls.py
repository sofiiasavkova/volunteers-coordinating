from django.urls import path, include
from . import views
from .views import (
    VolunteerListView,
    VolunteerDetailView,
    VolunteerCreateView,
    VolunteerUpdateView,
    VolunteerDeleteView,
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    CoordinatorListView,
    CoordinatorCreateView,
    CoordinatorDetailView,
    CoordinatorUpdateView,
    CoordinatorDeleteView,
    custom_logout_view,
)

app_name = 'coordination'

urlpatterns = [
    path('', views.home, name='home'),
    path('volunteers/', VolunteerListView.as_view(), name='all_volunteers'),
    path('volunteers/<int:pk>/', VolunteerDetailView.as_view(), name='volunteer-detail'),
    path('volunteers/create/', VolunteerCreateView.as_view(), name='volunteer-create'),
    path('volunteers/<int:pk>/update/', VolunteerUpdateView.as_view(), name='volunteer-update'),
    path('volunteers/<int:pk>/delete/', VolunteerDeleteView.as_view(), name='volunteer-delete'),
    path('projects/', ProjectListView.as_view(), name='all_projects'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('projects/create/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
    path('tasks/', TaskListView.as_view(), name='all_tasks'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('coordinators/', CoordinatorListView.as_view(), name='all_coordinators'),
    path('coordinators/create/', CoordinatorCreateView.as_view(), name='coordinator-create'),
    path('coordinators/<int:pk>/update/', CoordinatorUpdateView.as_view(), name='coordinator-update'),
    path('coordinators/<int:pk>/delete/', CoordinatorDeleteView.as_view(), name='coordinator-delete'),
    path('coordinators/<int:pk>/', CoordinatorDetailView.as_view(), name='coordinator-detail'),
    path('register/', views.register, name='register'),
    path("logout/", custom_logout_view, name="logout"),

    ]
