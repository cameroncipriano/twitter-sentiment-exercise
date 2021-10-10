from typing import Tuple
import tweepy
import os


class TwitterClient:
    def __init__(self) -> None:
        self._client = tweepy.Client(
            bearer_token=os.environ.get("TWITTER_BEARER_TOKEN"),
            consumer_key=os.environ.get("TWITTER_API_KEY"),
            consumer_secret=os.environ.get("TWITTER_API_SECRET"),
            access_token=os.environ.get("TWITTER_ACCESS_TOKEN"),
            access_token_secret=os.environ.get("TWITTER_ACCESS_SECRET"))

    def search_for_tweets(self, topic: str) -> list:
        query = f"(\"{topic}\" OR #{''.join(topic.split())}) -is:retweet lang:en"
        all_tweets = []

        print(f"\n\nSearching Twitter for '{topic}' ...")

        pagination_token = 0
        while (pagination_token != None and len(all_tweets) < 200):
            if pagination_token:
                tweet_batch: tuple = self._client.search_recent_tweets(
                    query, max_results=100, next_token=pagination_token)
            else:
                tweet_batch: tuple = self._client.search_recent_tweets(
                    query, max_results=100)

            # Tweet_batch is a tuple: [0]->data, [1]->includes, [2]->errors, [3]->meta
            all_tweets.extend(tweet_batch[0])
            pagination_token = tweet_batch[3][
                "next_token"] if "next_token" in tweet_batch[3].keys(
                ) else None

            print(f"Obtained {len(all_tweets)} tweets so far...")

        print(
            f"Grabbed a total of {len(all_tweets)} tweets from the topic '{topic}'\n\n"
        )
        return all_tweets
