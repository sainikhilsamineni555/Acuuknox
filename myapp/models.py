from django.contrib.auth.models import User
from django.db import models

# Profile model related to the User model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
