# Python libs
import os
import logging
import random

# Third-party dependencies
import twython
from forismatic import Forismatic
import text2img

def roll():
    a = random.randint(0,9)
    if a<5:
        return True
    else:
        return False

logging.basicConfig(format='%(asctime)s %(message)s', filename='quote.log',level=logging.INFO)

# Twitter settings
twitter = twython.Twython(os.environ.get('TWITTER_KEY'),
                  os.environ.get('TWITTER_SECRET'),
                  os.environ.get('TWITTER_ACCESS_TOKEN'),
                  os.environ.get('TWITTER_ACCESS_STOKEN'))

# Initializing manager
f = Forismatic()
q = f.get_quote()

logging.info('Retrieved quote: %s, -%s', q.quote, q.author)

# IMAGE POST TO TWITTER
if len(q.quote)+len(q.author)+1>140 or roll(): # 1:10 chance to post image or >140 char
    text2img.text2img(q.quote,q.author)
    fname = open("quote_img.png", 'rb')
    twitter.upload_media(status = "#motivationalquote #"+q.author, media = fname)

# TEXT ONLY POST TO TWITTER
else:
    combined_quote = q.quote
    combined_quote += '-'
    combined_quote += q.author

    if len(combined_quote)+len(" #quote #motivation")<=140: # add hash tags if enough space
        combined_quote += " #quote #motivation"
    elif len(combined_quote)+len(" #quote")<=140:
        combined_quote += " #quote"

    twitter.update_status(status=combined_quote)