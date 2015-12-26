import os
import twython

twitter = twython.Twython(os.environ.get('TWITTER_KEY'),
                          os.environ.get('TWITTER_SECRET'),
                          os.environ.get('TWITTER_ACCESS_TOKEN'),
                          os.environ.get('TWITTER_ACCESS_STOKEN'))

def getTwitterID():

    json = twitter.get_followers_list(screen_name='motivational', count=150)

    for x in range(150):
        follow_req_sent = json['users'][x]['follow_request_sent']
        statuses_count = json['users'][x]['statuses_count']
        friends_count = json['users'][x]['friends_count']
        following = json['users'][x]['following']
        followers_count = json['users'][x]['followers_count']
        id = json['users'][x]['id']

        if follow_req_sent is not True \
                and statuses_count > 100 \
                and friends_count > 100 \
                and following is not True \
                and followers_count > 100:

            print "Following id", id

            return id

twitter.create_friendship(user_id=getTwitterID())