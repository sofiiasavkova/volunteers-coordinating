from django.urls import path

from accounts.views import (CoordinatorCreateView, CoordinatorDeleteView,
                    CoordinatorDetailView, CoordinatorListView,
                    CoordinatorUpdateView, LogoutView, RegisterView)

app_name = "accounts"

urlpatterns = [
    path("coordinators/", CoordinatorListView.as_view(), name="all_coordinators"),
    path(
        "coordinators/create/",
        CoordinatorCreateView.as_view(),
        name="coordinator-create",
    ),
    path(
        "coordinators/<int:pk>/update/",
        CoordinatorUpdateView.as_view(),
        name="coordinator-update",
    ),
    path(
        "coordinators/<int:pk>/delete/",
        CoordinatorDeleteView.as_view(),
        name="coordinator-delete",
    ),
    path(
        "coordinators/<int:pk>/",
        CoordinatorDetailView.as_view(),
        name="coordinator-detail",
    ),
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
]