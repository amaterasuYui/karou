%load_ext autoreload
%autoreload 2
from kashi.kashi import Lyrics
from tsuita.bunseki import JaToken
from temp_func import *
import pandas as pd
import many_stop_words
import pickle

aimer_url = "https://www.uta-net.com/artist/11629/"
aimer = Lyrics(aimer_url)
aimyon_url = "https://www.uta-net.com/artist/17598/"
aimyon = Lyrics(aimyon_url)
pickle.dump(aimer, open("data/aimer.pickle", "wb"))
pickle.dump(aimyon, open("data/aimyon.pickle", "wb"))



# get token and corpus for kashi
aimer = pickle.load(open("data/aimer.pickle", "rb"))
dic_loc = "data/pn_ja.dic.txt"
filter_pos = ["記号", "助詞", "助動詞", "接頭詞", "連体詞", "接続詞"]
aimer_lyrics = list(map(lambda x: x[3], aimer.song_pack))
aimer_token = JaToken(aimer_lyrics, 
                       dic_loc,
                       "1",
                       filter_pos)

stop_words = {"する", "られる", "さん", "てる", "ん","の", "dont", "こと",
"よう", "まま", "そう", "あなた", "もの", "いつ", "いつか", "ため",
"いる", "なる", "れる", "れる", "ない", "くい", "mum", "いい", "ほしい",
"しまう", "ある", "くれる", "できる", "来る", "ゆく", "行く", "言う", "せる", "くる", "いく",
"日々", "今日", "明日"}
stop_words = many_stop_words.get_stop_words("ja", "en").union(stop_words)

# noun analysis
aimer_noun = word_by_pos(aimer_token, stop_words, "名詞", filtered_length = 0, most_common_show = 20)
aimer_verb = word_by_pos(aimer_token, stop_words, "動詞", filtered_length = 0, most_common_show = 20)
aimer_adj = word_by_pos(aimer_token, stop_words, "形容詞", filtered_length = 0, most_common_show = 20)
aimer_all = word_by_pos(aimer_token, stop_words, "", filtered_length = 0, most_common_show = 20)
aimerW = [pd.DataFrame(aimer_noun[3].most_common(), columns = ["word", "cnt"]),
          pd.DataFrame(aimer_verb[3].most_common(), columns = ["word", "cnt"]),
          pd.DataFrame(aimer_adj[3].most_common(), columns = ["word", "cnt"])]

aimer_viz = [
   aimerW,
   aimer_all,
   pd.DataFrame(aimer.song_pack, columns = ["title", "lyricist", "composer", "lyrics"])]
pickle.dump(
aimer_viz,
open("data/aimer_viz.pickle", "wb")
)

aimerW_big_tb = pd.concat([aimerW[0].assign(pos = "noun"), 
                           aimerW[1].assign(pos = "vern"),
                           aimerW[2].assign(pos = "adj")])
aimerW_big_tb.to_csv("data/aimer_cnt.csv", encoding = "utf-8")


