from PIL import Image, ImageDraw
import math
from progressbar import ProgressBar
import sys
import Pixel

def rgbget(pix):
    pixel.getcolors(pix[0], pix[1], pix[2])
    

def processing(mode, pix, width, height, draw, image):
    print(str(mode + 1) + ". Image")
    pbar.start()
    for i in range(width):
        for j in range(height):
            pixel = Pixel.Pixel(*pix[i, j])
            draw.point((i, j), (pixel.modeget(mode)))
            pbar.update(i * j)
            del pixel
    image.save("Image" + str(mode + 1) + ".jpg", "JPEG")
    print('')

def negative(mode, pix, width, height, draw, image):
    print(str(mode + 1) + ". Negative")
    pbar.start()
    for i in range(width):
        for j in range(height):
            pixel = Pixel.Pixel(*pix[i, j])
            red, green, blue = pixel.modeget(mode)
            draw.point((i, j), (255-red, 255-green, 255-blue))
            pbar.update(i * j)
            del pixel
    image.save("Negative" + str(mode + 1) + ".jpg", "JPEG")
    print('')

def main():
    #IMAGE_NAME = sys.argv[1]

    pixel = Pixel.Pixel(0, 0, 0)
    modsquantity = pixel.getmodsquantity()
    
    selectedmods = []

    wrongoption = True
    while(wrongoption):
        print("-p, -P \t Positive mods;")
        print("-n, -N \t Negative mods;")
        print("-a, -A \t All mods;")
        global administration
        administration = list(input("Select mods: ").split(" "))
        select = administration[:-1]
        print(administration)
        if len(select)==1:
            select = select[0]
            print(select)
            if select.startswith("-"):
                modenumber = select[1:]
                if modenumber.isdigit():
                    selectedmods = list(range(int(modenumber) - 1))
                    wrongoption = False
                else:
                    print('Wrong option 1')
            elif select.endswith("-"):
                modenumber = select[:-1]
                if modenumber.isdigit():
                    selectedmods = list(range(int(modenumber) - 1, modsquantity))
                    wrongoption = False
                else:
                    print('Wrong option 2')
            elif select.find('-')!=-1:
                try:
                    modenumber = list(map(int, select.split("-")))
                    selectedmods = list(range(modenumber[0] - 1, modenumber[1]))
                    wrongoption = False
                except:
                    print('Wrong option 3')
            else:
                selectedmods.append(int(select) - 1)
                wrongoption = False
        else:
            selectedmods = list(map(int, select))
            #try:
            for i in range(len(selectedmods)):
                selectedmods[i]=selectedmods[i]-1
            wrongoption = False
            #except:
            #    print('Wrong option 4')
        print('----------------------------------------------------------------')

    del pixel


    for mode in selectedmods:
        image = Image.open("pp.jfif")
        
        draw = ImageDraw.Draw(image)
        width = image.size[0]
        height = image.size[1]

        global pbar
        pbar = ProgressBar(maxval=width * height)

        pix = image.load()

        if administration[-1]=='-p' or administration[-1]=='-P':
            processing(mode = mode, pix=pix, width = width, height = height, draw = draw, image = image)
        elif administration[-1]=='-n' or administration[-1]=='-N':    
            negative(mode = mode, pix=pix, width=width, height=height, draw=draw, image = image)
        elif administration[-1]=='-a' or administration[-1]=='-A':
            processing(mode = mode, pix=pix, width = width, height = height, draw = draw, image = image)
            negative(mode = mode, pix=pix, width=width, height=height, draw=draw, image = image)
            
        print('')

if __name__=='__main__':
    main()
