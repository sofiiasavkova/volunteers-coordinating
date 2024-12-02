from django.contrib.auth.models import AbstractUser
from django.db import models


class Coordinator(AbstractUser):
    class Meta:
        verbose_name = 'Coordinator'
        verbose_name_plural = 'Coordinators'

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    coordinator = models.ForeignKey(
        Coordinator,
        on_delete=models.CASCADE,
        related_name="projects_coordinators"
    )

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=255)
    status = models.CharField(
        max_length=50,
        choices=[
            ("Pending", "Pending"),
            ("In Progress", "In Progress"),
            ("Completed", "Completed")
        ],
        default="Pending",
    )
    deadline = models.DateField()
    assigned_volunteers = models.ManyToManyField(
        "Volunteer",
        related_name="tasks",
        blank=True,
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="tasks"
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name="tasks",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return f"{self.title} ({self.status})"


class Volunteer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    assigned_tasks = models.ManyToManyField(
        Task,
        related_name="volunteers",
        blank=True
    )

    class Meta:
        verbose_name = 'Volunteer'
        verbose_name_plural = 'Volunteers'

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
