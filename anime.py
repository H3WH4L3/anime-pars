import json

from anime_parsers_ru import KodikParser

# Инициализация парсера
parser = KodikParser()


# Функция формирования ссылки на видео-файл
# def get_anime_link(
#     get_id, get_id_type="shikomori", get_seria_num="0", get_translation="610"
# ):
#     return parser.get_link(
#         id=get_id,
#         id_type=get_id_type,
#         seria_num=get_seria_num,
#         translation_id=get_translation,
#     )


title = "Наруто"
results = parser.search(title=title)
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
sorted_result = dict(
    sorted(converted_result.items(), key=lambda x: (x[1]["Тип"], x[1]["Год"]))
)
with open("anime_list.json", "w", encoding="utf-8") as file:
    json.dump(sorted_result, file, ensure_ascii=False, indent=2)
