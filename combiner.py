import moviepy.editor as mp
import cv2
from pydub import AudioSegment
import datetime


def combine_video(video_path="temp_video", voice_path="voice-audio.wav", back_music_path="back_music/chill-tech.mp3", video_format="mp4", prefix=''):
    video_path = f'{video_path}.{video_format}'
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
    filename = f'{prefix}{str(ts)}_final.{video_format}'
    final.write_videofile(filename)

    return filename


if __name__ == "__main__":
    combine_video()