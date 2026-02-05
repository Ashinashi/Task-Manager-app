from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=20, choices=[('Low','Low'),('Medium','Medium'),('High','High')], default='Medium')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

