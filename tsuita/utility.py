import tweepy

class TweetAPI:
  
  def __init__(self, cred = None, proxy = None):
    
    if cred is None:
      cred = {
        "consumer_key": "44IrueNgOr4N5jUfDfYVRK183",
        "consumer_secret": "QtgvCuFExIfWuMqSko3LwklJPuWsMtlPXFMEJAB38AEElzLIW0",
        "access_token": "1116301268333412353-YqFx2DuV2XTzzr3Smb5QxVsXY0JSSO",
        "access_token_secret": "U7WL9D7xGf2OmKs21fgWXUc9ScOeBlJExF3mfLjPbmJix"
      }
    
    self._csm_key = cred.get("consumer_key")
    self._csm_scrt = cred.get("consumer_secret")
    self._acs_tk = cred.get("access_token")
    self._acs_tk_scrt = cred.get("access_token_secret")
    self._proxy = proxy
    self._auth = self._authorize()
    self._auth.set_access_token(self._acs_tk, self._acs_tk_scrt)
    
  def _authorize(self):
    return tweepy.OAuthHandler(self._csm_key, self._csm_scrt)
  
  def get_api(self):
    return tweepy.API(self._auth, proxy = self._proxy, wait_on_rate_limit = True)
  
    
    
    
    
