#!/usr/bin/python

# every hour, query a list of users
# find the most retweeted trending tweet *that I have not RT'd yet*
# retweet it

import os
import twython

from twitter_handle_list import trending_handles

twitter = twython.Twython(os.environ.get('TWITTER_KEY'),
                          os.environ.get('TWITTER_SECRET'),
                          os.environ.get('TWITTER_ACCESS_TOKEN'),
                          os.environ.get('TWITTER_ACCESS_STOKEN'))

def mostRetweeted(): # Find the best tweet to RT
    max = 0

    for user in trending_handles:

        json = twitter.get_user_timeline(screen_name=user, count=20)

        for x in range(20):
            RT_count = json[x]['retweet_count']
            fav_count = json[x]['favorite_count']
            retweeted_yet = json[x]['retweeted']
            tweet_id = json[x]['id']

            if RT_count+fav_count > max and retweeted_yet is not True:
                max = RT_count+fav_count
                bestTweetID = tweet_id

    print 'Best tweet is', bestTweetID, 'with', max,'likes/favorites that I have not RTed yet'

    return bestTweetID

twitter.retweet(id=mostRetweeted())