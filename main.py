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
                  os.environ.get('TWITTER_ACCESS_TOKEN'),
                  os.environ.get('TWITTER_ACCESS_STOKEN'))

#print api.VerifyCredentials()

print os.environ.get('TWITTER_KEY'),os.environ.get('TWITTER_SECRET'),os.environ.get('TWITTER_ACCESS_TOKEN'),os.environ.get('TWITTER_ACCESS_STOKEN')

# Initializing manager
f = Forismatic()

# Getting Quote object & printing quote and author
q = f.get_quote()
quote_combined = u'%s\t%s' % (q.quote, q.author)

print quote_combined

#status = api.PostUpdate(quote_combined)