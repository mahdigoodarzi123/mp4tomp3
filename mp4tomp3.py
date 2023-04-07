from moviepy.video.io.VideoFileClip import VideoFileClip


with VideoFileClip("video.mp4") as video:
        audio = video.audio
        audio.write_audiofile("sound.mp3")
