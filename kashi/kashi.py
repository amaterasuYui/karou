import requests
import re
from bs4 import BeautifulSoup

class Lyrics:
  lyrics_site = "https://www.uta-net.com"
  
  def __init__(self, artist_url):
    
    self.artist_url = artist_url
    self.song_pack = self._song_pack()
  
  def _get_song_text(self, soup, *argv):
    text = []
    for ele in soup.find_all(*argv):
      text.append(ele.text)
    return text
    
  def _get_lyrics_url(self, soup, *argv):
    url = []
    for ele in soup.find_all(*argv):
      url.append(ele.a.get("href"))
    return url
  
  def _get_lyrics(self):
    lyrics = []
    req = requests.get(self.artist_url)
    soup = BeautifulSoup(req.text, "html.parser")
    lyrics_url = self._get_lyrics_url(soup, "td",{"class": "td1"})
    
    for url in lyrics_url:
      song_url = self.lyrics_site + url
      lyrics_req = requests.get(song_url)
      lyric_soup = BeautifulSoup(lyrics_req.text, "html.parser")
      lyrics.append(
        re.sub('\u3000|<br/>|</br>|<br>|</div>|<div id="kashi_area" itemprop="text">', 
        " ", str(lyric_soup.find("div", {"id": "kashi_area"})))
        )
    return lyrics
    
  def _song_pack(self):
    req = requests.get(self.artist_url)
    soup = BeautifulSoup(req.text, "html.parser")
    
    title = self._get_song_text(soup, "td", {"class": "td1"})
    lyricist = self._get_song_text(soup, "td", {"class": "td3"})
    composer = self._get_song_text(soup, "td", {"class": "td4"})
    lyrics = self._get_lyrics()
    
    return list(zip(title, lyricist, composer, lyrics))
    
