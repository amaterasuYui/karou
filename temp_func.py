def string_contain_all(texts, strings):
  
  return all(string in texts for string in strings)


def string_contain_any(texts, strings):
  
  return any(string in texts for string in strings)

def find_text_contain_all(texts, strings):
  
  return [text for text in texts if string_contain_all(text, strings)]
  
def save_to_text(file, *args):
  
  with open(file, "w", encoding = "utf-8") as handle:
    for string in args:
      print(string)
      handle.write(string + "\n")

def word_by_pos(token, stopwords, pos, filtered_length = 10, most_common_show = 10):
  import itertools
  from collections import Counter
  index, words = token.non_trivial_word(stopwords, filtered_length, pos)
  all_words = list(itertools.chain.from_iterable(words))
  all_words_cnt = Counter(all_words)
  
  print(all_words_cnt.most_common(most_common_show))
  
  return index, words, all_words, all_words_cnt

def substr_occurence(text_set, substr):
  return [text.lower().count(substr.lower()) for text in text_set]

def all_substr_occurence(text_set, substr_set):
  return {substr:substr_occurence(text_set, substr) for substr in substr_set}

def all_substr_occurence_by_base(base_set, substr_set):
  from collections import Counter
  def substr_occurence(base_set, substr):
    base_set = [list(map(lambda x: x.lower(), base)) for base in base_set]
    substr = substr.lower()
    return [Counter(base_text).get(substr) if substr in Counter(base_text) else int(0) in Counter(base_text) for base_text in base_set]
  return {substr:substr_occurence(base_set, substr) for substr in substr_set}


def word_distr_by_song(noun_occurence):
  import numpy as np
  return [(key, (np.array(item) != 0).sum()) for key, item in noun_occurence.items()]

def append_song_name(noun_occurence, song_name, song):
  return { key:sorted(list(zip(item, song_name, song)), key = lambda x:x[0], reverse = True) for key, item in noun_occurence.items()}
  
