from PIL import Image
import os

path_imgs = 'imgs'


def pc_resize():
    mean_height = 0
    mean_width = 0

    num_of_images = len(os.listdir(path_imgs))

    for file in os.listdir(path_imgs):
        im = Image.open(os.path.join(path_imgs, file))
        width, height = im.size
        mean_width += width
        mean_height += height

    mean_width = int(mean_width / num_of_images)
    mean_height = int(mean_height / num_of_images)

    for file in os.listdir(path_imgs):
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"):
            im = Image.open(os.path.join(path_imgs, file))

            width, height = im.size
            print(width, height)

            imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
            imResize.save(file, 'PNG', quality=95)

            print(im.filename.split('\\')[-1], " is resized")

def phone_resize():
    for file in os.listdir(path_imgs):
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"):
            im = Image.open(os.path.join(path_imgs, file))


            imResize.save(file, 'PNG', quality=95)

            print(im.filename.split('\\')[-1], " is resized")


phone_resize()