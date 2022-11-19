from youtube_transcript import *
from training import findToxicity


example_url = "https://www.youtube.com/watch?v=pN3jRihVpGk&list=PLKiU8vyKB6ti1_rUlpZJFdPaxT04sUIoV&index=1"

#very toxic https://www.youtube.com/watch?v=UQ4VeJeDTH0&ab_channel=Imbrandonfarris

# Returns a list of captions containing 4-element arrays of
# [startTime, duration, prediction, confidence]
def classifyChunks(yt_code):
    url = "https://www.youtube.com/watch?v=" + yt_code
    chunks = grab_timestamps_from_url(url)
    classifications = findToxicity(yt_code)[1]

    for i in range(min(len(chunks), len(classifications))):
        chunks[i].append(classifications[i].prediction)
        chunks[i].append(classifications[i].confidence)

    return chunks


