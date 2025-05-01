def get_translations(data, translation_number=-1):
    # Второй вызов
    if translation_number != -1:
        data = list(data.values())[0]["Переводы"]
        data = list(data.items())
        return list(data[translation_number])[1]

    # Первый вызов
    temp_translations = list(data.values())[0]["Переводы"]
    temp_list = []
    for i, key in enumerate(temp_translations.keys()):
        temp_list.append(f"{i + 1}. {key}")
    return "\n".join(temp_list)
