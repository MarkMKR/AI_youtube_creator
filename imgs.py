from google_images_search import GoogleImagesSearch
from dotenv import load_dotenv
import os

if os.path.exists(".env"):
    load_dotenv()
else:
    print(".env file missing, please create one with your API and CX")

# create an 'ims' sub directory if it doesn't already exists
if not os.path.exists('test-imgs/'):
    os.mkdir('test-imgs/')
spath = "test-imgs"

# Get env variables
DK = os.environ.get('DEVELOPER_KEY')
CX = os.environ.get('CX')
print(DK)

# custom progressbar function
def my_progressbar(url, progress):
    print(url + " " + progress + "%")


# create google images search - object
gis = GoogleImagesSearch(DK, CX, progressbar_fn=my_progressbar)


def fetch_images(searchfor):
    # using contextual mode (Curses)
    with GoogleImagesSearch(DK, CX) as gis:
        # define search params:
        _search_params = {"q": searchfor,
                          "num": 15,
                          "fileType": "jpg",
                          "imgType": "photo",
                          "rights": "cc_publicdomain"
                          }
        gis.search(search_params=_search_params, path_to_dir=spath)

    print("Finished!")


if __name__ == "__main__":
    fetch_images('cats')