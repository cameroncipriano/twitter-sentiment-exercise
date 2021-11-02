import os
import unittest
from TwitterClient import TwitterClient
from dotenv import load_dotenv

load_dotenv()


@unittest.skipIf({
    "TWITTER_BEARER_TOKEN", "TWITTER_API_KEY", "TWITTER_API_SECRET",
    "TWITTER_ACCESS_TOKEN", "TWITTER_ACCESS_SECRET"
} <= os.environ.keys(), "Twitter credentials do not exist in the environment")
class TestTwitterAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.twitter_client = TwitterClient()

    def test_returned_tweet_length(self):
        tweets = self.twitter_client.search_for_tweets("today")
        self.assertEqual(len(tweets), 200)