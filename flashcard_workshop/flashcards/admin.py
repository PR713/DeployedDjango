from django.contrib import admin

from flashcard_workshop.flashcards.models import Flashcard, FlashcardGroup

# Register your models here.


@admin.register(Flashcard)
class FlashcardAdmin(admin.ModelAdmin):
    pass


@admin.register(FlashcardGroup)
class FlashcardGroupAdmin(admin.ModelAdmin):
    pass
