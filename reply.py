# -*- coding: utf-8 -*-
#  このスクリプトは10分間隔で実行することを前提としています

import tweepy
import time

import key


auth = tweepy.OAuthHandler(key.CK, key.CS)
auth.set_access_token(key.AT, key.AS)

api = tweepy.API(auth, wait_on_rate_limit=True)

Twitter_ID = str(api.me().screen_name)

timeline = api.mentions_timeline()

nowTime = time.time()

for status in timeline:
    status_id = status.id
    screen_name = status.user.screen_name
    text = str(status.text).replace("\n", "")
    mentionTime = status.created_at.timestamp()
    if nowTime - mentionTime < 33000.0:  # 実行環境が標準時の場合は600.0にしてください
        try:
            reply_text = "@" + screen_name + " " + "テストリプライ"
            api.create_favorite(status.id)
            if str(status.in_reply_to_screen_name) == Twitter_ID and str(status.user.screen_name) != Twitter_ID:
                api.update_status(status=reply_text, in_reply_to_status_id=status_id)
            else:
                print("自分に返信を送っています")
        except Exception as e:
            print(e)
