import os
import moviepy.video.io.ImageSequenceClip
import PIL
import os
import os.path
from PIL import Image

f = r'imgs'
for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    img = img.resize((1280, 980))
    img.save(f_img)

imgs_len = len(os.listdir(f))

image_folder='imgs'
fps=1
duration=10


image_files = [os.path.join(image_folder, img)
               for img in os.listdir(image_folder)
               if img.endswith(".png")]
clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=1, durations=[duration for i in range(imgs_len)])
clip.write_videofile('my_video.mp4')