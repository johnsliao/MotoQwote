import os
import config
import text2img
import json

# Third-party dependencies
import twython

from forismatic import Forismatic

# Twitter settings
twitter = twython.Twython(os.environ.get('TWITTER_KEY'),
                  os.environ.get('TWITTER_SECRET'),
                  os.environ.get('TWITTER_ACCESS_TOKEN'),
                  os.environ.get('TWITTER_ACCESS_STOKEN'))

# Initializing manager
f = Forismatic()

# Getting Quote object & printing quote and author

q = f.get_quote()

print q.quote

# run text2img with paramters
text2img.text2img(q.quote,q.author)

# post image to twitter
f = open("a_test.png", 'rb')
twitter.upload_media(status = "#motivationquote", media = f)