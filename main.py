#!/usr/bin/python

# Python libs
import os
import logging
import random

# Third-party dependencies
import twython
from forismatic import Forismatic
import text2img

def roll():
    a = random.randint(0, 9)
    if a < 5:
        return True
    else:
        return False

# Twitter settings
twitter = twython.Twython(os.environ.get('TWITTER_KEY'),
                          os.environ.get('TWITTER_SECRET'),
                          os.environ.get('TWITTER_ACCESS_TOKEN'),
                          os.environ.get('TWITTER_ACCESS_STOKEN'))

# Initializing manager
f = Forismatic()
q = f.get_quote()

#logging.basicConfig(format='%(asctime)s %(message)s', filename='quote.log', level=logging.INFO)
#logging.info('Retrieved quote: %s, -%s', q.quote, q.author)

# IMAGE POST TO TWITTER
if len(q.quote) + len(q.author) + 1 > 140 or roll():  # 4:10 chance to post image or >140 char
    print 'Image posting...'
    text2img.text2img(q.quote, q.author)

    fname = open("quote_img.png", 'rb')
    hashtags = '#motivational #quote '

    for name in q.author.split():
        hashtags += '#'
        hashtags += name
        hashtags += ' '

    print hashtags

    twitter.update_status_with_media(status=hashtags, media=fname)
    print 'complete'

# TEXT ONLY POST TO TWITTER
else:
    print 'Text posting...'
    combined_quote = q.quote
    combined_quote += '-'
    combined_quote += q.author

    if len(combined_quote) + len(" #quote #motivation") <= 140:  # add hash tags if enough space
        combined_quote += " #quote #motivation"
    elif len(combined_quote) + len(" #quote") <= 140:
        combined_quote += " #quote"

    twitter.update_status(status=combined_quote)