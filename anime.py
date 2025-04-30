import json
from get_link import get_link
from anime_parsers_ru import KodikParser

# Инициализация парсера
parser = KodikParser()

# Прописываем искомый тайтл
title = "Магическая битва"


# Находим нужные ID и года
first_search_result = parser.search(title=title)

# Формируем словарь из "first_search_result" в читаемый вид
first_search_result = {
    element["title"]: {
        "Год": element["year"],
        "ID": element["shikimori_id"],
    }
    for element in first_search_result
}

# Сортируем словарь по годам
final_result = dict(sorted(first_search_result.items(), key=lambda x: x[1]["Год"]))

# Формирую словарь со всей информацией
for key, value in final_result.items():
    response = parser.api_request(
        endpoint="search", filters={"shikimori_id": value["ID"]}
    )
    test = {}
    for element in response["results"]:
        translation = element["translation"]
        test[translation["title"]] = translation["id"]
    final_result[key]["Количество серий"] = response["results"][0]["episodes_count"]
    final_result[key]["Переводы"] = test

with open("anime_list.json", "w", encoding="UTF-8") as file:
    json.dump(final_result, file, ensure_ascii=False, indent=2)


#Костыль доработки
print("Название: ", title)

print("Кол-во серий: ", final_result["Магическая битва [ТВ-1]"]["Количество серий"])

input_seria = input("Введите номер серии: ")

id_anime = final_result["Магическая битва [ТВ-1]"]["ID"]
id_translate = final_result["Магическая битва [ТВ-1]"]["Переводы"]["Studio Band"]

result = get_link(id_anime, id_translate, int(input_seria))
print(result)
