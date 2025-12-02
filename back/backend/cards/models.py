from django.db import models
from django.utils import timezone
from decks.models import Deck

class Card(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='cards')
    front = models.TextField()
    back = models.TextField()

    # FSRS поля
    stability = models.FloatField(default=4.0)      # сколько дней держится
    difficulty = models.FloatField(default=5.0)     # 1–10
    lapses = models.IntegerField(default=0)
    reps = models.IntegerField(default=0)

    due = models.DateTimeField(default=timezone.now)
    last_review = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.front[:50]}..."