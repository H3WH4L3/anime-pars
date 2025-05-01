import json

from anime_parsers_ru import KodikParser

parser = KodikParser()


def get_json_titles(title):
    # Находим первую инфу
    anime_list = parser.search(title=title)

    # Формируем словарь результатов
    anime_list = {
        element["title"]: {
            "Год": element["year"],
            "ID": element["shikimori_id"],
        }
        for element in anime_list
    }

    # Сортируем словарь по годам
    anime_list = dict(sorted(anime_list.items(), key=lambda x: x[1]["Год"]))

    # Находим количество серий и перевода, и вносим в основной словарь

    for key, value in anime_list.items():
        response = parser.api_request(
            endpoint="search", filters={"shikimori_id": value["ID"]}
        )
        temp_translations = {}
        for element in response["results"]:
            translation = element["translation"]
            temp_translations[translation["title"]] = translation["id"]
        anime_list[key]["Количество серий"] = response["results"][0]["episodes_count"]
        anime_list[key]["Переводы"] = temp_translations

    # Заносим результаты в JSON
    with open("temp_list.json", "w", encoding="UTF-8") as file:
        json.dump(anime_list, file, ensure_ascii=False, indent=2)
