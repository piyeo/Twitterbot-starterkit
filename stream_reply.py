#-*- coding:utf-8 -*-
import tweepy

import key

auth = tweepy.OAuthHandler(key.CK, key.CS)
auth.set_access_token(key.AT, key.AS)
api = tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        status_id = status.id
        screen_name = status.user.screen_name
        reply_text = "@" + screen_name + " " + "テストリプライ"
        if str(status.in_reply_to_screen_name) == Twitter_ID:
            api.create_favorite(status_id)
            if str(screen_name) != Twitter_ID:
                api.update_status(status=reply_text, in_reply_to_status_id=status_id)
            else:
                print("自分に返信を送っています")


Twitter_ID = str(api.me().screen_name)
filter_ID = "@" + Twitter_ID

stream = tweepy.Stream(auth, MyStreamListener())

while True:
    try:
        stream.filter(track=[filter_ID])
    except KeyboardInterrupt:
        stream.disconnect()
        break
    except Exception as e:
        stream.disconnect()
        print(e)