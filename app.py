import requests

from flask import Flask

app = Flask(__name__)

NEWS_URL = ('https://newsapi.org/v2/top-headlines?'
            'country=us&'
            'apiKey=e092ed30578546bda11eeb912e62942b'
            )

SEARCH_NEWS_URL = ('https://newsapi.org/v2/everything?'
                   'q=Taliban&'
                   'from=2021-08-21&'
                   'sortBy=popularity&'
                   'apiKey=e092ed30578546bda11eeb912e62942b'
                   )


@app.route("/news")
def news():
    """
    This API will get all news and will return it in response.
    :return: json
    """
    try:
        response = requests.get(url=NEWS_URL)
    except ConnectionError as e:
        return {"message": e}
    json_body = response.json()
    return json_body


@app.route("/search-news")
def search_news():
    """
    This API will get all news containing a specific keyword and will return it in response.
    :return: json
    """
    try:
        response = requests.get(url=SEARCH_NEWS_URL)
    except ConnectionError as e:
        return {"message": e}
    json_body = response.json()
    return json_body


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
