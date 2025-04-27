from django.db import models

from users.models import User

# Create your models here.

class Task(models.Model):
    class TaskStatus(models.TextChoices):
        NOTSTARTED = "NS", "Not Started"
        ONGOING = "OG", "Ongoing"
        COMPLETED = "CD", "Completed"

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=2, choices=TaskStatus)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=False)

    def __str__(self):
        return self.title