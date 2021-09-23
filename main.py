from Twitter import TwitterAPI
from GoogleNLP import GoogleNLP
from dotenv import load_dotenv


def main():
    # Load variables from a .env file
    load_dotenv()

    # Create the Twitter API and Google NLP link
    twitter_api = TwitterAPI()
    google_nlp = GoogleNLP()

    saved_tweets = twitter_api.get_timeline_for_user("@elonmusk", 30)
    for i, tweet in enumerate(saved_tweets):
        print(f"---------------------\nTweet {i+1}: {tweet.created_at}")
        print(f"{tweet.text}\n---------------------")


if __name__ == "__main__":
    main()