import combiner
import imgs
import os
import speach
import video_v2
import subtitles
from resize import resize_photo



text = """
Meta has announced that it will launch a paid subscription service called Meta Verified, which allows Instagram and Facebook users to pay for a blue tick verification. The monthly subscription, costing $11.99 for web and $14.99 for iPhone users, will improve security and authenticity on the social media apps. The badges or "blue ticks" have been used as verification tools for high-profile accounts, and the paid subscription will give users increased visibility, protection from impersonators, and easier access to customer service.
"""

img_path = 'imgs'
img_search = '---'
resized_path = 'resize_imgs'

# imgs.fetch_images(img_path, num=3, dir=img_path)

# if not os.listdir(resized_path):
resize_photo(path_inp=img_path, path_out=resized_path)

duration = speach.make_voice(text)

video_v2.make_video(duration=duration, img_path=img_path, resized_path=resized_path)

filename = combiner.combine_video()

subtitles.make_subs(text, filename)