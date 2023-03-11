from moviepy.editor import *

def make_video(video_name="temp_video", duration=60, img_path="imgs", resized_path="resize_imgs"):
    img_clips = []
    path_list = []

    for image in os.listdir(resized_path):
        if image.endswith(".jpg") or image.endswith(".jpeg") or image.endswith(".png") \
                or image.endswith('.JPG') or image.endswith('.JPEG') or image.endswith("PNG"):
            path_list.append(os.path.join(resized_path, image))

    frame_duration = duration / len(path_list)

    for img_path in path_list:
        slide = ImageClip(img_path, duration=frame_duration)
        img_clips.append(slide)

    video_slides = concatenate_videoclips(img_clips, method='compose')
    video_slides.write_videofile(f"{video_name}.mp4", fps=60)


if __name__ == "__main__":
    make_video()