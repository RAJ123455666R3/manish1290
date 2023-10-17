import tweepy



api_key = "jOoLDXqLYrPuw7rGeVp449mce"
api_secret = "YqLhKPHhi6GXT6Iq1RwxZ5azXzkE14KwjxKSWONWXij8C1adF7"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAKoSqQEAAAAAlm8qt%2BKDH5ennAI2%2BOe1Xdsx6Vc%3DqAABnTddJwshwexkJZ7TCFqXGakLtnyZjNQDWAzxZqeHq61TM6"
access_token = "1708798262361141248-fmAy5MfdHrGaI3b6lEKsHt54khcVIH"
access_token_secret = "1VNCEt5GiZvNbl2YRWIbEElYlM3WvZKwaQcHoLqVFy4ws"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

client.create_tweet(text = "Hello Simplilearners")

