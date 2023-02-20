import shutil

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


def fetch_images(searchfor, num=10, dir="imgs"):
    if not os.path.exists(dir + "\\"):
        os.mkdir(dir + "\\")
    spath = dir

    for filename in os.listdir(spath):
        file_path = os.path.join(spath, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    with GoogleImagesSearch(DK, CX) as gis:
        _search_params = {"q": searchfor,
                          "num": num,
                          "fileType": "jpg|png|jpeg",
                          "imgType": "photo",
                          # "rights": "cc_publicdomain"
                          }
        gis.search(search_params=_search_params, path_to_dir=spath)

    print("Finished!")


if __name__ == "__main__":
    fetch_images('biologic artificial heart', dir='imgs', num=30)