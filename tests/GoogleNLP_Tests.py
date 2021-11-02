import os
import unittest
from GoogleNLP import GoogleNLP
from dotenv import load_dotenv

load_dotenv()


@unittest.skipIf({"GOOGLE_APPLICATION_CREDENTIALS"} <= os.environ.keys(),
                 "Google NLP Credentials are not in the environment")
class TestGoogleNLPAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.google_nlp = GoogleNLP()

    def test_sentiment_score(self):
        sentiment_score = self.google_nlp.get_sentiment(
            "Google, headquartered in Mountain View (1600 Amphitheatre Pkwy, Mountain View, CA 940430), unveiled the new Android phone for $799 at the Consumer Electronic Show. Sundar Pichai said in his keynote that users love their new Android phones."
        )
        self.assertEqual(sentiment_score, 0.50)
