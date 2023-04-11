from moviepy.video.io.VideoFileClip import VideoFileClip



def converter(filename):
        with VideoFileClip(filename) as video:
                audio = video.audio
                audio.write_audiofile("sound.mp3")


# import os

# def converter(old_name, new_name):
#     os.rename(old_name, new_name)

# Example usage
# rename_file('vid.mp4', 'sound.mp3')