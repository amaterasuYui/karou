from collections import defaultdict
class SearchTwitter:
  
  def __init__(self, api, query, lang, cnt):
    
    self._api = api
    self._query = query
    self._lang = lang
    self._cnt = cnt
    self._first_tweets = self._get_first_tweets()
  
  def _get_first_tweets(self):
    return self._api.search(q = self._query, 
                            lang = self._lang, 
                            count = self._cnt)
    
  def get_all_tweets(self, lit):
    
    all_tweets = self._first_tweets
    for i in range(lit):
      tweets = self._api.search(q = self._query, 
                                lang = self._lang, 
                                count = self._cnt,
                                max_id = all_tweets.max_id - 1)
      if len(tweets) > 0:
        all_tweets.extend(tweets)
        print("Finished ", i + 1, "out of", lit, "searches", flush = True, end = "\r")
      else:
        break
    return all_tweets
  
  @staticmethod
  def flatten_tweets(tweets, user_info, *args):
    flatten_tweet = defaultdict(list)
    
    for tweet in tweets:
      tweet_json = tweet._json
      for info in user_info:
        flatten_tweet["user-" + info].append(tweet_json["user"][info])
      for attr in args:
        flatten_tweet[attr].append(tweet_json[attr])
        
    return flatten_tweet
        
      
    
      
    
