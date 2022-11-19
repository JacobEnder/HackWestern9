import cohere
from cohere.classify import Example
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript import single_captions_from_url
from transcript_sentiment import sentiment_from_phrases
import json

# 'https://www.youtube.com/shorts/UBaSmpNMu-8'
andrew_tate_humiliates_logan_paul = 'https://www.youtube.com/watch?v=UBaSmpNMu-8&list=PLKiU8vyKB6ti1_rUlpZJFdPaxT04sUIoV&index=1'

rise_and_grind = 'https://www.youtube.com/watch?v=8ZsN-dRZT_4'
 
example_url = "https://www.youtube.com/watch?v=pN3jRihVpGk&list=PLKiU8vyKB6ti1_rUlpZJFdPaxT04sUIoV&index=1"
# _id = example_url.split("=")[1].split("&")[0]
# transcript = YouTubeTranscriptApi.get_transcript(_id)
# with open(f'transcript.json', 'w', encoding='utf-8') as json_file:
#   json.dump(transcript, json_file)


co = cohere.Client('SJrk3bWz9kHuqGfUEdDhDaCcJYFJdT8bYhowER6l')

examples = [
  Example("The order came 5 days early", "positive"), 
  Example("The item exceeded my expectations", "positive"), 
  Example("I ordered more for my friends", "positive"), 
  Example("I would buy this again", "positive"), 
  Example("I would recommend this to others", "positive"), 
  Example("The package was damaged", "negative"), 
  Example("The order is 5 days late", "negative"), 
  Example("The order was incorrect", "negative"), 
  Example("I want to return my item", "negative"), 
  Example("The item\'s material feels low quality", "negative"), 
  Example("The product was okay", "neutral"), 
  Example("I received five items in total", "neutral"), 
  Example("I bought it from the website", "neutral"), 
  Example("I used the product this morning", "neutral"), 
  Example("The product arrived yesterday", "neutral"),
  Example("This amazing product is exactly what I wanted", "positive"),
  Example("This is a super product", "positive"),
]

inputs = [
  "This item was broken when it arrived",
  "The product is amazing",
  "The product was not too bad",
  "The product was alright, but the price was quite high. I don't think the value was there \
        and overall would recommend looking for alternative options.",
  "This item arrived 1 day late"
]

response = co.classify(
  model='medium',
  inputs=single_captions_from_url(rise_and_grind),
  examples=examples
)

print(sentiment_from_phrases(response.classifications))

# print(response.classifications)

