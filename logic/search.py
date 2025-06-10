from anime_parsers_ru import KodikParser

parser = KodikParser()


def get_anime_data(title):
    """
    Формирует список аниме по заданному названию.

    Каждый элемент в списке содержит:
        - title (str): название тайтла
        - year (int): год выпуска
        - episodes (int): количество серий
        - translations (dict[str, int]): словарь с переводами, где:
            ключ — название команды переводчика,
            значение — ID перевода

    Parameters:
        title (str): Название аниме для поиска

    Returns:
        list[dict]: Список найденных тайтлов с деталями и переводами,
                    или None, если ничего не найдено.
    """
    try:
        anime_list = parser.search(title=title)
    except:
        return None
    if not anime_list:
        return None

    result = []
    for element in anime_list:
        if element.get("shikimori_id") is None:
            continue

        anime_id = element["shikimori_id"]
        year = element.get("year")
        title_name = element.get("title")

        response = parser.api_request(
            endpoint="search", filters={"shikimori_id": anime_id}
        )
        if not response["results"]:
            continue

        episodes = response["results"][0].get("episodes_count", 0)
        translations = {
            item["translation"]["title"]: item["translation"]["id"]
            for item in response["results"]
        }

        result.append(
            {
                "title": title_name,
                "year": year,
                "id": anime_id,
                "episodes": episodes,
                "translations": translations,
            }
        )

    return result
