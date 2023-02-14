import combiner
import imgs
import speach
import video_v2

text = """
    The veteran tech company is reorganising its advertising unit, which will lose more than half of the department by the end of the year.
    """

img_path = 'cats'

imgs.fetch_images(img_path, num=4, dir=img_path)

duration = speach.make_voice(text)

video_v2.make_video(duration=duration, img_path=img_path)

combiner.combine_video()