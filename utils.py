def to_json(data, message, status_code):
    try:
        return {"data": data,
                "meta": {
                    "message": message,
                    "status_code": status_code
                    }
                }
    except:
        return {"data": "",
                "meta": {
                    "message": "fail to return response",
                    "status_code": 400
                    }
                }


'''
testing function
'''

# def recursive_search(keys, dictionary):
#     searched_keys = dict()
#     # searched_keys = {key: value for key, value in dictionary.items() if key in ["title", "url", "source"]}\
#
#     for key, value in dictionary.items():
#         print({"m": key})
#
#     for value in dictionary.values():
#         if isinstance(value, dict):
#             recursive_search(keys, value)
#         elif isinstance(value, list):
#             for item in value:
#                 if isinstance(item, dict):
#                     recursive_search(keys, item)
#     return searched_keys

# json_body = response.json()
