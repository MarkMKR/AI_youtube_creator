import cv2
import pandas as pd
from moviepy.editor import VideoFileClip

frame_words_storage = []


def frames_opencv(filename):
    video = cv2.VideoCapture(filename)
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)

    return frame_count


def pipeline(frame):
    global frame_words_storage

    try:
        text = str(next(frame_words_storage)[1][0])
        font = cv2.FONT_HERSHEY_DUPLEX
        textsize = cv2.getTextSize(text, font, 2, 3)[0]

        text_w, text_h = textsize

        margin_bottom_y = 120

        textX = int((frame.shape[1] - textsize[0]) / 2)
        textY = int(textsize[1] + margin_bottom_y)

        padding = 25

        start_x = (textX - padding)
        start_y = (textY + padding)
        end_x = int((textX + text_w + padding))
        end_y = int((textY - text_h - padding))

        cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), (0, 0, 0), -1)

        cv2.putText(frame, text, (textX, textY), font, 2, (255, 255, 255), 3)
    except StopIteration:
        pass
    return frame


def imgs_subs():
    img = cv2.imread('resize_imgs/1676103270-6391.png')

    font = cv2.FONT_HERSHEY_DUPLEX
    text = "10 provinces. The longer one"

    textsize = cv2.getTextSize(text, font, 2, 3)[0]

    text_w, text_h = textsize

    margin_bottom_y = 120

    textX = int((img.shape[1] - textsize[0]) / 2)
    textY = int(textsize[1] + margin_bottom_y)

    padding = 25

    start_x = (textX - padding)
    start_y = (textY + padding)
    end_x = int((textX + text_w + padding))
    end_y = int((textY - text_h - padding))

    cv2.rectangle(img, (start_x, start_y), (end_x, end_y), (0, 0, 0), -1)

    cv2.putText(img, text, (textX, textY), font, 2, (255, 255, 255), 3)

    cv2.imwrite('test.jpg', img)


def lookahead(iterable):
    it = iter(iterable)
    last = next(it)
    for val in it:
        yield last, False
        last = val
    yield last, True


def words_splitter(text):
    text = ' '.join(text.splitlines())
    words_arr = []
    temp_words = ''
    for i, last in lookahead(text.split(' ')):
        i = i.rstrip().lstrip()
        if len(temp_words):
            temp_words += " " + i
        else:
            temp_words += i

        if " " in temp_words and len(temp_words) > 25:
            temp_words = temp_words[:-len(i) - 1]
            words_arr.append(temp_words.rstrip().lstrip())
            temp_words = i
        elif last:
            words_arr.append(temp_words.rstrip().lstrip())

    print(words_arr)
    print(len(words_arr))
    return words_arr


def make_subs(text, video_name):
    global frame_words_storage

    chunked_text = words_splitter(text)

    frames = frames_opencv(video_name)
    text_chunks = len(chunked_text)

    per_chunk = int(frames / text_chunks)

    subs = [ch for ch in chunked_text for _ in range(per_chunk)]

    frame_words_storage = pd.DataFrame(subs).iterrows()

    video = VideoFileClip(video_name)
    out_video = video.fl_image(pipeline)
    out_video.write_videofile("subs_" + video_name, audio=True)

    return subs


if __name__ == "__main__":
    text = """
    Satellite images reveal two massive cracks near the Turkish-Syrian border after 7.7 magnitude earthquake hit Kahramanmaras and affected 10 provinces. The longer one is 300km long, caused by the first of two powerful earthquakes, which claimed over 31,600 lives.
    """
    filename = '1676834711.4079_final.mp4'

    make_subs(text, filename)
