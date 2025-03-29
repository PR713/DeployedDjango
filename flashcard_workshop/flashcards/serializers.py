from rest_framework import serializers

from flashcard_workshop.accounts.models import CustomUser
from flashcard_workshop.flashcards.models import Flashcard, FlashcardGroup, ScorePerFlashcard


class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = "__all__"


class FlashcardGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashcardGroup
        fields = "__all__"


class ScorePerFlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScorePerFlashcard
        fields = "__all__"


class MarkFlashcardSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100, required=True)

    def validate_username(self, value):
        if not CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("User with that username does not exist")
        return value
