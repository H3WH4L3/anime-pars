from anime_parsers_ru import KodikParser

# Инициализация парсера
parser = KodikParser()

def get_link(id_anime, id_translate, seria_id):
    seria = parser.get_link(
        id=id_anime,
        id_type="shikimori",
        seria_num=seria_id,
        translation_id=id_translate)

    link = "https:" + str(seria[0]) + "720.mp4:hls:manifest"
    return link







