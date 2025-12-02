from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from cards.models import Card
from cards.services.fsrs import schedule_card

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def due_today(request):
    cards = Card.objects.filter(
        deck__owner=request.user,
        due__lte=timezone.now()
    ).order_by('due')

    data = [{
        "id": c.id,
        "front": c.front,
        "back": c.back,
        "deck": c.deck.title
    } for c in cards]

    return Response({"count": len(data), "cards": data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_card(request, card_id):
    card = Card.objects.get(id=card_id, deck__owner=request.user)
    rating = int(request.data["rating"])
    schedule_card(card, rating)

    return Response({
        "message": "Ок!",
        "next_in_days": (card.due - timezone.now()).days + 1,
        "stability": round(card.stability, 1)
    })