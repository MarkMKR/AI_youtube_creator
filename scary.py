import combiner
import imgs
import os
import speach
import video_v2
import subtitles
from resize import resize_photo


img_path = 'scary_imgs'
img_search = '---'
resized_path = 'scary_resize_imgs'

temp_video_name = 'scary_temp_video'
temp_speach_name = 'scary_voice_audio.wav'

final_video_prefix = 'scary_'

text = """
South Korea and the US are set to conduct their biggest joint military exercises in five years, as tensions with North Korea escalate. The training, including amphibious drills and a computer-simulated command post exercise, will take place from March 13 to 23. The North is expected to respond with missile tests, viewing the exercises as an invasion rehearsal.
"""

# imgs.fetch_images(img_path, num=3, dir=img_path)

# if not os.listdir(resized_path):
resize_photo(path_inp=img_path, path_out=resized_path)

duration = speach.make_voice(text, filename=temp_speach_name)

video_v2.make_video(video_name=temp_video_name, duration=duration, img_path=img_path, resized_path=resized_path)

filename = combiner.combine_video(video_path=temp_video_name, voice_path=temp_speach_name, back_music_path="back_music/news2.mp3", prefix=final_video_prefix)

subtitles.make_subs(text, filename)