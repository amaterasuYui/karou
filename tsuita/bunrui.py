#coding: utf-8

from gensim import corpora
from gensim.models.ldamodel import LdaModel
from gensim.models import CoherenceModel
import pyLDAvis
import pyLDAvis.gensim
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from scipy.misc import imread

class Topic:
  
  def __init__(self, doc_list):
    
    self.doc_list = doc_list
    self.dictionary = corpora.Dictionary(doc_list)
    self.corpus = self._get_corpus()
  
  def _get_corpus(self):
    
    return [self.dictionary.doc2bow(text) for text in self.doc_list]
    
  def ldamodel(self, num_topics, random_state = 24, passes = 20):
    
    return LdaModel(self.corpus, 
                    num_topics = num_topics,
                    id2word = self.dictionary,
                    random_state = random_state, 
                    passes = passes)

  @staticmethod                  
  def print_lda_topics(ldamodel, num_words = 6):
    topics = ldamodel.print_topics(num_words = num_words)
    
    for topic in topics:
      print(topic)
  
  def coherence_values(self, limit, start = 2, step = 2, random_state = 24, passes = 20):
    coherence_values = []
    model_list = []
    
    for num_topics in range(start, limit, step):
      model = LdaModel(self.corpus,
                       num_topics = num_topics,
                       id2word = self.dictionary,
                       random_state = random_state, 
                       passes = passes)
      model_list.append(model)
      coherencemodel = CoherenceModel(model = model, 
                                      texts = self.doc_list,
                                      dictionary = self.dictionary,
                                      coherence = "c_v")
      coherence_values.append(coherencemodel.get_coherence())
      print("Model with # of topics", num_topics, "has coherence:", coherencemodel.get_coherence(),
      end = "\r", flush = True)
      
    return model_list, coherence_values
    
  def visualize_lda(self, lda, save_to, sort_topics = False):
    lda_display = pyLDAvis.gensim.prepare(lda,
                                          self.corpus,
                                          self.dictionary,
                                          sort_topics = sort_topics)
    pyLDAvis.save_html(lda_display, save_to)
  
  @staticmethod
  def word_cloud(text_list, 
                 fpath,
                 save_to,
                 filter_words,
                 mask = None,
                 background_color = "white", 
                 max_words = 300, 
                 contour_width = 3, 
                 contour_color = "steelblue"):
    long_string = " ".join(word for sentence in text_list for word in sentence if word not in filter_words)
    
    if mask is not None:
      mask = imread(mask, flatten = True)
    
    wordcloud = WordCloud(background_color = background_color,
                          font_path = fpath,
                          width = 900,
                          height = 500,
                          mask = mask,
                          max_words = max_words,
                          contour_width = contour_width,
                          contour_color = contour_color).generate(long_string)
    wordcloud.to_file(save_to)
    plt.figure(figsize = (15, 12))
    plt.imshow(wordcloud, interpolation = "bilinear")
    plt.axis("off")
    plt.show()
    
    
