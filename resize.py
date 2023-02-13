import os
from PIL import Image

path_imgs = 'imgs'
phone_imgs = 'phone_imgs'

def resize_for_phone(p_heiht=1920, p_width=1080):
    for file in os.listdir(path_imgs):
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"):
            try:
                im = Image.open(os.path.join(path_imgs, file))
                width, height = im.size
                new_width = int((width * p_heiht) / height)
                centered_box = 0
                gap = new_width - p_width
                if gap > 2:
                    centered_box = int(gap / 2)
                imResize = im.resize((new_width, p_heiht))
                imResize = imResize.crop((0 + centered_box, 0, p_width + centered_box, p_heiht))
                imResize.save(os.path.join(phone_imgs, file), 'PNG', quality=100)

                print(im.filename.split('\\')[-1], " is resized")
            except Exception as e:
                print(file, ' scipped')

def resize_for_pc():
    pass