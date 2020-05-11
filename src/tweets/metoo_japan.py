import base64
import json
import time

import requests

from credentials import twitter_api_key, twitter_api_secret_key, \
    twitter_access_token, twitter_access_token_secret


base_url = 'https://api.twitter.com/'
search_url = f'{base_url}1.1/tweets/search/fullarchive/development.json'
auth_url = f'{base_url}oauth2/token'


key_secret = '{}:{}'.format(twitter_api_key, twitter_api_secret_key).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')
auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}
auth_data = {
    'grant_type': 'client_credentials'
}
auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
# Keys in data response are token_type (bearer) and access_token (your access token)
auth_resp.json().keys()
access_token = auth_resp.json()['access_token']
search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

search_params = {
    "query": "#metoo lang:ja",
    "fromDate": "20160101000"
}

search_resp = requests.get(search_url, headers=search_headers, params=search_params)
tweet_data = search_resp.json()
if tweet_data.get('error'):
    print(tweet_data.get('error').get('message'))

while 'next' in tweet_data:
    counter = 0
    while counter < 180:
        counter += 1
        search_params.update({"next": tweet_data.get('next')})
        search_resp = requests.get(search_url, headers=search_headers, params=search_params)
        tweet_data = search_resp.json()
        if tweet_data.get('error'):
            print(tweet_data.get('error').get('message'))
            break
        with open("metoo_japan.jsonl", "a+") as jsonl_file:
            print(tweet_data.get('results')[0])
            for tweet in tweet_data.get('results'):
                jsonl_file.write(json.dumps(tweet))
    time.sleep(900)
