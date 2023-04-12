# from moviepy.video.io.VideoFileClip import VideoFileClip



# def converter(filename):
#         with VideoFileClip(filename) as video:
#                 audio = video.audio
#                 audio.write_audiofile("sound.mp3")


# import os

# def converter(old_name, new_name):
#     os.rename(old_name, new_name)

# Example usage
# rename_file('vid.mp4', 'sound.mp3')


from pydub import AudioSegment


def converter(filename):
        sound = AudioSegment.from_file(filename, format="mp4")
        sound.export("sound.mp3", format="mp3")