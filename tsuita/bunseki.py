import codecs
import re
from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.charfilter import *
from janome.tokenfilter import *
from collections import namedtuple, Counter

class JaToken:
  
  def __init__(self, text_list, dic, replace_word, pos_filter):
    
    
    self._raw_text = text_list
    self._text = self._all_text_process()
    self._dict = self._read_dict(dic)
    self.tokens = self._tokenize_elements(replace_word, pos_filter)
    self.score_set = self._sentiment_scores()
    self.score = self._element_tot_score()
  
  def text_process(self, text):
    
    #remove all urls
    text = re.sub(r"http\S+", "", text)
    
    #remove non japanese thinngs
    text = re.sub("[^\w\s]", "", text)
    
    #remove all the numbers
    text = re.sub("\d+", "", text)
    
    return text
  
  def _all_text_process(self):
    
    return [self.text_process(text) for text in self._raw_text]
      
  def _tokenize_elements(self, replace_word, pos_filter):
    
    tokenizer = Tokenizer()
    char_filters = [UnicodeNormalizeCharFilter(), RegexReplaceCharFilter(replace_word, "")]
    token_filters = [LowerCaseFilter(),  POSStopFilter(pos_filter)]
    t = Analyzer(char_filters, tokenizer, token_filters)
    return [list(t.analyze(text)) for text in self._text]
  
  def _read_dict(self, file):
    
    dic = {}
    with codecs.open(file, "r", "shift_jis") as handle:
      lines = handle.readlines()
      
      for line in lines:
        
        columns = line.split(":")
        dic[columns[0] + "-" + columns[2]] = float(columns[3])
        dic[columns[1] + "-" + columns[2]] = float(columns[3])
      
    return dic
  
  def sentiment_score(self, token):
    
    scores = []
    
    words = [t.base_form + "-" + t.part_of_speech.split(",")[0] for t in token 
              if t.part_of_speech.split(",")[0] 
              in ["動詞", "名詞", "形容詞", "副詞"]]
    for word in words:
      if word in self._dict:
        scores.append(self._dict.get(word))
    
    return scores
  
  def _sentiment_scores(self):
    
    return [self.sentiment_score(token) for token in self.tokens]
  
  def _element_tot_score(self):
    
    return [sum(scores) for scores in self.score_set]
  
  def non_trivial_word(self, stop_words, filter_length = 10):
    
    word_list = []
    index_list = []
    
    for index, sentence in enumerate(self.tokens):
      words = [token.base_form for token in sentence 
                      if token.base_form not in stop_words
                        and len(token.base_form) > 1
                        and not token.base_form.isdigit()]
      if len(words) >= filter_length and words not in word_list:
        word_list.append(words)
        index_list.append(index)
    return index_list, word_list

    
    
    
    
  
  
  
  
