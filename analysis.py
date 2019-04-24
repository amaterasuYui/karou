%load_ext autoreload
%autoreload 2
import pandas as pd
import numpy as np
import many_stop_words
from tsuita.twidata import SearchTwitter
from tsuita.bunseki import JaToken


flatten_ontime = SearchTwitter.load_twitters("data/teiji_twi.pickle")
# save twits to csv
ontime_df = pd.DataFrame(flatten_ontime)
ontime_df = ontime_df.assign(
  if_rt = np.where(ontime_df["text"].str.contains("RT @"),
  True, False))
non_rt = ontime_df[ontime_df.if_rt == False].sort_values("favorite_count", ascending = False)

dic_loc = "data/pn_ja.dic.txt"

filter_pos = ["記号", "助詞", "助動詞", "接頭詞", "連体詞", "接続詞"]
ontime_token = JaToken(non_rt.text.tolist(), 
                       dic_loc,
                       "わたし定時で帰ります",
                       filter_pos)

SearchTwitter.save_twitters(ontime_token, "data/ontime_token.pickle")

# get non trivial word list
stop_words = {"する", "られる", "さん", "てる", "ん","の", "彼", "彼女", "私", "わたし", "我々"}
stop_words = many_stop_words.get_stop_words("ja").union(stop_words)
ontime_words = ontime_token.non_trivial_word(stop_words)

# to check the worst and best comments
ontime_list = list(zip(ontime_token.score, 
                       ontime_token.score_set, 
                       ontime_token._text,
                       ontime_words))
ontime_list.sort(key = lambda x: x[0], reverse = False)



  
  
  
