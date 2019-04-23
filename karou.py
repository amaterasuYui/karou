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
ontime = SearchTwitter(api, "#わたし定時で帰ります", "ja", 200)
ontime_tweets = ontime.get_all_tweets(900)

user_info = ["id", "screen_name", "description"]

flatten_ontime = SearchTwitter.flatten_tweets(ontime_tweets,
                                         user_info,
                                         "id",
                                         "created_at",
                                         "text",
                                         "favorite_count")
ontime_df = pd.DataFrame(flatten_ontime)
ontime_df = ontime_df.assign(
  if_rt = np.where(ontime_df["text"].str.contains("RT @"),
  True, False))
ontime_df.to_csv("data/teiji.csv")

  
  

