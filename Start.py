import ImageLoader
import ImageAnalyzer
from PIL import Image
import Tests


def main():
    with open("urls.xml", "rt") as urls:
        for url in urls:
            ImageLoader.load(url, "images")
        ImageAnalyzer.sortImages("images")
    #Tests.testsForBrightness("testImages")


if __name__ == '__main__':
    main()