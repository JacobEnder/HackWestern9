import cohere
from cohere.classify import Example
from youtube_transcript import captions_from_url
from transcript_sentiment import sentiment_from_phrases
import csv
import pandas as pd
dict_from_csv = {}

co = cohere.Client('SJrk3bWz9kHuqGfUEdDhDaCcJYFJdT8bYhowER6l')

def findToxicity(yt_code):
  url = "https://www.youtube.com/watch?v=" + yt_code
  print(url)
  df = pd.read_csv('train2.csv')

  datafile = open('toxic_no_emojis.csv', 'r')
  datareader = csv.reader(datafile, delimiter='<')
  data = []

  for id, row in df.iterrows():
      toxic = row[1]
      text = row[2]
      if toxic <= 0.1:
          data.append(Example(text, "positive"))
      elif toxic >= 0.5:
          data.append(Example(text, "negative"))

  for text, toxic in datareader:
    label = 'positive' if toxic == 'Not Toxic' else 'negative'
    data.append(Example(text, label))


  # https://www.youtube.com/watch?v=eBSeCp__xhI&ab_channel=LawofAttractionCoaching - motivatoinal speech: positive

  response = co.classify(
    model='medium',
    inputs=captions_from_url(url),
    examples=data
  )

  return sentiment_from_phrases(response)