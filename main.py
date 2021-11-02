from dotenv import load_dotenv
import matplotlib.pyplot as plt
from sys import exit
from os import _exit
from TwitterAPI import TwitterAPI
from TwitterClient import TwitterClient
from GoogleNLP import GoogleNLP


def get_topics():
    # Small loop to ensure the user inputs the correct number of topics to compare
    topics = []
    while len(topics) != 2:
        topics = input(
            "Enter two products/companies/items you'd like to compare (comma separated):\n\n"
        ).split(",")

        if len(topics) == 0:
            return "\nIt seems like you didn't enter anything to compare. Please enter 2 items.\n"
        elif len(topics) == 1:
            return "\nAh... It looks like you only entered one thing to compare. Please enter another item with it.\n"
        elif len(topics) > 2:
            return "\nWoah! Someone is ambitious... this can only handle 2 items at a time.\n"
    return topics


def main():
    # Load variables from a .env file
    load_dotenv()

    twitter_client = TwitterClient()
    google_nlp = GoogleNLP()

    print("\n\nWelcome to the Comparison Sentiment Analyzer!\n\n")

    topics = get_topics()

    max_tweets = -1
    while (max_tweets <= 10):
        try:
            if 0 < max_tweets < 10:
                print("Sorry, please enter a number that's 10 or more.\n")
            max_tweets = int(
                input('How many tweets should I analyze? (At least 10):  '))
        except ValueError:
            print("Sorry, please enter a number that's 10 or more.\n")

    # Creates a 2x1 subplot for each item being compared
    for plot, topic in enumerate(topics):
        saved_tweets = twitter_client.search_for_tweets(
            topic.strip(), max_tweets)
        x_marks = [num + 1 for num in range(len(saved_tweets))]

        # tweet_dates = []
        sentiment_scores = []

        print("Plotting the sentiment over time...")
        for i, tweet in enumerate(saved_tweets):
            sentiment_scores.append(google_nlp.get_sentiment(tweet.text))

        plt.subplot(2, 1, plot + 1)
        plt.title(f"{topic}'s Tweet Sentiments")
        plt.ylabel("Sentiment Score")
        plt.xlabel("Tweet Number")
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


# Main runner with some nicer error handling to handle the keyboard interrupt and EOF key
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\nThanks for using the program!\n')
        try:
            exit(0)
        except SystemExit:
            _exit(0)
    except EOFError:
        print('\nThanks for using the program!\n')
        try:
            exit(0)
        except SystemExit:
            _exit(0)