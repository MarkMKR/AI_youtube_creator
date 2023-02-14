from google_images_search import GoogleImagesSearch
from dotenv import load_dotenv
import os

if os.path.exists(".env"):
    load_dotenv()
else:
    print(".env file missing, please create one with your API and CX")


DK = os.environ.get('DEVELOPER_KEY')
CX = os.environ.get('CX')


def my_progressbar(url, progress):
    print(url + " " + progress + "%")

gis = GoogleImagesSearch(DK, CX, progressbar_fn=my_progressbar)


def fetch_images(searchfor, num=15, dir="imgs"):
    if not os.path.exists(dir + "\\"):
        os.mkdir(dir + "\\")
    spath = dir

    with GoogleImagesSearch(DK, CX) as gis:
        _search_params = {"q": searchfor,
                          "num": num,
                          "fileType": "jpg|png|jpeg",
                          "imgType": "photo",
                          "rights": "cc_publicdomain"
                          }
        gis.search(search_params=_search_params, path_to_dir=spath)

    print("Finished!")


if __name__ == "__main__":
    fetch_images('cats', dir='cats')