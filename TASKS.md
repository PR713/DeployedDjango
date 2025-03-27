## Projekt fiszek

### Opis projektu

Głównym celem projektu jest stworzenie prostego projektu z API do nauki fiszek.

### Funkcjonalności

- API z możliwością tworzenia grup fiszek i zarządzania nimi
- API do nauki fiszek
- Endpoint do zapisywania postępów w nauce

### Technologie

- Python 3.12
- Django 5.1
- Django REST Framework
- PostgreSQL 17

### Uruchomienie

Szczegóły znajdziesz w pliku `README.md`. Ale w skrócie:
1. Utwórz fork naszego repozytorium i sklonuj go na swój komputer
2. Zainstaluj uv i docker compose (jeśli jeszcze nie korzystasz)
3. Uruchom komendę `make bootstrap-docker`
4. Uruchom komendę `make` i voila!

### Zadania do wykonania

1. Stwórz w projekcie aplikację `flashcards`
2. Stwórz modele na grupę fiszek i fiszki
3. Stwórz model do przechowywania postępów w nauce - będziemy przechowywać score w danej fiszcze per user
4. Zapoznaj się ze zaproponowaną przez nas i oczekiwaną przez front-end i mobilki specyfikacją API w pliku API_SCHEMA.md
5. Przy pomocy `ModelViewSet` stwórz API do zarządzania grupami fiszek
6. Przetestuj działanie API za pomocą Swaggera, który jest dostępny pod adresem `http://localhost:8000/api/schema/swagger-ui/`
7. Zapoznaj się z doinstalowaną biblioteką `drf-nested-routers`, a następnie stwórz API do zarządzania fiszkami
8. Przy pomocy `extra action` w DRF, stwórz endpoint do pobierania 10 fiszek do nauki
9. Przy pomocy `extra action` w DRF, stwórz endpointy do zapisywania postępów w nauce
10. Stwórz testy do API, używając bibliotekę `pytest`

### Bonus

Jeśli starczy Ci czasu, spróbuj zaimplementować dodatkowe funkcjonalności:

1. Rozbuduj logikę zwracającą fiszki do nauki, tak aby były uwzględniane postępy w nauce, możesz zapoznać się z techniką `spaced repetition` i ją zaimplementować
2. Dodaj autentykację do API - możesz wykorzystać bibliotekę `djangorestframework-simplejwt`
