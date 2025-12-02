from django.db import models
from django.contrib.auth.models import User

class Deck(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=7, default="#3B82F6")  # hex
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title