import requests

from flask import Flask, request

from utils import to_json


app = Flask(__name__)


URL = ('https://newsapi.org/v2/top-headlines?''country=us&''{}''from=2021-08-21&''sortBy=popularity&'
       'apiKey=e092ed30578546bda11eeb912e62942b'
       )


@app.route("/news", methods=['GET'])
def news():
    """
    This API will get all news and will return it in response.
    :return: json
    """
    try:
        response = requests.get(url=URL)
        if response.status_code != 200:
            return to_json(data="", message='Error', status_code=400)  # dummy status code
    except ConnectionError as e:
        return to_json(data="", message=e, status_code=400)  # dummy status code
    response_data = response.json()
    return to_json(data=response_data, message="Success", status_code=200)


@app.route("/search-news", methods=['GET'])
def search_news():
    """
    This API will get all news containing a specific keyword and will return it in response.
    :return: json
    """
    keyword = request.args.get('search')
    url = URL.format('q=' + keyword + '&')
    try:
        response = requests.get(url=url)
        if response.status_code != 200:
            return to_json(data="", message='Error', status_code=400)  # dummy status code
    except ConnectionError as e:
        return to_json(data="", message=e, status_code=400)  # dummy status code
    response_data = response.json()
    return to_json(data=response_data, message="Success", status_code=200)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
