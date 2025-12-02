# cards/services/fsrs.py
import math
from datetime import timedelta
from django.utils import timezone

def schedule_card(card, rating: int):
    """
    rating: 1=Again, 2=Hard, 3=Good, 4=Easy
    """
    now = timezone.now()

    # Сколько дней прошло с прошлого повторения
    if card.last_review:
        days_elapsed = (now - card.last_review).days
        days_elapsed = max(1, days_elapsed)
    else:
        days_elapsed = 1

    # === Первое повторение ===
    if card.reps == 0:
        intervals = [1, 10, 1440, 5760]  # 1 мин, 10 мин, 1 день, 4 дня
        if rating == 1:
            card.stability = 0.001  # 1 минута
        elif rating == 2:
            card.stability = 0.007  # 10 минут
        elif rating == 3:
            card.stability = 4.0
        else:  # Easy
            card.stability = 7.0
    else:
        # === Основной FSRS ===
        if rating == 1:  # Забыл
            card.stability = max(card.stability * 0.2, 0.5)
            card.difficulty = min(10.0, card.difficulty + 0.8)
            card.lapses += 1
        else:
            # Успешное повторение
            factor = {2: 1.5, 3: 2.2, 4: 3.5}.get(rating, 2.2)
            card.stability = card.stability * factor * (days_elapsed ** 0.1)
            card.difficulty = max(1.0, card.difficulty - 0.15)

    # Следующий показ
    next_days = max(1, round(card.stability))
    card.due = now + timedelta(days=next_days)
    card.last_review = now
    card.reps += 1
    card.save()

    return card