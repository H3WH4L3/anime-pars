import json
import os

from anime_parsers_ru import KodikParser

from scripts.anime_title_choise import clean_json
from scripts.choise_title import get_json_titles
from scripts.get_link import get_link
from scripts.get_translations import get_translations

# Инициализация парсера
parser = KodikParser()

# Прописываем искомый тайтл
title = input("Введите тайтл: ")

# Формируем первый список
get_json_titles(title)

# Выводим список
with open("temp_list.json", "r", encoding="UTF-8") as file:
    data = json.load(file)
    for i, (key, value) in enumerate(data.items()):
        print(
            f"{i + 1}. {key}\n  - Количество серий: {value["Количество серий"]}\n  - Год: {value["Год"]}\n"
        )

# Номер тайтла
anime_choise = int(input("Укажите номер тайтла из списка: "))

# Оставляем один результат
temp_anime_dict = clean_json(anime_choise)

# Фиксируем ID
anime_id = list(temp_anime_dict.values())[0]["ID"]

# Фиксируем номер серии
seria = int(input("Укажите номер серии: "))

# Выводим переводы
print(get_translations(temp_anime_dict))

# Устанавливаем ID перевода
traslations_number = int(input("Укажите номер перевода: "))
traslations_id = get_translations(temp_anime_dict, traslations_number)

# Выводим ссылку
print(get_link(anime_id, traslations_id, seria))

# Удаляем временный json
os.remove("temp_list.json")
