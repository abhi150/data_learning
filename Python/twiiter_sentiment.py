import tweepy
from textblob import TextBlob


consumer_key = 'iicRdbtAYItuoFazHY90B6kFT'
consumer_secret = '8pdOVfLYCMuUYKxUFwPUucJxivq1WG4mLxbqlQqqbdJIVcfAGS'


access_token = '2234539196-mzMmrv71of4DooW5jkWFQHDBA3fOkpYqqOJbROD'
access_token_secret = 'YEkESqNwFJn6Kvf1hlxTcHd6nXfaOOl0xuLwLq8J56Poj'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)exi
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Step 3 - Retrieve Tweets
public_tweets = api.search('Trump')



# CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
# and label each one as either 'positive' or 'negative', depending on the sentiment
# You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)

    # Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")