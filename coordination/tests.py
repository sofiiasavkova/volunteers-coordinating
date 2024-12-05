from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Project, Task
from datetime import datetime, timedelta


class ProjectTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@example.com",
            password="password123"
        )
        self.project = Project.objects.create(
            name="Test Project",
            description="A project for testing",
            coordinator=self.user,
            start_date=datetime.now().date(),
            end_date=(datetime.now() + timedelta(days=30)).date()
        )

    def test_project_creation(self):
        self.assertEqual(self.project.name, "Test Project")
        self.assertEqual(self.project.description, "A project for testing")
        self.assertIsNotNone(self.project.start_date)

    def test_project_detail_view(self):
        self.client.login(username="testuser", password="password123")

        url = reverse('coordination:project-detail', args=[self.project.id])
        response = self.client.get(url)
        self.assertEqual(
            response.status_code,
            200,
            f"Got {response.status_code} instead of 200"
        )
        self.assertContains(response, "Test Project")

    def test_task_assigned_to_project(self):
        task = Task.objects.create(
            title="Test Task",
            status="Pending",
            deadline=(datetime.now() + timedelta(days=10)).date(),
            project=self.project
        )
        self.assertIn(task, self.project.tasks.all())
