#!/usr/bin/python

import twython
import os

class TweetStreamer(twython.TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')

    def on_error(self, status_code, data):
        print status_code
        self.disconnect()

streamer = TweetStreamer(os.environ.get('TWITTER_KEY'),
                          os.environ.get('TWITTER_SECRET'),
                          os.environ.get('TWITTER_ACCESS_TOKEN'),
                          os.environ.get('TWITTER_ACCESS_STOKEN'))

streamer.statuses.filter(track = 'motivational')

