#!/usr/bin/python
# -*- coding: utf-8 -*-

# Python libs
import os
import logging
import random

# Third-party dependencies
import twython
from forismatic import Forismatic
import text2img

# Twitter settings
twitter = twython.Twython(os.environ.get('TWITTER_KEY'),
                          os.environ.get('TWITTER_SECRET'),
                          os.environ.get('TWITTER_ACCESS_TOKEN'),
                          os.environ.get('TWITTER_ACCESS_STOKEN'))

# Initializing manager
f = Forismatic()
q = f.get_quote()

# IMAGE POST TO TWITTER
tweet_chars = len(q.quote) + len(q.author) + 3

if tweet_chars > 140:
    print 'Image posting...'

    text2img.text2img(q.quote, q.author)

    fname = open("quote_img.png", 'rb')

    phrases = [
        '',
        'Exactly.',
        '🙌',
        '👏👏',
        'try it',
        'the little things',
        'I love this',
        'always',
        'say it',
        '👌',
        'Remember this',
        'Seriously',
        'Amen',
        'hit me hard',
        'Yes',
        'This',
        'Yup',
        'So true',
        'This is for you',
        'feelin this one',
        'for sure',
        'def for u',
        'yes',
        'totally agree',
        'agree',
        '100%',
        'share this',
        'share if you agree #100%',
        'believe it',
        'srs',
        'try this',
        'for u',
        'luv this',
        'love it',
    ]

    if tweet_chars > 200:
        hashtags = 'worth the read'
    else:
        hashtags = random.choice(phrases)

    hashtags += ' '

    for name in q.author.split():
        hashtags += '#'
        hashtags += name.encode('utf-8')
        hashtags += ' '

    print hashtags

    twitter.update_status_with_media(status=hashtags, media=fname)

# TEXT ONLY POST TO TWITTER
else:
    print 'Text posting...'

    combined_quote = q.quote.stip()
    if q.author != '':
        combined_quote += ' - '
        combined_quote += q.author

    twitter.update_status(status=combined_quote)