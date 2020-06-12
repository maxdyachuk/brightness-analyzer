import requests
import os
from tqdm import tqdm
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup as bs


def is_url_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def extractor(url):
    soup = bs(requests.get(url).content, "html.parser")
    urlsOfImagess = []
    for img in tqdm(soup.find_all("img"), "Extracting images"):
        urlsOfImages = img.attrs.get("src")
        if not urlsOfImages:
            continue
        urlsOfImages = urljoin(url, urlsOfImages)
        try:
            pos = urlsOfImages.index("?")
            urlsOfImages = urlsOfImages[:pos]
        except ValueError:
            pass

        if is_url_valid(urlsOfImages):
            urlsOfImagess.append(urlsOfImages)
    return urlsOfImagess



def download(url, pathname):
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    response = requests.get(url, stream=True)
    file_size = int(response.headers.get("Content-Length", 0))
    filename = os.path.join(pathname, url.split("/")[-1])
    progress = tqdm(response.iter_content(1024), f"Uploading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress:
            f.write(data)
            progress.update(len(data))
    f.close()


def load(url, path):
    imgs = extractor(url)
    for img in imgs:
        download(img, path)
