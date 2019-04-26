%load_ext autoreload
%autoreload 2
import pandas as pd
import numpy as np
import many_stop_words
from tsuita.twidata import SearchTwitter
from tsuita.bunseki import JaToken


flatten_ontime = SearchTwitter.load_twitters("data/teiji_twi_2.pickle")
# save twits to csv
ontime_df = pd.DataFrame(flatten_ontime)
ontime_df = ontime_df.assign(
  if_rt = ontime_df["text"].str.contains("RT @"))
non_rt = ontime_df[ontime_df.if_rt == False].sort_values("favorite_count", ascending = False)

dic_loc = "data/pn_ja.dic.txt"

filter_pos = ["記号", "助詞", "助動詞", "接頭詞", "連体詞", "接続詞", "動詞", "副詞"]
replace_words = "わたし定時で帰ります|わた定"
ontime_token = JaToken(non_rt.text.tolist(), 
                       dic_loc,
                       replace_words,
                       filter_pos)

SearchTwitter.save_twitters(ontime_token, "data/ontime_token_2.pickle")





