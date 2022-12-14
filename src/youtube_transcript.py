# Return various strings representing a transcript of a YouTube video, referenced by URL. Uses 
# youtube-transcript-api. 

from youtube_transcript_api import YouTubeTranscriptApi

example_url = "https://www.youtube.com/watch?v=pN3jRihVpGk&list=PLKiU8vyKB6ti1_rUlpZJFdPaxT04sUIoV&index=1"

def transcript_object_from_url(url):
    id = url.split('=')[1].split('&')[0]
    return YouTubeTranscriptApi.get_transcript(id)

def full_transcript_from_url(url):
    full_text = ''
    for caption in transcript_object_from_url(url):
        full_text += caption['text'] + ' '
    return full_text

def captions_from_url(url):
    """Returns list of strings, each containing the text of a single caption"""
    transcript = transcript_object_from_url(url)
    for i in range(len(transcript)):
        transcript[i]['text'] = transcript[i]['text'].replace("[\xa0__\xa0]", " fucking ")
    count = 0
    trans = []
    for i in range(len(transcript)):
        count += 1
        if (count % 3 == 0 and i < len(transcript) - 3) :
            trans.append(transcript[i]['text'] + transcript[i + 1]['text'] + transcript[i + 2]['text'])
            count = 0
        
    return trans

def grab_timestamps_from_url(url):
    transcript = transcript_object_from_url(url)
    count=0
    stamps=[]
    step = 3
    i = 0
    while i < len(transcript):
        chunk_time = 0
        if (i < len(transcript) - 3): 
            chunk_time = (transcript[i+2]['duration'] + transcript[i+2]['start']) - transcript[i]['start']
        if (chunk_time != 0):
            stamps.append([transcript[i]['start'],chunk_time])
            count+=1
        i += step
    return stamps
    

