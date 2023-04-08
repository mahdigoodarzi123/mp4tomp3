from moviepy.video.io.VideoFileClip import VideoFileClip



def converter(filename):
        with VideoFileClip(filename) as video:
                audio = video.audio
                audio.write_audiofile("sound.mp3")

