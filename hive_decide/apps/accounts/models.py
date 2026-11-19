from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Project user model.

    Created before the first migration so that email login and the display
    name can be added later without swapping the user model.
    """
