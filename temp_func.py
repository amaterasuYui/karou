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
  

  
