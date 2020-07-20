from PIL import Image, ImageDraw
import math
from progressbar import ProgressBar
import sys
import mods

modsquantity = 98

def rgbget(pixel):
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    s = int((r + g + b) // 3)
    return r, g, b, s

def processing(mode, width, height, pix, draw):
    for i in range(width):
        for j in range(height):
            r, g, b, s = rgbget(pix[i, j])
            draw.point((i, j), (mods.modeget(mode, r, g, b, s)))
            pbar.update(i * j)

def negative(mode, width, height, pix, draw):
    for i in range(width):
        for j in range(height):
            r, g, b, s = rgbget(pix[i, j])
            red, green, blue = mods.modeget(mode, r, g, b, s)
            draw.point((i, j), (255-red, 255-green, 255-blue))
            pbar.update(i * j)

def main():
    IMAGE_NAME = sys.argv[1]

    selectedmods = []

    wrongoption = True
    while(wrongoption):
        select = input("Select mods: ")
        if select.startswith("-"):
            modenumber = select[1:]
            if modenumber.isdigit():
                selectedmods = list(range(int(modenumber) - 1))
                wrongoption = False
            else:
                print('Wrong option')
        elif select.endswith("-"):
            modenumber = select[:1]
            if modenumber.isdigit():
                selectedmods = list(range(int(modenumber) - 1, modsquantity * 2))
                wrongoption = False
            else:
                print('Wrong option')
        elif select.find('-')!=-1:
            try:
                modenumber = list(map(int, select.split("-")))
                selectedmods = list(range(modenumber[0] - 1, modenumber[1]))
                wrongoption = False
            except:
                print('Wrong option')
        else:
            try:
                selectedmods = list(map(int, select.split(" ")))
                for i in range(len(selectedmods)):
                    selectedmods[i]=selectedmods[i]-1
                wrongoption = False
            except:
                print('Wrong option')


    for mode in selectedmods:
        image = Image.open(IMAGE_NAME)
        #image = Image.open("Original.jfif")

        draw = ImageDraw.Draw(image)
        width = image.size[0]
        height = image.size[1]

        global pbar
        pbar = ProgressBar(maxval=width * height)

        pix = image.load()

        print(str(mode + 1) + ".")

        pbar.start()

        if mode%2==0:
            processing(mode = int(mode/2), width = width, height = height, pix = pix, draw = draw)
        else:
            negative(mode=int(mode//2), width=width, height=height, pix=pix, draw=draw)
        print('')
        image.save("Image" + str(mode + 1) + ".jpg", "JPEG")

if __name__=='__main__':
    main()