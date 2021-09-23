import tweepy
import os


class TwitterAPI:
    def __init__(self) -> None:
        self._batch_size = 10
        auth = tweepy.OAuthHandler(os.environ.get("TWITTER_API_KEY"),
                                   os.environ.get("TWITTER_API_SECRET"))
        auth.set_access_token(os.environ.get("TWITTER_ACCESS_TOKEN"),
                              os.environ.get("TWITTER_ACCESS_SECRET"))
        self._api = tweepy.API(auth)

    def get_self_timeline(self):
        return self._api.home_timeline()

    def get_timeline_for_user(self, username: str, max_number: int) -> list:
        all_tweets = []
        tweet_batch = []
        retrieved = 0

        if max_number < self._batch_size:
            all_tweets = self._api.user_timeline(screen_name=username,
                                                 count=max_number)
            return all_tweets

        while len(tweet_batch) > 0 or retrieved < max_number:

            # Tests if this is the first time the API is being called
            if retrieved == 0:
                tweet_batch = self._api.user_timeline(screen_name=username,
                                                      count=self._batch_size)
                retrieved += len(tweet_batch)
                print(f"First Batch Retrieval: {retrieved}")
                all_tweets.extend(tweet_batch)
            elif len(tweet_batch) > 0:
                oldest_tweet_id = tweet_batch[-1].id
                tweet_batch = self._api.user_timeline(screen_name=username,
                                                      count=self._batch_size,
                                                      max_id=oldest_tweet_id)
                retrieved += len(tweet_batch)
                print(
                    f"New Batch Retrieval: {len(tweet_batch)} -- Total Received: {retrieved}"
                )
                all_tweets.extend(tweet_batch)

        return all_tweets[0:max_number]
