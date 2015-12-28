import os
import twython

twitter = twython.Twython(os.environ.get('TWITTER_KEY'),
                          os.environ.get('TWITTER_SECRET'),
                          os.environ.get('TWITTER_ACCESS_TOKEN'),
                          os.environ.get('TWITTER_ACCESS_STOKEN'))
def getTwitterID():

    json = twitter.get_followers_list(screen_name='motivational', count=200)

    for x in range(150):
        follow_req_sent = json['users'][x]['follow_request_sent']
        statuses_count = json['users'][x]['statuses_count']
        friends_count = json['users'][x]['friends_count']
        following = json['users'][x]['following']
        followers_count = json['users'][x]['followers_count']
        id = json['users'][x]['id']

        print follow_req_sent, statuses_count, friends_count, following, followers_count, id

        if follow_req_sent is False \
                and statuses_count > 5 \
                and friends_count > 5 \
                and following is False \
                and followers_count > 5:

            return id

    return -1

# get list of users that follow @motivational

twitterID=getTwitterID()

assert twitterID!=-1, "no valid id found"

# pick one and get timeline
u_json = twitter.get_user_timeline(user_id=twitterID, count=100)

c = 0
x = 0

# fav 4 tweets
while c<4:
    tweetid = u_json[x]['id']
    favorited = u_json[x]['favorited']
    text = u_json[x]['text']

    if favorited is not True:
        print 'Favoriting ', text, '. Tweet ID: ', tweetid

        twitter.create_favorite(id=tweetid)
        c+=1

    x += 1