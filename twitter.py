import tweepy
import time
import csv
import sklearn

#insert your Twitter keys here
consumer_key ='Hidden'
consumer_secret='Hidden'
access_token='Hidden'
access_token_secret='Hidden'
twitter_handle= 'thetemplenews'

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


list = open('twitter_followers.txt','w')

if(api.verify_credentials):
    print ('We successfully logged in')



# try:
    tweets = api.user_timeline(screen_name=twitter_handle, page = 3)

    with open('tweets.csv', 'a') as csvfile:
        linewriter = csv.writer(csvfile, delimiter=',', quotechar="\"")
        linewriter.writerow(["tweets", "label"])

        for tweet in tweets:
            print(tweet.text)
            linewriter.writerow([tweet.text, 0])


list.close()