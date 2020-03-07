import base64
import json

from credentials import twitter_api_key, twitter_api_secret_key, \
    twitter_access_token, twitter_access_token_secret

base_url = 'https://api.twitter.com/'
search_url = f'{base_url}1.1/tweets/search/fullarchive/development.json'

"""
key_secret = '{}:{}'.format(twitter_api_key, twitter_api_secret_key).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')

import requests

base_url = 'https://api.twitter.com/'
auth_url = f'{base_url}oauth2/token'

auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {
    'grant_type': 'client_credentials'
}

auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
auth_resp.status_code

# Keys in data response are token_type (bearer) and access_token (your access token)
auth_resp.json().keys()

access_token = auth_resp.json()['access_token']

search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

search_params = {
    "query": "#metoo",
    #"mawResults": 10
}

search_url = f'{base_url}1.1/tweets/search/fullarchive/development.json'

search_resp = requests.get(search_url, headers=search_headers, search_params=search_params)

tweet_data = search_resp.json()

for x in tweet_data['results']:
    print(x['text'] + '\n')
"""

from TwitterAPI import TwitterAPI
api = TwitterAPI(twitter_api_key, twitter_api_secret_key, twitter_access_token, twitter_access_token_secret)
r = api.request(
    search_url,
    {
        'query': "#metoo",
        'language': "ja"
    }
)
for item in r:
    print(item)

