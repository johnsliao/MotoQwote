import os

# Third-party dependencies
import twitter
from forismatic import Forismatic

'''
To do
Change access tokens to new account
find python lib to convert text -> image
create new volume in AWS
upload and run on chron job
'''

api = twitter.Api(os.environ.get('TWITTER_KEY'),
                  os.environ.get('TWITTER_SECRET'),
                  os.environ.get('TWITTER_TOKEN'),
                  os.environ.get('TWITTER_SECRET_TOKEN'))

#print api.VerifyCredentials()
print os.environ.get('TWITTER_KEY'),

# Initializing manager
f = Forismatic()

# Getting Quote object & printing quote and author
q = f.get_quote()
print u'%s\t%s' % (q.quote, q.author)