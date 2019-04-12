import tweepy

consumer_key = "44IrueNgOr4N5jUfDfYVRK183"
consumer_secret = "QtgvCuFExIfWuMqSko3LwklJPuWsMtlPXFMEJAB38AEElzLIW0"
access_token = "1116301268333412353-YqFx2DuV2XTzzr3Smb5QxVsXY0JSSO"
access_token_secret = "U7WL9D7xGf2OmKs21fgWXUc9ScOeBlJExF3mfLjPbmJix"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,
                 proxy = "https://sjd-entbc-001:80",
                 wait_on_rate_limit = True)

api.search(q = "#逃げ恥", lang = "ja", result_type = "mixed", count = 51)


