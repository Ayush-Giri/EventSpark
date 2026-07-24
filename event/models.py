from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

# Create your models here.

class StatusChoices(models.TextChoices):
    DRAFT = ("draft", "draft")
    published = ("publisehd", "published")
    cancelled = ("cancelled", "cancelled")
    completed = ("completed", "completed")

class Event(models.Model):
    organiser = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    cover_image = models.ImageField(upload_to="event_cover_image")
    venue_name = models.CharField(max_length=100)
    venue_address = models.TextField()
    city = models.CharField(max_length=50)
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    status = models.CharField(choices=StatusChoices.choices, max_length=20)
    is_online = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.organiser.username} | {self.city} | {self.title}"

    def save(self, *args, **kwargs):
        if self.is_online:
            if not self.venue_address.startswith("www"):
                raise ValidationError("venue address link not correct")
            super().save(*args, **kwargs)
        super.save(*args, **kwargs)

