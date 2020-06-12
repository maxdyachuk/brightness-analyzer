from PIL import Image, ImageStat
import os
from os import listdir


def sortImages(pathOfImages):
    try:
        os.path.isdir(pathOfImages)
    except:
        print("Error with path of images")
        return
    images = listdir(pathOfImages)
    with open("results.xml", "wt") as f:
        for image in images:
            try:
                value = brightness(pathOfImages + "/" + image)
                if value <= 25:
                    levelOfBrightness = 1
                elif value <= 50:
                    levelOfBrightness = 2
                elif value <= 75:
                    levelOfBrightness = 3
                elif value <= 100:
                    levelOfBrightness = 4
                elif value <= 125:
                    levelOfBrightness = 5
                elif value <= 150:
                    levelOfBrightness = 6
                elif value <= 175:
                    levelOfBrightness = 7
                elif value <= 200:
                    levelOfBrightness = 8
                elif value <= 225:
                    levelOfBrightness = 9
                else:
                    levelOfBrightness = 10
                f.write(image + " have " + str(levelOfBrightness) + " brightness level\n")
            except:
                f.write(image + " not correct\n")
    f.close()


def brightness(image):
    im = Image.open(image).convert('L')
    stat = ImageStat.Stat(im)
    return stat.mean[0]