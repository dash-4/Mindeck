from django.urls import path
from .views import due_today, review_card

urlpatterns = [
    path('cards/due/', due_today),
    path('cards/<int:card_id>/review/', review_card),
]