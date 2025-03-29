from rest_framework import routers
from rest_framework_nested import routers as nested_routers

from flashcard_workshop.flashcards.views import FlashcardGroupViewSet, FlashcardViewSet, ScorePerFlashcardViewSet

router = routers.DefaultRouter()
router.register(r"flash-cards", FlashcardViewSet)

router.register(r"flash-card-sets", FlashcardGroupViewSet)

groups_router = nested_routers.NestedSimpleRouter(router, r"flash-card-sets", lookup="flash_card_set_pk")
groups_router.register(r"flash-cards", FlashcardViewSet)


learn_router = nested_routers.NestedSimpleRouter(router, r"flash-card-sets", lookup="id")
learn_router.register(r"learn", FlashcardViewSet)

router.register(r"score", ScorePerFlashcardViewSet)
