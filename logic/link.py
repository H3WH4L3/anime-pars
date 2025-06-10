from anime_parsers_ru import KodikParser

parser = KodikParser()


def get_stream_link(anime_id, translate_id, seria):
    """
    Формирует ссылку на конкретную серию аниме с указанным переводом.

    Parameters:
        anime_id (str): ID тайтла по Shikimori
        translate_id (int): ID команды переводчиков
        seria (int): Номер серии

    Returns:
        str: Ссылка вида 'https://...720.mp4:hls:manifest'
    """
    response = parser.get_link(
        id=anime_id, id_type="shikimori", seria_num=seria, translation_id=translate_id
    )

    if not response:
        raise ValueError("Не удалось получить ссылку")

    return "https:" + str(response[0]) + "720.mp4:hls:manifest"
