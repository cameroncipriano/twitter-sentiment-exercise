from Twitter import TwitterAPI
from GoogleNLP import GoogleNLP
from dotenv import load_dotenv
import matplotlib.pyplot as plt


def main():
    # Load variables from a .env file
    load_dotenv()

    # Create the Twitter API and Google NLP link
    twitter_api = TwitterAPI()
    google_nlp = GoogleNLP()

    twitter_account = "@elonmusk"
    recent_tweets = 30

    tweet_dates = []
    sentiment_scores = []

    print(
        f"Obtaining the {recent_tweets} most recent tweets from {twitter_account}..."
    )
    saved_tweets = twitter_api.get_timeline_for_user(twitter_account,
                                                     recent_tweets)
    for i, tweet in enumerate(saved_tweets):

        tweet_dates.append(tweet.created_at)
        sentiment_scores.append(google_nlp.get_sentiment(tweet.text))
    x_marks = [num + 1 for num in range(len(saved_tweets))]

    plt.figure()
    plt.title(
        f"{twitter_account}'s {recent_tweets} Most Recent Tweet Sentiments")
    plt.ylabel("Sentiment Score")
    plt.xlabel("Date of Tweet")
    plt.xticks(x_marks, labels=tweet_dates, rotation=90)
    plt.plot(x_marks, sentiment_scores)
    plt.fill_between(x=x_marks, y1=0.25, y2=1.0, color="green", alpha=0.5)
    plt.fill_between(x=x_marks, y1=-0.25, y2=0.25, color="yellow", alpha=0.5)
    plt.fill_between(x=x_marks, y1=-1.00, y2=-0.25, color="red", alpha=0.5)
    plt.show()


if __name__ == "__main__":
    main()