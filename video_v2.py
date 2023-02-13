from moviepy.editor import *
from PIL import Image
from resize import resize_for_phone

img_clips = []
path_list=[]
path_imgs = 'imgs'
phone_imgs = 'phone_imgs'

if not os.listdir(phone_imgs):
    resize_for_phone()

#accessing path of each image
for image in os.listdir(phone_imgs):
    if image.endswith(".jpg") or image.endswith(".jpeg") or image.endswith("png"):
        path_list.append(os.path.join(phone_imgs, image))

#creating slide for each image
for img_path in path_list:
    slide = ImageClip(img_path, duration=2)
    img_clips.append(slide)

# breakpoint()
#concatenating slides
video_slides = concatenate_videoclips(img_clips, method='compose')
#exporting final video
video_slides.write_videofile("output_video.mp4", fps=60)