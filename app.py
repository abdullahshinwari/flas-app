import requests

from flask import Flask, Response, request


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
    json_response = dict()
    try:
        response = requests.get(url=URL)
    except ConnectionError as e:
        return {"message": e}
    return Response(response, status=200, mimetype='application/json')


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
    except ConnectionError as e:
        return {"message": e}
    return Response(response, status=200, mimetype='application/json')


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
