import json

from anime_parsers_ru import KodikParser

# Инициализация парсера
parser = KodikParser()

# Прописываем искомый тайтл
title = input("Впиши наименование тайтла: ")

# Находим всю информацию по наименованию
results = parser.search(title=title)
with open("test.txt", "w", encoding="utf-8") as file:
    json.dump(results, file, ensure_ascii=False, indent=2)

# Формируем словарь из "results" в читаемый вид
converted_result = {
    element["title"]: {
        "Год": element["year"],
        "Тип": "Сериал" if element["type"] == "anime-serial" else "Фильм",
        "ID Платформ": {
            "Шикомори": element["shikimori_id"],
            "Кинопоиск": element["kinopoisk_id"],
            "IMDB": element["imdb_id"],
        },
    }
    for element in results
}

# Сортируем словарь по годам
sorted_result = dict(sorted(converted_result.items(), key=lambda x: x[1]["Год"]))

# Записываем все в читабельный JSON формат
with open("anime_list.json", "w", encoding="utf-8") as file:
    json.dump(sorted_result, file, ensure_ascii=False, indent=2)

# Выводим краткую информацию
with open("anime_list.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    for key, value in data.items():
        print(f"{key}:\n-Год: {value["Год"]}\n-Формат: {value["Тип"]}\n")
