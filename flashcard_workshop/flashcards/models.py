from django.db import models

from flashcard_workshop.accounts.models import CustomUser

# Create your models here.


class FlashcardGroup(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Flashcard(models.Model):
    group = models.ForeignKey(FlashcardGroup, on_delete=models.CASCADE, related_name="flashcards")
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question


class ScorePerFlashcard(models.Model):
    score = models.IntegerField(default=0)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    flashcard = models.ForeignKey(Flashcard, on_delete=models.CASCADE, related_name="scores")

    def __str__(self):
        return f"Score: {self.score} (User: {self.user.username})"
