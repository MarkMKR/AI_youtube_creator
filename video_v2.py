from moviepy.editor import *
from resize import resize_photo


def make_video(video_name="temp_video", duration=60, img_path="imgs", resized_path="phone_imgs"):
    img_clips = []
    path_list = []

    if not os.listdir(resized_path):
        resize_photo(path_inp=img_path, path_out=resized_path)

    for image in os.listdir(resized_path):
        if image.endswith(".jpg") or image.endswith(".jpeg") or image.endswith("png"):
            path_list.append(os.path.join(resized_path, image))

    frame_duration = duration / len(path_list)

    for img_path in path_list:
        slide = ImageClip(img_path, duration=frame_duration)
        img_clips.append(slide)

    video_slides = concatenate_videoclips(img_clips, method='compose')
    video_slides.write_videofile(video_name + ".mp4", fps=60)


if __name__ == "__main__":
    make_video()