#-*- coding:utf-8 -*-
import tweepy

import key

auth = tweepy.OAuthHandler(key.CK, key.CS)
auth.set_access_token(key.AT, key.AS)
api = tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        screen_name = status.user.screen_name
        text = status.text
        text = str(status.text).replace("\n", "")
        print(screen_name)
        print(text)


word ="xxx"

stream = tweepy.Stream(auth, MyStreamListener())

while True:
    try:
        stream.filter(track=[word])
    except KeyboardInterrupt:
        stream.disconnect()
        break
    except Exception as e:
        stream.disconnect()
        print(e)