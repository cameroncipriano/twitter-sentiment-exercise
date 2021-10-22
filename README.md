### EC601 Twitter-NLP Project 2

# Welcome to the Item-Sentiment Comparator


## About
This project demonstrates the ability to search Twitter for 2 different items, whether that be products, companies, people, etc, and compare the sentiment of the tweets about those two items.

## 1. Flow
1. Run the program and enter the two things you want to compare
   
2. Indicate how many tweets about each item you wish to include in the comparison
   - Limited to the number of tweets that exist about each topic
   - Limited by Twitter API's monthly quota of 500,000 tweets per month

3. A plot of each item's tweet sentiment will be displayed, allowing the user to compare the two subplots.

## 2. Running this project
To run this project, you'll need to have a Twitter Developer account with a working Twitter Project that includes the API Key, API Secret, Access Token, and Access Secret. Additionally, you will need a GoogleAPIs account and project with the NLP API enabled on the proejct (this requries you to enter billing information).

Once you have these things follow the following steps:
1. Install conda on your machine
2. Run `conda env create --file requirements.txt`
   - This will install all the correct dependencies required
3. Create a file in the project's root directory called `.env`
4. Inside this `.env` file, fill in these variables with your keys from your associated Twitter project
```
TWITTER_API_KEY=
TWITTER_API_SECRET=
TWITTER_ACCESS_TOKEN=
TWITTER_ACCESS_SECRET=
```
5. Once you have completed the above steps, you should be able to run `python main.py` and begin the experience

## 3. Is it Working?
If you have done the above steps correctly, you should see similar outputs to these:

Output from `python main.py`
![](Screen%20Shot%202021-10-21%20at%209.36.30%20PM.png)

Output once program is complete:
![](Screen%20Shot%202021-10-21%20at%209.42.40%20PM.png)
