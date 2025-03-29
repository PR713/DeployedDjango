from django.db.models import Q
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from flashcard_workshop.accounts.models import CustomUser
from flashcard_workshop.flashcards.models import Flashcard, FlashcardGroup, ScorePerFlashcard
from flashcard_workshop.flashcards.serializers import (
    FlashcardGroupSerializer,
    FlashcardSerializer,
    MarkFlashcardSerializer,
    ScorePerFlashcardSerializer,
)

# Create your views here.


class FlashcardViewSet(viewsets.ModelViewSet):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer

    def get_queryset(self):
        return Flashcard.objects.filter(group=self.kwargs["flash_card_set_pk"])

    @action(detail=True, methods=["post"])
    def mark_as_known(self, request, flash_card_set_pk=None, pk=None):
        return self._handle_marking(request, flash_card_set_pk, pk, status="known")

    @action(detail=True, methods=["post"])
    def mark_as_unknown(self, request, flash_card_set_pk=None, pk=None):
        return self._handle_marking(request, flash_card_set_pk, pk, status="unknown")

    def _handle_marking(self, request, flash_card_set_pk, pk, status):
        serializer = MarkFlashcardSerializer(data=request.data)

        flashcard = get_object_or_404(Flashcard, pk=pk)  # pk to id fiszki

        try:
            user = get_object_or_404(CustomUser, name=serializer.validated_data["username"])
        except KeyError:
            return Response({"error": "Field 'user' is required"})

        if flashcard.group_id != int(flash_card_set_pk):
            return Response({"error": "Flashcard does not belong to this set"}, status=status.HTTP_400_BAD_REQUEST)

        ScorePerFlashcard.objects.update_or_create(user=user, flashcard=flashcard, defaults={"status": status})

        return Response({"status": f"marked as {status}"}, status=status.HTTP_200_OK)


class FlashcardGroupViewSet(viewsets.ModelViewSet):
    queryset = FlashcardGroup.objects.all()
    serializer_class = FlashcardGroupSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="username", type=str, location=OpenApiParameter.QUERY, description="username", required=True
            )
        ]
    )
    @action(detail=True, methods=["get"])
    def learn(self, request, pk=None):
        username = request.query_params.get("username")

        if not username:
            return Response({"error": "Parameter 'username' is required"}, status=status.HTTP_400_BAD_REQUEST)

        user = get_object_or_404(CustomUser, username=username)
        group = self.get_object()

        unknown_flashcards = (
            Flashcard.objects.filter(group=group)
            .filter(  # __ inner join lub atrybut modelu
                scores__user=user, scores__score=0
            )
            .order_by("?")[:10]
        )

        serializer = FlashcardSerializer(list(unknown_flashcards), many=True)
        return Response(serializer.data)


class ScorePerFlashcardViewSet(viewsets.ModelViewSet):
    queryset = ScorePerFlashcard.objects.all()
    serializer_class = ScorePerFlashcardSerializer
