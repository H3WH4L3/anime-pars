import json

from flask import Flask, Response, jsonify, request

from logic.link import get_stream_link
from logic.search import get_anime_data

app = Flask(__name__)


# API Для вывода результата. /search?title=...
@app.route("/search", methods=["GET"])
def search_anime():
    # Берем подаваемое значение
    title = request.args.get("title")

    # Если ничего не подано - возвращаем 400
    if not title:
        return jsonify({"error": "Не указано название аниме"}), 400

    # Запускаем работу скрипта для формирования JSON результата
    result = get_anime_data(title)

    # Если вернуло None, значит ничего не нашли
    if not result:
        return jsonify({"error": f"Аниме '{title}' не найдено"}), 404

    # Возвращаем результат в формате JSON
    return Response(
        json.dumps(result, ensure_ascii=False, indent=2),
        content_type="application/json; charset=utf-8",
    )


# API Для формирования ссылки. /link anime_id=... translate_id=... seria=...
@app.route("/link", methods=["GET"])
def link():
    # Сохраняем себе данные из трех атрибутов: ID аниме, ID перевода, Номер серии
    anime_id = request.args.get("anime_id")
    translate_id = request.args.get("translate_id")
    seria = request.args.get("seria")

    # Если чего-то нехватает, то возвращаем 400
    if not all([anime_id, translate_id, seria]):
        return (
            jsonify({"error": "Не хватает параметров (anime_id, translate_id, seria)"}),
            400,
        )

    # Пробуем запустить поиск.
    try:
        link = get_stream_link(anime_id, int(translate_id), int(seria))
        return jsonify({"link": link})

    # Ничего не нашли, либо данные битые, то возвращаем 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Запуск постоянной работы скрипта
if __name__ == "__main__":
    app.run(debug=True)
