from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class RoleChoices(models.TextChoices):
    ORGANISER = ("organiser", "Organiser")
    ATTENDEE = ("attendee", "Attendee")


class CustomUser(AbstractUser):
    # just extending the base user model and defining our own custom fields is not enough
    # we have to register it as well
    role = models.CharField(max_length=20, choices=RoleChoices.choices)
    phone_number = models.CharField(max_length=15)
    profile_photo = models.ImageField(upload_to="profile_image")
    created_at = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return f"{self.username} | {self.phone_number} | {self.role}"