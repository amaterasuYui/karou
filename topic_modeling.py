%load_ext autoreload
%autoreload 2
import pandas as pd
import numpy as np
import many_stop_words
from tsuita.twidata import SearchTwitter
from tsuita.bunseki import JaToken
from tsuita.bunrui import Topic
import warnings
warnings.filterwarnings("ignore")
from temp_func import *

ontime_token = SearchTwitter.load_twitters("data/perfe.pickle")
# get non trivial word list
stop_words = {"する", "られる", "さん", "てる", "ん","の", "彼", "彼女", "私","自分", "わたし", "我々"}
filter_words = {"中丸", "高", "吉", "ドラマ", "三谷", "くん", "人", "由里子", "向井", "理", "雄一", "ちゃん", "こと", "もの", "よう", "rt", "teiji", "watashi", "火曜", "どちら", "ふたり", "ない", "定時", "そう", "シシドカフカ", "カフカ", "内田", "有紀", "結衣", "あなた", "是枝", "晴人", "北斗", "美月", "山本", "松村", "松坂", "桃李", "放送", "perfectworldktv", "つぐみ", "長沢", "瀬戸", "康史", "gw", "菅田", "鮎川"}
stop_words = many_stop_words.get_stop_words("ja").union(stop_words)
stop_words = stop_words.union(filter_words)
index, ontime_words = ontime_token.non_trivial_word(stop_words, 10)

# to check the worst and best comments
ontime_list = list(zip(ontime_token.score, 
                       ontime_token.score_set, 
                       ontime_token._text))
ontime_list.sort(key = lambda x: x[0], reverse = False)
SearchTwitter.save_twitters((ontime_words, ontime_list), "data/perfe_strip.pickle")

# topic modeling
ontime_topic = Topic(ontime_words)
ontime_mdl, coherence_values = ontime_topic.coherence_values(20, start = 8)
mdl_score = list(zip(ontime_mdl, coherence_values))
mdl_score.sort(key = lambda score: score[1], reverse = True)
best_mdl = mdl_score[0][0]
Topic.print_lda_topics(best_mdl)
# word cloud
fpath = "C:\Windows\Fonts\msgothic.ttc"
save_to = "data/wordcloud.png"
filter_words = ["ため", "ところ", "いい", "多い", "みんな", "みたい", "良い", "とき", "たち"]
mask = "img/twitter_mask.png"
Topic.word_cloud(ontime_words, fpath, save_to, filter_words, mask = mask, max_words = 88, contour_width = 0)

#lda visulazie
save_to = "data/perfe_topic_visualize.html"
ontime_topic.visualize_lda(best_mdl, save_to)

# find twitter contain all the strings
topics_6_words = ["車椅子", "障害"]
topics_6_comments = find_text_contain_all(ontime_token._raw_text, topics_6_words)

topics_17_words = ["幸せ", "切ない"]
topics_17_comments = find_text_contain_all(ontime_token._raw_text, topics_17_words)

topics_8_words = ["好き", "演技"]
topics_8_comments = find_text_contain_all(ontime_token._raw_text, topics_8_words)



save_to_text("data/topics_representative_comments.txt",
              "Topic 6:", *topics_6_comments,
              "Topic 17:", *topics_17_comments,
              "Topic 8:", *topics_8_comments
             )
save_to_text("data/perfe_words_comments_top_10.txt",
*list(map(lambda x: x[2] + "\n\r", ontime_list[:10]))
)

save_to_text("data/perfe_best_comments_top_10.txt",
*list(map(lambda x: x[2] + "\n\r", ontime_list[-1:-10:-1])))

