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

# word distribution analysis
aimer = pickle.load(open("data/aimer.pickle", "rb"))
aimer_all = pickle.load(open("data/aimer_viz.pickle", "rb"))[1]
song = [song_set[3] for song_set in aimer.song_pack]
noun_top = pd.read_csv("data/aimer_noun_20.csv")
noun_top_substr = noun_top.word.tolist()
noun_word_occur_by_song = all_substr_occurence_by_base(aimer_all[1], noun_top_substr)
word_distr = word_distr_by_song(noun_word_occur_by_song)
word_distr.sort(key = lambda x:x[1], reverse = True)
noun_word_occur_by_song = append_song_name(noun_word_occur_by_song, 
list(map(lambda x: x[0], aimer.song_pack)),
list(map(lambda x: x[3], aimer.song_pack)))

# by adj
adj_top = pd.read_csv("data/aimer_adj_20.csv")
adj_top_substr = adj_top.word.tolist()
adj_word_occur_by_song = all_substr_occurence_by_base(aimer_all[1], adj_top_substr)
adj_word_distr = word_distr_by_song(adj_word_occur_by_song)
adj_word_distr.sort(key = lambda x:x[1], reverse = True)
adj_word_occur_by_song = append_song_name(adj_word_occur_by_song, 
list(map(lambda x: x[0], aimer.song_pack)),
list(map(lambda x: x[3], aimer.song_pack)))



