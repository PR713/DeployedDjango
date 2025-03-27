# Dokumentacja API FlashCard Workshop

## Przegląd
API FlashCard Workshop jest przeznaczone do zarządzania zestawami fiszek oraz pojedynczymi fiszkami, umożliwiając użytkownikom ich tworzenie, pobieranie, aktualizowanie i usuwanie. API obejmuje również funkcje oznaczania fiszek jako znane/nieznane oraz pobierania fiszek do nauki.

### Bazowy URL
API powinno być dostępne pod adresem `http://localhost:8000/api/`.

---

## Endpointy

### Zestawy fiszek
#### Pobierz wszystkie zestawy fiszek
**GET** `/flash-card-sets/`

**Odpowiedź:**
```json
[
  {
    "id": 1,
    "title": "Przykładowy zestaw",
    "flashcardCount": 0
  }
]
```

#### Utwórz zestaw fiszek
**POST** `/flash-card-sets/`

**Treść żądania:**
```json
{
  "title": "Nowy zestaw"
}
```

**Odpowiedź:**
```json
{
  "id": 1,
  "title": "Nowy zestaw",
  "flashcardCount": 0
}
```

---

### Fiszki
#### Pobierz wszystkie fiszki z zestawu
**GET** `/flash-card-sets/{flash_card_set_pk}/flash-cards/`

**Odpowiedź:**
```json
[
  {
    "id": 1,
    "question": "Co to jest API?",
    "answer": "Interfejs programowania aplikacji",
    "flashcard_set": 1
  }
]
```

#### Utwórz fiszkę
**POST** `/flash-card-sets/{flash_card_set_pk}/flash-cards/`

**Treść żądania:**
```json
{
  "question": "Co to jest REST?",
  "answer": "Representational State Transfer",
  "flashcard_set": 1
}
```

**Odpowiedź:**
```json
{
  "id": 2,
  "question": "Co to jest REST?",
  "answer": "Representational State Transfer",
  "flashcard_set": 1
}
```

#### Pobierz pojedynczą fiszkę
**GET** `/flash-card-sets/{flash_card_set_pk}/flash-cards/{id}/`

**Odpowiedź:**
```json
{
  "id": 1,
  "question": "Co to jest API?",
  "answer": "Interfejs programowania aplikacji",
  "flashcard_set": 1
}
```

#### Zaktualizuj fiszkę
**PUT** `/flash-card-sets/{flash_card_set_pk}/flash-cards/{id}/`

**Treść żądania:**
```json
{
  "question": "Zaktualizowane pytanie",
  "answer": "Zaktualizowana odpowiedź",
  "flashcard_set": 1
}
```

**Odpowiedź:**
```json
{
  "id": 1,
  "question": "Zaktualizowane pytanie",
  "answer": "Zaktualizowana odpowiedź",
  "flashcard_set": 1
}
```

#### Częściowo zaktualizuj fiszkę
**PATCH** `/flash-card-sets/{flash_card_set_pk}/flash-cards/{id}/`

**Treść żądania:**
```json
{
  "answer": "Nowa odpowiedź"
}
```

**Odpowiedź:**
```json
{
  "id": 1,
  "question": "Co to jest API?",
  "answer": "Nowa odpowiedź",
  "flashcard_set": 1
}
```

#### Usuń fiszkę
**DELETE** `/flash-card-sets/{flash_card_set_pk}/flash-cards/{id}/`

---

### Oznaczanie fiszek
#### Oznacz jako znane
**POST** `/flash-card-sets/{flash_card_set_pk}/flash-cards/{id}/mark-as-known/`

**Treść żądania:**
```json
{
  "user": "nazwa_użytkownika"
}
```

#### Oznacz jako nieznane
**POST** `/flash-card-sets/{flash_card_set_pk}/flash-cards/{id}/mark-as-unknown/`

**Treść żądania:**
```json
{
  "user": "nazwa_użytkownika"
}
```

---

### Tryb nauki
#### Pobierz fiszki do nauki
**GET** `/flash-card-sets/{id}/learn/?user={username}`

**Odpowiedź:**
```json
[
  {
    "id": 5,
    "question": "Co to jest REST?",
    "answer": "Representational State Transfer",
    "flashcardSet": 2
  }
]
```
