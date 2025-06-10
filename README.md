# Anime Pars

Flask-приложение с двумя REST API для поиска и генерации прямой ссылки на аниме-видео с помощью сервиса Kodik.  

Позволяет:
- Найти аниме по названию (`/search?title=...`);
- Получить прямую ссылку на серию (`/link?anime_id=...&translate_id=...&seria=...`).

---

## Примеры API-запросов

### Поиск по названию
```
GET /search?title=chainsaw
```

Ответ:
```json
[
  {
    "title": "Chainsaw Man",
    "year": 2022,
    "id": 15896,
    "episodes": 12,
    "translations": {
      "StudioBand": 1253,
      "AniDub": 982
    }
  }
]
```

### 🔗 Получение ссылки
```
GET /link?anime_id=15896&translate_id=982&seria=3
```

Ответ:
```json
{
  "link": "https://...720.mp4:hls:manifest"
}
```

---

## Установка

```bash
git clone https://github.com/H3WH4L3/anime-pars
cd anime-pars
python -m venv venv
source venv/bin/activate   # или .\venv\Scripts\activate на Windows
pip install -r requirements.txt
python app.py
```

---

## Стек
- Python
- Flask
- Kodik API (через `anime_parsers_ru`)
- REST API