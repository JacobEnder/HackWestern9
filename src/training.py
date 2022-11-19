import cohere
from cohere.classify import Example
from youtube_transcript import captions_from_url
from transcript_sentiment import sentiment_from_phrases
dict_from_csv = {}

co = cohere.Client('SJrk3bWz9kHuqGfUEdDhDaCcJYFJdT8bYhowER6l')

def findToxicity(yt_code):
  url = "https://www.youtube.com/watch?v=" + yt_code

  # https://www.youtube.com/watch?v=eBSeCp__xhI&ab_channel=LawofAttractionCoaching - motivatoinal speech: positive

  response = co.classify(
    model='e6dd720d-e81e-44f8-b0c2-8c93a140b3ca-ft',
    inputs=captions_from_url(url)
  )

  return sentiment_from_phrases(response), response.classifications