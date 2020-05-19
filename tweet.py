#-*- coding:utf-8 -*-
import tweepy

import key

auth = tweepy.OAuthHandler(key.CK, key.CS)
auth.set_access_token(key.AT, key.AS)
api = tweepy.API(auth)


def main():
    api.update_status("テストツイート")


if __name__ == '__main__':
    main()