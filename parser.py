import requests as r
from bs4 import BeautifulSoup as bs

news_urls = [
    'https://edition.cnn.com/world'
]

def cnn():
    cnn_url = 'https://edition.cnn.com/world'
    domain = 'https://edition.cnn.com'
    resp = r.get(cnn_url)
    # file = open('index.html', 'w', newline='', encoding="utf-8")
    # file.write(resp.text)

    soup = bs(resp.text, 'lxml')

    con = soup.select_one(r"div[data-editable='items']")
    links = [domain + a['href'] for a in con.select("a.container__link")]
    print(links)

def main():
    cnn()


if __name__ == "__main__":
    main()