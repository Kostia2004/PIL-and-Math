from PIL import Image, ImageDraw
import math
from progressbar import ProgressBar
import sys
import Pixel

def rgbget(pix):
    pixel.getcolors(pix[0], pix[1], pix[2])
    

def processing(mode, pix, width, height, draw):
    for i in range(width):
        for j in range(height):
            pixel = Pixel.Pixel(*pix[i, j])
            draw.point((i, j), (pixel.modeget(mode)))
            pbar.update(i * j)
            del pixel

def negative(mode, pix, width, height, draw):
    for i in range(width):
        for j in range(height):
            pixel = Pixel.Pixel(*pix[i, j])
            red, green, blue = pixel.modeget(mode)
            draw.point((i, j), (255-red, 255-green, 255-blue))
            pbar.update(i * j)
            del pixel

def main():
    IMAGE_NAME = sys.argv[1]

    pixel = Pixel.Pixel(0, 0, 0)
    modsquantity = pixel.getmodsquantity()
    
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
            modenumber = select[:-1]
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

    del pixel


    for mode in selectedmods:
        image = Image.open(IMAGE_NAME)
        
        draw = ImageDraw.Draw(image)
        width = image.size[0]
        height = image.size[1]

        global pbar
        pbar = ProgressBar(maxval=width * height)

        pix = image.load()

        print(str(mode + 1) + ".")

        pbar.start()

        if mode%2==0:
            processing(mode = int(mode/2), pix=pix, width = width, height = height, draw = draw)
        else:
            negative(mode = int(mode//2), pix=pix, width=width, height=height, draw=draw)
        print('')
        image.save("Image" + str(mode + 1) + ".jpg", "JPEG")

if __name__=='__main__':
    main()
