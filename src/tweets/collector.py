from twython import Twython

from credentials import twitter_api_key, twitter_api_secret_key, \
    twitter_access_token, twitter_access_token_secret


def test():
    api = Twython(twitter_api_key,
                  twitter_api_secret_key,
                  twitter_access_token,
                  twitter_access_token_secret)

    api_url = 'https://api.twitter.com/1.1/tweets/search/fullarchive/development.json'
    constructed_url = api.construct_api_url(api_url, q='#metoo')
    minimal_url = 'search/fullarchive/development'


    latitude_paris = 48.8534
    longitude_paris = 2.3488
    radius = "50km"
    # geocode = f"{latitude_paris},{longitude_paris},{radius}"
    language = "ja"

    #results = api.search(q=add_filter_to_query("élite"),
    #                     langg=language,
    #                     result_type="mixed",
    #                     geocode=geocode)

    results = api.request(endpoint=minimal_url)

    for result in results.get('statuses'):
        print(result.get('text'))


def add_filter_to_query(q: str) -> str:
    no_retweet_no_replies = f"{q} AND -filter:retweets AND -filter:replies"
    return f"{q} AND -filter:replies"


if __name__ == "__main__":
    test()
