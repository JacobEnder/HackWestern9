import pandas as pd
import cohere
from cohere.classify import Example
from youtube_transcript import single_captions_from_url
from transcript_sentiment import sentiment_from_phrases

co = cohere.Client('SJrk3bWz9kHuqGfUEdDhDaCcJYFJdT8bYhowER6l')

df = pd.read_csv('train2.csv')

data = []

toxic_count = 0
not_toxic_count = 0
for id, row in df.iterrows():
    toxic = row[1]
    text = row[2]
    if toxic <= 0.1 and not_toxic_count < 10000:
        data.append(Example(text, "positive"))
        not_toxic_count += 1
    elif toxic >= 0.5:
        data.append(Example(text, "negative"))
        toxic_count += 1
    if toxic_count > 5000 and not_toxic_count > 5000:
        break

inputs = [
  "These dumb democrats have their head up their butts",
  "I have so much love in my heart",
  "Mica is such an intelligent and kind young man",
  "Jaacob is such a silly jew"
]

andrew_tate_humiliates_logan_paul = 'https://www.youtube.com/watch?v=VI46EuYqt-g&ab_channel=ChrisWilliamson'


response = co.classify(
  model='large',
  inputs=inputs,
  #inputs=single_captions_from_url(andrew_tate_humiliates_logan_paul),
  examples=data
)

#print(single_captions_from_url(andrew_tate_humiliates_logan_paul))
print(sentiment_from_phrases(response))
