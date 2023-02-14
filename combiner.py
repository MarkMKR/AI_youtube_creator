import moviepy.editor as mp
import cv2
from pydub import AudioSegment
import datetime


def combine_video(video_path="temp_video.mp4", voice_path="voice-audio.wav", back_music_path="back_music/chill-tech.mp3"):

    data = cv2.VideoCapture(video_path)
    frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = data.get(cv2.CAP_PROP_FPS)
    m_seconds = (frames / fps) * 1000

    print('mileseconds: ', m_seconds)

    back_music = AudioSegment.from_mp3(back_music_path) - 10
    cut_back = back_music[:m_seconds]
    cut_back.export("back-cut.mp3", format="mp3")
    audio = mp.AudioFileClip("back-cut.mp3")

    voice = mp.AudioFileClip(voice_path)
    final_audio = mp.CompositeAudioClip([voice, audio])
    video1 = mp.VideoFileClip(video_path)
    final = video1.set_audio(final_audio)

    ts = datetime.datetime.now().timestamp()
    final.write_videofile(str(ts) + "_final.mp4")


if __name__ == "__main__":
    combine_video()