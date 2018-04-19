#

# Tested API: GET movie/{movie_id}
#TODO: 1. create class MOVIES, then create method for each target API. Like forllowing
    # def get_detailes:
    # def get account_states
    # get alternative_tieles

#TODO: 2. I will separate test_cases.py file, and figure out to access it from Movie class.

# How to run this. It will not run in windows command prompt, but run under IDE, pycharm.
# what am I testing? In this api, GET /movie/{movie_id}, I am testing {movie_id}
# I create Class, static method to parameterize api_key
# test_cases, is data, a list of dict. I will loop over it and replace {movie_id} with all values of key 'id'.
# test_cases, has both 'pos' and 'neg'
# I make request, and get response. For 'pos', i will check response['id'] is matching 'id' from test_case, which is 15.
#   I could check other paramaters as well, like Response [200]
# for 'neg', i will check reponse[404]
# both positive and negative check, use assert


import importlib
import copy
import requests
import json

__author__ = "Dylan Dai"


# create helper class, where contains static method for easy access
# only 1 method now, but can put in whatever i want in the future

class Helper:

    @staticmethod
    def get_apiKey():
        api_key = "b8494f0c03ef1ba54406cc4ce85f0edd"
        return api_key



#importlib.import_module(helper)
#from soFiChallenge import test_cases


test_cases = [
    {"type": "pos", "id": '15'},
    {"type": "neg", "id": '0'},
   {"type": "neg", "id": '-1'},
    {"type": "neg", "id": "True"},
    {"type": "neg", "id": "False"},
    {"type": "neg", "id": "special$#@$%"},
    {"type": "neg", "id": "string space"},
    {"type": "neg", "id": "{}"},
    {"type": "neg", "id": ""},
    {"type": "neg", "id": "\\u0192\\u0224\\u0193\\u0225\\u0194\\u0226\\u0195\\u0227\\u0196\\u0228"},
    {"type": "neg", "id": "abcd\\\\123"},
    {"type": "neg", "id": "abcd/12/3"},
    {"type": "neg", "id": "abcd:123"},
    {"type": "neg", "id": "abcd.123"},
    {"type": "neg", "id": "[]"    },
    {"type": "neg", "id": "[abcd]/123"},
    {"type": "neg", "id": "ABCD"},
    {"type": "neg", "id": "select * from users;"},
    {"type": "neg", "id": "abcd;123"}

]

print(len(test_cases))



def get_movie_by_id(movie_id):
    #my_helper = helper.Helper
    api_key = Helper.get_apiKey()

    base_url = "https://api.themoviedb.org/3"
    url = base_url + "/movie/" + movie_id + "?api_key=" + api_key + "&language=en-US"

    response = requests.get(url)
    return response


#start here
new_testcases = copy.deepcopy(test_cases)

new_list = [d['id'] for d in new_testcases]

for i in range(len(new_list)):

    movie_id = new_list[i]
    response = get_movie_by_id(movie_id)
    response_dict = (response.json())
    print(response_dict)
    print(response)

    if test_cases[i]['type'] == 'pos':
        assert response_dict['id'] == 15, "Failed to return movie info"

    elif test_cases[i]['type'] == 'neg':
            assert "<Response [404]>", "failed"












