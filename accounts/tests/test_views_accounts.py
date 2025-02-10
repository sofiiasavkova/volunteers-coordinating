import pytest
from django.urls import reverse
from accounts.models import Coordinator
from django.contrib.auth import get_user_model  # Додаємо імпорт для отримання правильної моделі користувача

@pytest.fixture
def create_user_and_coordinator():
    User = get_user_model()  # Використовуємо правильну модель користувача
    user = User.objects.create_user(username="testuser", password="password123")
    coordinator = Coordinator.objects.create(
        username="coordinator1",
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
    )
    return user, coordinator

@pytest.mark.django_db  # Додаємо маркер для доступу до бази даних
def test_coordinator_list_view_unauthenticated(create_user_and_coordinator, client):
    response = client.get(reverse("accounts:all_coordinators"))
    assert response.status_code == 302  # Перевіряємо перенаправлення на login
    assert reverse("login") in response.url

@pytest.mark.django_db  # Додаємо маркер для доступу до бази даних
def test_coordinator_create_view_invalid_data(create_user_and_coordinator, client):
    user, _ = create_user_and_coordinator
    client.login(username="testuser", password="password123")
    response = client.post(reverse("accounts:coordinator_create"), {
        "username": "",  # Неправильні дані
        "email": "not-an-email",
        "password": "short",
    })
    assert response.status_code == 200  # Форма відображається з помилками
    assert "This field is required." in response.content.decode()

@pytest.mark.django_db  # Додаємо маркер для доступу до бази даних
def test_coordinator_update_view_unauthenticated(create_user_and_coordinator, client):
    user, coordinator = create_user_and_coordinator
    response = client.get(reverse("accounts:coordinator_update", args=[coordinator.pk]))
    assert response.status_code == 302  # Перевіряємо перенаправлення на login
    assert reverse("login") in response.url

@pytest.mark.django_db  # Додаємо маркер для доступу до бази даних
def test_coordinator_delete_view_unauthenticated(create_user_and_coordinator, client):
    user, coordinator = create_user_and_coordinator
    response = client.post(reverse("accounts:coordinator_delete", args=[coordinator.pk]))
    assert response.status_code == 302  # Перевіряємо перенаправлення на login
    assert reverse("login") in response.url

def test_logout_view_get_unauthenticated(client):
    response = client.get(reverse("logout"))
    assert response.status_code == 200  # Логаут працює навіть для неавторизованих

@pytest.mark.django_db  # Додаємо маркер для доступу до бази даних
def test_register_view_invalid_data(client):
    response = client.post(reverse("accounts:register"), {
        "username": "newuser",
        "password1": "short",  # Пароль надто короткий
        "password2": "mismatch",  # Паролі не збігаються
    })
    assert response.status_code == 200  # Форма відображається з помилками
    assert "This password is too short." in response.content.decode()  # Заміна .text на .decode()
    assert "The two password fields didn’t match." in response.content.decode()  # Заміна .text на .decode()
