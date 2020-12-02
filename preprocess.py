import csv
import time
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation


#pre processing class
class DataPre:
    def __init__(self):
        # username and punctuation set using nltk library
        self.extra = set(stopwords.words('english')+list(punctuation) + ['USER_NAME', 'URL'])

    # gets the list of tweets, cleans them using removeExtra, and returns the clean list
    def initialize(self, allTweets):
        tweets = []
        for tweet in allTweets:
            tweets.append((self.removeExtra(tweet["tweet"]), tweet["label"]))
        return tweets

    def removeExtra(self, tweet):
        # tweet becomes lower case
        tweet = tweet.lower()
        # remove URLs
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)
        # remove usernames
        tweet = re.sub('@[^\s]+', 'USER_NAME', tweet)
        # remove hashtag tags
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
        # remove repeats
        tweet = word_tokenize(tweet)
        return [word for word in tweet if word not in self.extra]

