import json


def clean_json(title_number):
    with open("temp_list.json", "r", encoding="utf-8") as file:
        data = list(json.load(file).items())

    current_title = data[title_number - 1]
    current_title = {current_title[0]: current_title[1]}

    with open("temp_list.json", "w", encoding="utf-8") as file:
        json.dump(current_title, file, ensure_ascii=False, indent=2)

    return current_title
