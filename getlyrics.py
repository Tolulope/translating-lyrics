import requests
from bs4 import BeautifulSoup
import goslate

token = "IjNTOX1ZKhZ3zJIdnvgJB1s_1FNFXcBYgsGpDIupoRGG7dVQI3QEAwVu-bR-WwvV"
base_url = "http://api.genius.com"
headers = {'Authorization': 'Bearer IjNTOX1ZKhZ3zJIdnvgJB1s_1FNFXcBYgsGpDIupoRGG7dVQI3QEAwVu-bR-WwvV'}

song_title = "moule frites"
artist_name = "Stromae"

def lyrics_from_song_api_path(song_api_path):
  song_url = base_url + song_api_path
  response = requests.get(song_url, headers=headers)
  json = response.json()
  path = json["response"]["song"]["path"]
  #gotta go regular html scraping... come on Genius
  page_url = "http://genius.com" + path
  page = requests.get(page_url)
  html = BeautifulSoup(page.text, "html.parser")
  #remove script tags that they put in the middle of the lyrics
  [h.extract() for h in html('script', 'a')]
  #at least Genius is nice and has a tag called 'lyrics'!
  lyrics = html.find("lyrics")
  extra = html.find_all("a", class_="referent")
  texts = lyrics.findAll(text=True)
  print(texts)

  for text in texts:
      print text

  translate(texts)


def translate(texts):
        gs = goslate.Goslate()
        for t in texts:
            tran = gs.translate(t, "en")
            print tran





def main():
    search_url = base_url + "/search?q=" + song_title
    data = song_title
    response = requests.get(search_url, headers=headers)
    json = response.json()
    body = json["response"]["hits"]
    for hit in json["response"]["hits"]:
        if hit["result"]["primary_artist"]["name"] == artist_name:
            song_info = hit
            #if song_info:
            song_api_path = hit["result"]["api_path"]
            printed_lyrics = lyrics_from_song_api_path(song_api_path)
            print (printed_lyrics)
            break
            print ("Yaaaaaas!")
        break



if __name__ == "__main__":
        main()







