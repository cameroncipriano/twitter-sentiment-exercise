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

    def search_for_tweets(self, topic: str, max_tweets: int = 200) -> list:
        query = f"(\"{topic}\" OR #{''.join(topic.split())}) -is:retweet lang:en"
        all_tweets = []
        num_tweets = len(all_tweets)
        print(f"\n\nSearching Twitter for '{topic}' ...")

        pagination_token = 0
        while (pagination_token != None and num_tweets < max_tweets):
            remaining = max_tweets - num_tweets
            if pagination_token:
                tweet_batch: tuple = self._client.search_recent_tweets(
                    query,
                    max_results=min(remaining, 100),
                    next_token=pagination_token)
            else:
                tweet_batch: tuple = self._client.search_recent_tweets(
                    query, max_results=min(remaining, 100))

            # Tweet_batch is a tuple: [0]->data, [1]->includes, [2]->errors, [3]->meta
            all_tweets.extend(tweet_batch[0])
            pagination_token = tweet_batch[3][
                "next_token"] if "next_token" in tweet_batch[3].keys(
                ) else None

            num_tweets = len(all_tweets)
            print(f"Obtained {num_tweets} tweets so far...")

        print(
            f"Grabbed a total of {len(all_tweets)} tweets from the topic '{topic}'\n\n"
        )
        return all_tweets
