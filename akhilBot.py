#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
from keys import keys

    
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
   
ACCESS_KEY = keys['access_token']
ACCESS_SECRET = keys['access_token_secret']
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

twitter = tweepy.API(auth)
        
def tweet(message):
    status = message
    twitter.update_status(message)

def reader():
    argfile = str(sys.argv[1])
    quotes_file = open(argfile,'r')
    quote_array = quotes_file.readlines()
    quotes_file.close()
    return quote_array
     
if __name__ == '__main__':
    for quote in reader():
        tweet(quote)
        time.sleep(43200) # Tweet every 12 hours

