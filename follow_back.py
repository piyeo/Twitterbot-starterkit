#-*- coding:utf-8 -*-
import tweepy

import key


def main():
    auth = tweepy.OAuthHandler(key.CK, key.CS)
    auth.set_access_token(key.AT, key.AS)

    api = tweepy.API(auth)

    follower_id = api.followers_ids()
    follow_id = api.friends_ids()
    not_followed_user_id = set(follower_id + follow_id) ^ set(follow_id)

    try:
        for user_id in not_followed_user_id:
            api.create_friendship(user_id)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()