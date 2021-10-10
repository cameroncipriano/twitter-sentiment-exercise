from dotenv import load_dotenv
import matplotlib.pyplot as plt
import sys
import os
from TwitterAPI import TwitterAPI
from TwitterClient import TwitterClient
from GoogleNLP import GoogleNLP


def main():
    # Load variables from a .env file
    load_dotenv()

    # Create the Twitter API and Google NLP link
    # twitter_api = TwitterAPI()
    twitter_client = TwitterClient()
    google_nlp = GoogleNLP()

    # twitter_account = "@JoeBiden"
    # recent_tweets = 40

    # print(
    # f"Obtaining the {recent_tweets} most recent tweets from {twitter_account}..."
    # )
    # saved_tweets = twitter_api.get_timeline_for_user(twitter_account,
    #                                                  recent_tweets)
    print("\n\nWelcome to the Comparison Sentiment Analyzer!\n\n")

    topics = []
    while len(topics) != 2:
        topics = input(
            "Enter two products/companies/items you'd like to compare (comma separated):\n\n"
        ).split(",")

        if len(topics) == 0:
            print(
                "\nIt seems like you didn't enter anything to compare. Please enter 2 items.\n"
            )
        elif len(topics) == 1:
            print(
                "\nAh... It looks like you only entered one thing to compare. Please enter another item with it.\n"
            )
        elif len(topics) > 2:
            print(
                "\nWoah! Someone is ambitious... this can only handle 2 items at a time.\n"
            )

    for plot, topic in enumerate(topics):
        saved_tweets = twitter_client.search_for_tweets(topic)
        x_marks = [num + 1 for num in range(len(saved_tweets))]

        # tweet_dates = []
        sentiment_scores = []

        print("Plotting the sentiment over time...")
        for i, tweet in enumerate(saved_tweets):
            sentiment_scores.append(google_nlp.get_sentiment(tweet.text))

        plt.subplot(2, 1, plot + 1)
        plt.title(f"{topic}'s Tweet Sentiments")
        plt.ylabel("Sentiment Score")
        plt.xlabel("Date of Tweet")
        # plt.xticks(x_marks, labels=tweet_dates, rotation=90)
        plt.plot(x_marks, sentiment_scores)
        plt.fill_between(x=x_marks, y1=0.25, y2=1.0, color="green", alpha=0.5)
        plt.fill_between(x=x_marks,
                         y1=-0.25,
                         y2=0.25,
                         color="yellow",
                         alpha=0.5)
        plt.fill_between(x=x_marks, y1=-1.00, y2=-0.25, color="red", alpha=0.5)

    plt.show()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\nThanks for using the program!\n')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    except EOFError:
        print('\nThanks for using the program!\n')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)