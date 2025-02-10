from django.db import models
from django.contrib.auth.models import AbstractUser


class Coordinator(AbstractUser):
    class Meta:
        verbose_name = "Coordinator"
        verbose_name_plural = "Coordinators"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"
