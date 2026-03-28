from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id: str) -> str:
    """
    Takes a YouTube video ID (e.g. UZDiGooFs54)
    and returns the full transcript as a clean string.
    """
    if not video_id or video_id.strip() == "":
        raise ValueError("Video ID cannot be empty!")

    video_id = video_id.strip()  # remove accidental spaces

    ytt = YouTubeTranscriptApi()
    fetched = ytt.fetch(video_id)

    # Join all text chunks into one clean string
    full_transcript = " ".join([chunk.text for chunk in fetched])

    return full_transcript