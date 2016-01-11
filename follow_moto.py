import os
import twython

twitter = twython.Twython(os.environ.get('TWITTER_KEY'),
                          os.environ.get('TWITTER_SECRET'),
                          os.environ.get('TWITTER_ACCESS_TOKEN'),
                          os.environ.get('TWITTER_ACCESS_STOKEN'))

def getTwitterID(json):

    for x in range(150):
        follow_req_sent = json['users'][x]['follow_request_sent']
        statuses_count = json['users'][x]['statuses_count']
        friends_count = json['users'][x]['friends_count']
        following = json['users'][x]['following']
        followers_count = json['users'][x]['followers_count']
        id = json['users'][x]['id']

        if follow_req_sent is False \
                and statuses_count > 5 \
                and friends_count > 5 \
                and following is False \
                and followers_count > 5:

            print "Following id", id

            return id

    return -1

json = twitter.get_followers_list(screen_name='motivational', count=150)

twitterID=getTwitterID(json)
assert twitterID != -1, "No twitter ID found"
twitter.create_friendship(user_id=twitterID)

twitterID=getTwitterID(json)
assert twitterID != -1, "No twitter ID found"
twitter.create_friendship(user_id=twitterID)

twitterID=getTwitterID(json)
assert twitterID != -1, "No twitter ID found"
twitter.create_friendship(user_id=twitterID)