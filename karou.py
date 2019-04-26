%load_ext autoreload
%autoreload 2
from tsuita.utility import TweetAPI
from tsuita.twidata import SearchTwitter
import pandas as pd
import numpy as np
from inspect import getsource

proxy = "https://sjd-entbc-001:80"
twi = TweetAPI(proxy = proxy)
api = twi.get_api()
search_query = ["#わたし定時で帰ります", "#わた定"]
search_query = " OR ".join(search_query)
ontime = SearchTwitter(api, search_query, "ja", 100)
ontime_tweets = ontime.get_all_tweets(1000)
user_info = \
["id", 
"screen_name", 
"description", 
"location", 
"friends_count",
"followers_count"]
flatten_ontime = SearchTwitter.flatten_tweets(ontime_tweets,
                                              user_info,
                                              "id",
                                              "created_at",
                                              "text",
                                              "favorite_count")
# save twits to pickle
SearchTwitter.save_twitters(flatten_ontime, "data/teiji_twi_2.pickle")
# save twits to csv
ontime_df = pd.DataFrame(flatten_ontime)
ontime_df = ontime_df.assign(
  if_rt = ontime_df["text"].str.contains("RT @"))

ontime_df.to_csv("data/teiji_2.csv")
