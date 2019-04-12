%load_ext autoreload
%autoreload 2
from tsuita.utility import TweetAPI
proxy = "https://sjd-entbc-001:80"
twi = TweetAPI(proxy = proxy)
api = twi.get_api()
