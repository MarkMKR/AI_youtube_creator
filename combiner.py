# import moviepy.editor as mpe
#
# video = mpe.VideoFileClip('mygeneratedvideo.mp4')
# background = mpe.AudioFileClip('back_music/chill-tech.mp3')
# voice = mpe.AudioFileClip('audio-4.wav')
# print('start')
# if(video.audio is not None):
#     new_audioclip = mpe.CompositeAudioClip([video.audio, background])
# else:
#     new_audioclip = mpe.CompositeAudioClip([voice, background])
# print('almost')
# final_clip = video.set_audio(background)

import moviepy.editor as mp
import cv2
from pydub import AudioSegment


data = cv2.VideoCapture('output_video.mp4')

# count the number of frames
frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
fps = data.get(cv2.CAP_PROP_FPS)
m_seconds = (frames / fps) * 1000
print('mileseconds: ', m_seconds)

back_music = AudioSegment.from_mp3("back_music/chill-tech.mp3") - 10
cut_back = back_music[:m_seconds]
cut_back.export("cut.mp3", format="mp3")

audio = mp.AudioFileClip("cut.mp3")
voice = mp.AudioFileClip("audio-4.wav")
final_audio = mp.CompositeAudioClip([voice, audio])
video1 = mp.VideoFileClip("output_video.mp4")
final = video1.set_audio(final_audio)

final.write_videofile("output.mp4")
