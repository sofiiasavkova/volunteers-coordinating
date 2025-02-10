from django.contrib.auth.forms import UserCreationForm

from .models import Coordinator

class CoordinatorRegistrationForm(UserCreationForm):
    class Meta:
        model = Coordinator
        fields = ["username", "email", "first_name", "last_name"]
