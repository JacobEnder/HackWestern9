### Our Hack Western 9 Project

## What it is

(Insert title here) is a Chrome extension designed to allow users to detect bias and toxicity in YouTube videos that they watch. Users can analyze their videos for skewed language and content, and should they desire (for example, for children), users can skip sections of their videos that our classifier deems toxic or profane.

## How it works

Using a custom-trained Cohere classifier, we fetch custom or auto-generated YouTube captions based on a video's ID and analyze it for bias. The transcript is then split into "chunks", which are aggregates of roughly 3 consecutive captions. We compute an average "toxicity" score for a video by taking a weighted average of our classifier's toxicity ratings with respect to the classifier's confidence in each of those ratings. To create a readable, user-friendly scale, this data is then normalized to a custom distribution, which we feel makes the results more intuitive for users.

## Stack

The backend of this app was built in `Python`, with Flask linking our frontend and backend. To detect bias and toxicity in videos, we used a custom `Cohere` language classifier trained on approximately 3,000 examples. The frontend was written with `TypeScript` and `React`, making use of `Vite` to allow our app to function as Chrome extension. We used `youtube_transcript_api` to pull transcripts for each YouTube video.

