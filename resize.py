import os, shutil
from PIL import Image


def resize_photo(p_height=1920, p_width=1080, path_inp='imgs', path_out='resize_imgs'):
    for filename in os.listdir(path_out):
        file_path = os.path.join(path_out, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    for file in os.listdir(path_inp):
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png") \
                or file.endswith('.JPG') or file.endswith('.JPEG') or file.endswith("PNG"):
            try:
                im = Image.open(os.path.join(path_inp, file))
                width, height = im.size
                new_width = int((width * p_height) / height)
                centered_box = 0
                gap = new_width - p_width
                if gap > 2:
                    centered_box = int(gap / 2)
                imResize = im.resize((new_width, p_height))
                imResize = imResize.crop((0 + centered_box, 0, p_width + centered_box, p_height))
                imResize.save(os.path.join(path_out, file), 'PNG', quality=100)

                print(im.filename.split('\\')[-1], " is resized")
            except Exception as e:
                print(file, ' scipped')



def resize_photo_pc(p_height=1080, p_width=1920, path_inp='imgs', path_out='resize_imgs'):
    for filename in os.listdir(path_out):
        file_path = os.path.join(path_out, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    for file in os.listdir(path_inp):
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png") \
                or file.endswith('.JPG') or file.endswith('.JPEG') or file.endswith("PNG"):
            try:
                im = Image.open(os.path.join(path_inp, file))
                width, height = im.size

                new_height = int((height * p_width) / width)
                new_width = int((width * p_height) / height)
                background = Image.new('RGB', (p_width, p_height), (255, 255, 255))

                if height >= width:
                    y_offset = 0
                    x_offset = int((p_width - new_width) / 2)
                    background.paste(im.resize((new_width, p_height)), (x_offset, y_offset))
                else:
                    x_offset = 0
                    y_offset = int((p_height - new_height) / 2)
                    background.paste(im.resize((p_width, new_height)), (x_offset, y_offset))

                background.save(os.path.join(path_out, file), 'png', quality=100)

                print(im.filename.split('\\')[-1], " is resized")
            except Exception as e:
                print(file, ' scipped')



if __name__ == "__main__":
    resize_photo()
