from youtube_transcript_api import YouTubeTranscriptApi
video_id = "dQw4w9WgXcQ"
transcript = YouTubeTranscriptApi.get_transcript(video_id)
full_text = " ".join([item['text'] for item in transcript])
print("Transcript:", full_text[:300])