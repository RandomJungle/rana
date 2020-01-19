from twython import Twython

from credentials import twitter_api_key, twitter_api_secret_key, \
    twitter_access_token, twitter_access_token_secret


def test():
    api = Twython(twitter_api_key,
                  twitter_api_secret_key,
                  twitter_access_token,
                  twitter_access_token_secret)

    latitude_paris = 48.8534
    longitude_paris = 2.3488
    radius = "50km"
    geocode = f"{latitude_paris},{longitude_paris},{radius}"
    language = "fr"

    results = api.search(q=add_filter_to_query("élite"),
                         langg=language,
                         result_type="mixed",
                         geocode=geocode)
    for result in results.get('statuses'):
        print(result.get('text'))


def add_filter_to_query(q: str) -> str:
    return f"{q} AND -filter:retweets AND -filter:replies"


if __name__ == "__main__":
    test()