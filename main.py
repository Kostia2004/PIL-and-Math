from PIL import Image, ImageDraw
import math

for k in range(172, 175):

    image = Image.open("Original.jpeg")

    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]

    pix = image.load()

    #mode = int(input())
    mode = k

    for i in range(width):
      for j in range(height):
        r = pix[i, j][0]
        g = pix[i, j][1]
        b = pix[i, j][2]
        if mode==1:
            s = int((r + g + b) // 3)
            draw.point((i, j),(s, s, s))
    #black and white
        elif mode==2:
            s = int((r+g+b)//3)
            if s<50:
                draw.point((i, j),(0, 0, 0))
            else:
                draw.point((i, j),(255, 255, 255))
        elif mode==3:
            s = int((r+g+b)//3)
            if s<70:
                draw.point((i, j),(0, 0, 0))
            else:
                draw.point((i, j),(255, 255, 255))
        elif mode==4:
            s = int((r+g+b)//3)
            if s<100:
                draw.point((i, j),(0, 0, 0))
            else:
                draw.point((i, j),(255, 255, 255))
        elif mode==5:
            s = int((r+g+b)//3)
            if s<127:
                draw.point((i, j),(0, 0, 0))
            else:
                draw.point((i, j),(255, 255, 255))
        elif mode==6:
            s = int((r+g+b)//3)
            if s<150:
                draw.point((i, j),(0, 0, 0))
            else:
                draw.point((i, j),(255, 255, 255))
        elif mode==7:
            s = int((r+g+b)//3)
            if s<200:
                draw.point((i, j),(0, 0, 0))
            else:
                draw.point((i, j),(255, 255, 255))
    #black and sepia
        elif mode==8:
            s = int((r+g+b)//3)
            if s<50:
                draw.point((i, j),(0, 0, 0))
            else:
                draw.point((i, j),(s, s, s))
        elif mode==9:
            s = int((r+g+b)//3)
            if s<70:
                draw.point((i, j),(0, 0, 0))
            else:
                draw.point((i, j),(s, s, s))
        elif mode==10:
            s = int((r+g+b)//3)
            if s<100:
                draw.point((i, j),(0, 0, 0))
            else:
                draw.point((i, j),(s, s, s))
        elif mode==11:
            s = int((r+g+b)//3)
            if s<127:
                draw.point((i, j),(0, 0, 0))
            else:
                draw.point((i, j),(s, s, s))
        elif mode==12:
            s = int((r+g+b)//3)
            if s<150:
                draw.point((i, j),(0, 0, 0))
            else:
                draw.point((i, j),(s, s, s))
        elif mode==13:
            s = int((r+g+b)//3)
            if s<200:
                draw.point((i, j),(0, 0, 0))
            else:
                draw.point((i, j),(s, s, s))
    #Black and color
        elif mode==14:
            s = int((r+g+b)//3)
            if s<50:
                draw.point((i, j),(0, 0, 0))
            else:
                draw.point((i, j),(r, g, b))
        elif mode==15:
            s = int((r+g+b)//3)
            if s<70:
                draw.point((i, j),(0, 0, 0))
            else:
                draw.point((i, j),(r, g, b))
        elif mode==16:
            s = int((r+g+b)//3)
            if s<100:
                draw.point((i, j),(0, 0, 0))
            else:
                draw.point((i, j),(r, g, b))
        elif mode==17:
            s = int((r+g+b)//3)
            if s<127:
                draw.point((i, j),(0, 0, 0))
            else:
                draw.point((i, j),(r, g, b))
        elif mode==18:
            s = int((r+g+b)//3)
            if s<150:
                draw.point((i, j),(0, 0, 0))
            else:
                draw.point((i, j),(r, g, b))
        elif mode==19:
            s = int((r+g+b)//3)
            if s<200:
                draw.point((i, j),(0, 0, 0))
            else:
                draw.point((i, j),(r, g, b))
    #Negative
        elif mode==20:
            draw.point((i, j),(255-r, 255-g, 255-b))
    #Red
        elif mode==21:
            draw.point((i, j),(r, 0, 0))
        elif mode==22:
            draw.point((i, j),(2*r, g, b))
    #Green
        elif mode==23:
            draw.point((i, j),(0, g, 0))
        elif mode==24:
            draw.point((i, j),(r, 2*g, b))
    #Blue
        elif mode==25:
            draw.point((i, j),(0, 0, b))
        elif mode==26:
            draw.point((i, j),(r, g, 2*b))
    #Hell (math)
        elif mode==27:
            draw.point((i, j),(math.ceil(r**(g/130)), math.ceil(g**(b/130)), math.ceil(b**(r/130))))
        elif mode==28:
            draw.point((i, j),(math.ceil(r**1.3), math.ceil(g**1.4), math.ceil(b**1.3)))
        elif mode==29:
            draw.point((i, j),(math.ceil((255-r)**1), math.ceil((255-g)**1), math.ceil((255-b)**1.3)))
        elif mode==30:
            draw.point((i, j),(math.ceil(r**(b/130)), math.ceil(g**(r/130)), math.ceil(b**(g/130))))
        elif mode==31:
            draw.point((i, j),(math.ceil(r**(g/130)), math.ceil(g**(b/130)), math.ceil(b**(r/130))))
        elif mode==32:
            draw.point((i, j),(math.ceil(r**(g/90)), math.ceil(g**(b/90)), math.ceil(b**(r/90))))
        elif mode==33:
            draw.point((i, j),(math.ceil(r**1.3), math.ceil(g**1.3), math.ceil(b**1.4)))
        elif mode==34:
            draw.point((i, j),(math.ceil((255-r)**1.6), math.ceil((255-g)**1.6), math.ceil((255-b)**1.8)))
        elif mode==35:
            draw.point((i, j),(math.ceil(r**(b/130)), math.ceil(g**(r/130)), math.ceil(b**(math.sqrt(g%10)))))
        elif mode==36:
            draw.point((i, j),(math.ceil(r**(g/130)), math.ceil(g**(math.sqrt(b%10))), math.ceil(b**(r/130))))
        elif mode==37:
            draw.point((i, j),(math.ceil(r**(math.sqrt(g%10))), math.ceil(g**(math.sqrt(b/130))), math.ceil(b**(r/130))))
        elif mode==38:
            draw.point((i, j),(math.ceil(math.sin(r)*255), math.ceil(math.sin(g)*255), math.ceil(math.sin(b)*255)))
        elif mode==39:
            draw.point((i, j),(math.ceil(math.cos(r)*255), math.ceil(math.cos(g)*255), math.ceil(math.cos(b)*255)))
        elif mode==40:
            draw.point((i, j),(math.ceil(math.tan(r)*255), math.ceil(math.tan(g)*255), math.ceil(math.tan(b)*255)))
        elif mode==41:
            draw.point((i, j),(math.ceil(math.sin(r)*255), math.ceil(math.cos(g)*255), math.ceil(math.tan(b)*255)))
        elif mode==42:
            draw.point((i, j),(math.ceil(math.sin(r)*255), g, b))
        elif mode==43:
            draw.point((i, j),(r, math.ceil(math.sin(g)*255), b))
        elif mode==44:
            draw.point((i, j),(r, g, math.ceil(math.sin(b)*255)))
        elif mode==45:
            draw.point((i, j),(math.ceil(math.cos(r)*255), g, b))
        elif mode==46:
            draw.point((i, j),(r, math.ceil(math.cos(g)*255), b))
        elif mode==47:
            draw.point((i, j),(r, g, math.ceil(math.cos(b)*255)))
        elif mode==48:
            draw.point((i, j),(math.ceil(math.tan(r)*255), g, b))
        elif mode==49:
            draw.point((i, j),(r, math.ceil(math.tan(g)*255), b))
        elif mode==50:
            draw.point((i, j),(r, g, math.ceil(math.tan(b)*255)))
        elif mode==51:
            draw.point((i, j),(r*g%255, g*b%255, b*r%255))
        elif mode==52:
            draw.point((i, j),(r*b%255, g*r%255, b*g%255))
        elif mode==53:
            draw.point((i, j),(b, r, g))
        elif mode==54:
            draw.point((i, j),(g, b, r))
        elif mode==55:
            draw.point((i, j),(r, b, g))
        elif mode==56:
            draw.point((i, j),(b, g, r))
        elif mode==57:
            draw.point((i, j),(g, r, b))
        elif mode==58:
            draw.point((i, j),(math.ceil(math.tan(r)*r), math.ceil(math.tan(g)*g), math.ceil(math.tan(b)*b)))
        elif mode==59:
            draw.point((i, j),(math.ceil(math.sin(r)*r), math.ceil(math.sin(g)*g), math.ceil(math.sin(b)*b)))
        elif mode==60:
            draw.point((i, j),(math.ceil(math.cos(r)*r), math.ceil(math.cos(g)*g), math.ceil(math.cos(b)*b)))
        elif mode==58:
            draw.point((i, j),(math.ceil(math.tan(r)*g), math.ceil(math.tan(g)*b), math.ceil(math.tan(b)*r)))
        elif mode==59:
            draw.point((i, j),(math.ceil(math.sin(r)*g), math.ceil(math.sin(g)*b), math.ceil(math.sin(b)*r)))
        elif mode==60:
            draw.point((i, j),(math.ceil(math.cos(r)*g), math.ceil(math.cos(g)*b), math.ceil(math.cos(b)*r)))
        elif mode==61:
            draw.point((i, j),(math.ceil(math.tan(r)*b), math.ceil(math.tan(g)*r), math.ceil(math.tan(b)*g)))
        elif mode==62:
            draw.point((i, j),(math.ceil(math.sin(r)*b), math.ceil(math.sin(g)*r), math.ceil(math.sin(b)*g)))
        elif mode==63:
            draw.point((i, j),(math.ceil(math.cos(r)*b), math.ceil(math.cos(g)*r), math.ceil(math.cos(b)*g)))
        elif mode==64:
            draw.point((i, j),(math.ceil(math.tan(g)*r), math.ceil(math.tan(b)*g), math.ceil(math.tan(r)*b)))
        elif mode==65:
            draw.point((i, j),(math.ceil(math.sin(g)*r), math.ceil(math.sin(b)*g), math.ceil(math.sin(r)*b)))
        elif mode==66:
            draw.point((i, j),(math.ceil(math.cos(g)*r), math.ceil(math.cos(b)*g), math.ceil(math.cos(r)*b)))
        elif mode==67:
            draw.point((i, j),(math.ceil(math.tan(b)*r), math.ceil(math.tan(r)*g), math.ceil(math.tan(g)*b)))
        elif mode==68:
            draw.point((i, j),(math.ceil(math.sin(b)*r), math.ceil(math.sin(r)*g), math.ceil(math.sin(g)*b)))
        elif mode==69:
            draw.point((i, j),(math.ceil(math.cos(b)*r), math.ceil(math.cos(r)*g), math.ceil(math.cos(g)*b)))    
        elif mode==70:
            draw.point((i, j),(255-math.ceil(r**(g/130)), 255-math.ceil(g**(b/130)), 255-math.ceil(b**(r/130))))
        elif mode==71:
            draw.point((i, j),(255-math.ceil(r**1.3), 255-math.ceil(g**1.4), 255-math.ceil(b**1.3)))
        elif mode==72:
            draw.point((i, j),(255-math.ceil((255-r)**1), 255-math.ceil((255-g)**1), 255-math.ceil((255-b)**1.3)))
        elif mode==73:
            draw.point((i, j),(255-math.ceil(r**(b/130)), 255-math.ceil(g**(r/130)), 255-math.ceil(b**(g/130))))
        elif mode==74:
            draw.point((i, j),(255-math.ceil(r**(g/130)), 255-math.ceil(g**(b/130)), 255-math.ceil(b**(r/130))))
        elif mode==75:
            draw.point((i, j),(255-math.ceil(r**(g/90)), 255-math.ceil(g**(b/90)), 255-math.ceil(b**(r/90))))
        elif mode==76:
            draw.point((i, j),(255-math.ceil(r**1.3), 255-math.ceil(g**1.3), 255-math.ceil(b**1.4)))
        elif mode==77:
            draw.point((i, j),(255-math.ceil((255-r)**1.6), 255-math.ceil((255-g)**1.6), 255-math.ceil((255-b)**1.8)))
        elif mode==78:
            draw.point((i, j),(255-math.ceil(r**(b/130)), 255-math.ceil(g**(r/130)), 255-math.ceil(b**(math.sqrt(g%10)))))
        elif mode==79:
            draw.point((i, j),(255-math.ceil(r**(g/130)), 255-math.ceil(g**(math.sqrt(b%10))), 255-math.ceil(b**(r/130))))
        elif mode==80:
            draw.point((i, j),(255-math.ceil(r**(math.sqrt(g%10))), 255-math.ceil(g**(math.sqrt(b/130))), 255-math.ceil(b**(r/130))))
        elif mode==81:
            draw.point((i, j),(255-math.ceil(math.sin(r)*255), 255-math.ceil(math.sin(g)*255), 255-math.ceil(math.sin(b)*255)))
        elif mode==82:
            draw.point((i, j),(255-math.ceil(math.cos(r)*255), 255-math.ceil(math.cos(g)*255), 255-math.ceil(math.cos(b)*255)))
        elif mode==83:
            draw.point((i, j),(255-math.ceil(math.tan(r)*255), 255-math.ceil(math.tan(g)*255), 255-math.ceil(math.tan(b)*255)))
        elif mode==84:
            draw.point((i, j),(255-math.ceil(math.sin(r)*255), 255-math.ceil(math.cos(g)*255), 255-math.ceil(math.tan(b)*255)))
        elif mode==85:
            draw.point((i, j),(255-math.ceil(math.sin(r)*255), 255-g, 255-b))
        elif mode==86:
            draw.point((i, j),(255-r, 255-math.ceil(math.sin(g)*255), 255-b))
        elif mode==87:
            draw.point((i, j),(255-r, 255-g, 255-math.ceil(math.sin(b)*255)))
        elif mode==88:
            draw.point((i, j),(255-math.ceil(math.cos(r)*255), 255-g, 255-b))
        elif mode==89:
            draw.point((i, j),(255-r, 255-math.ceil(math.cos(g)*255), 255-b))
        elif mode==90:
            draw.point((i, j),(255-r, 255-g, 255-math.ceil(math.cos(b)*255)))
        elif mode==91:
            draw.point((i, j),(255-math.ceil(math.tan(r)*255), 255-g, 255-b))
        elif mode==92:
            draw.point((i, j),(255-r, 255-math.ceil(math.tan(g)*255), 255-b))
        elif mode==93:
            draw.point((i, j),(255-r, 255-g, 255-math.ceil(math.tan(b)*255)))
        elif mode==94:
            draw.point((i, j),(255-r*g%255, 255-g*b%255, 255-b*r%255))
        elif mode==95:
            draw.point((i, j),(255-r*b%255, 255-g*r%255, 255-b*g%255))
        elif mode==96:
            draw.point((i, j),(255-b, 255-r, 255-g))
        elif mode==97:
            draw.point((i, j),(255-g, 255-b, 255-r))
        elif mode==98:
            draw.point((i, j),(255-r, 255-b, 255-g))
        elif mode==99:
            draw.point((i, j),(255-b, 255-g, 255-r))
        elif mode==100:
            draw.point((i, j),(255-g, 255-r, 255-b))
        elif mode==101:
            draw.point((i, j),(255-math.ceil(math.tan(r)*r), 255-math.ceil(math.tan(g)*g), math.ceil(math.tan(b)*b)))
        elif mode==102:
            draw.point((i, j),(255-math.ceil(math.sin(r)*r), 255-math.ceil(math.sin(g)*g), math.ceil(math.sin(b)*b)))
        elif mode==103:
            draw.point((i, j),(255-math.ceil(math.cos(r)*r), 255-math.ceil(math.cos(g)*g), math.ceil(math.cos(b)*b)))
        elif mode==104:
            draw.point((i, j),(255-math.ceil(math.tan(r)*g), 255-math.ceil(math.tan(g)*b), math.ceil(math.tan(b)*r)))
        elif mode==105:
            draw.point((i, j),(255-math.ceil(math.sin(r)*g), 255-math.ceil(math.sin(g)*b), math.ceil(math.sin(b)*r)))
        elif mode==106:
            draw.point((i, j),(255-math.ceil(math.cos(r)*g), 255-math.ceil(math.cos(g)*b), math.ceil(math.cos(b)*r)))
        elif mode==107:
            draw.point((i, j),(255-math.ceil(math.tan(r)*b), 255-math.ceil(math.tan(g)*r), math.ceil(math.tan(b)*g)))
        elif mode==108:
            draw.point((i, j),(255-math.ceil(math.sin(r)*b), 255-math.ceil(math.sin(g)*r), math.ceil(math.sin(b)*g)))
        elif mode==109:
            draw.point((i, j),(255-math.ceil(math.cos(r)*b), 255-math.ceil(math.cos(g)*r), math.ceil(math.cos(b)*g)))
        elif mode==110:
            draw.point((i, j),(255-math.ceil(math.tan(g)*r), 255-math.ceil(math.tan(b)*g), math.ceil(math.tan(r)*b)))
        elif mode==111:
            draw.point((i, j),(255-math.ceil(math.sin(g)*r), 255-math.ceil(math.sin(b)*g), math.ceil(math.sin(r)*b)))
        elif mode==112:
            draw.point((i, j),(255-math.ceil(math.cos(g)*r), 255-math.ceil(math.cos(b)*g), math.ceil(math.cos(r)*b)))
        elif mode==113:
            draw.point((i, j),(255-math.ceil(math.tan(b)*r), 255-math.ceil(math.tan(r)*g), math.ceil(math.tan(g)*b)))
        elif mode==114:
            draw.point((i, j),(255-math.ceil(math.sin(b)*r), 255-math.ceil(math.sin(r)*g), math.ceil(math.sin(g)*b)))
        elif mode==115:
            draw.point((i, j),(255-math.ceil(math.cos(b)*r), 255-math.ceil(math.cos(r)*g), math.ceil(math.cos(g)*b)))
        elif mode==116:
            s = (r+g+b)//3
            draw.point((i, j),(s**2, s, 1))
        elif mode==117:
            s = (r+g+b)//3
            draw.point((i, j),(s, s**2, 1))
        elif mode==118:
            s = (r+g+b)//3
            draw.point((i, j),(1, s**2, s))
        elif mode==119:
            s = (r+g+b)//3
            draw.point((i, j),(s**2, 1, s))
        elif mode==120:
            s = (r+g+b)//3
            draw.point((i, j),(s, 1, s**2))
        elif mode==121:
            s = (r+g+b)//3
            draw.point((i, j),(1, s, s**2))
        elif mode==122:
            s = (r+g+b)//3
            draw.point((i, j),(s**2, s, b))
        elif mode==123:
            s = (r+g+b)//3
            draw.point((i, j),(s, s**2, b))
        elif mode==124:
            s = (r+g+b)//3
            draw.point((i, j),(r, s**2, s))
        elif mode==125:
            s = (r+g+b)//3
            draw.point((i, j),(s**2, g, s))
        elif mode==126:
            s = (r+g+b)//3
            draw.point((i, j),(s, g, s**2))
        elif mode==127:
            s = (r+g+b)//3
            draw.point((i, j),(r, s, s**2))
        elif mode==128:
            draw.point((width-i, height-j),(r, g, b))
        elif mode==129:
            draw.point((width-i, j),(r, g, b))
        elif mode==130:
            draw.point((i, height-j),(r, g, b))
        elif mode==131:
            draw.point((width-2*i, height-2*j),(r, g, b))
        elif mode==132:
            draw.point((i, height-2*j),(r, g, b))
        elif mode==133:
            draw.point((width-2*i, j),(r, g, b))
        elif mode==134:
            draw.point((width//2-i, height//2-j),(r, g, b))
        elif mode==135:
            draw.point((i, height//2-j),(r, g, b))
        elif mode==136:
            draw.point((width//2-i, j),(r, g, b))
        elif mode==137:
            draw.point((width%(i+1), height%(j+1)),(r, g, b))
        elif mode==138:
            draw.point((width%(i+1), j),(r, g, b))
        elif mode==139:
            draw.point((i, height%(j+1)),(r, g, b))
        elif mode==140:
            draw.point((j, i),(r, g, b))
        elif mode==141:
            draw.point((width-j, height-i),(r, g, b))
        elif mode==142:
            draw.point((height-j, width-i),(r, g, b))
        elif mode==143:
            draw.point((i**2, j**2),(r, g, b))
        elif mode==144:
            draw.point((i**2, j),(r, g, b))
        elif mode==145:
            draw.point((i, j**2),(r, g, b))
        elif mode==146:
            draw.point((i, math.sqrt(j)),(r, g, b))
        elif mode==147:
            draw.point((math.sqrt(i), j),(r, g, b))
        elif mode==148:
            draw.point((i**2, math.sqrt(j)),(r, g, b))
        elif mode==149:
            draw.point((math.sqrt(i), j**2),(r, g, b))
        elif mode==150:
            if not 110<i<160 and not 40<j<110:
                draw.point((i, j),(255, 255, 255))
        elif mode==151:
            if 110<i<160 and 40<j<110:
                draw.point((i, j),(255, 255, 255))
        elif mode==152:
            if not(100<i<150 and 40<j<110):
                draw.point((i, j),(255, 255, 255))
        elif mode==153:
            if not(100<i<150 and 40<j<110):
                draw.point((i, j),(255, 255, 255))
            elif i==125 or j==75:
                draw.point((i, j),(255, 255, 255))
        elif mode==154:
            if not(100<i<150 and 40<j<110):
                draw.point((i, j),(255, 255, 255))
            elif i==125 or j==75:
                draw.point((i, j),(255, 255, 255))
            else:
                draw.point((i, j),(r, g, 2*b))
        elif mode==155:
            if not(100<i<150 and 40<j<110) and not(10<i<60 and 10<j<80):
                draw.point((i, j),(255, 255, 255))
            elif (i==125 or j==75) or (i==35 or j==45):
                draw.point((i, j),(255, 255, 255))
            else:
                draw.point((i, j),(r, g, 2*b))
        elif mode==156:
            if not(100<i<150 and 40<j<110) and not(10<i<60 and 0<j<70) and not(190<i<240 and 80<j<150):
                draw.point((i, j),(255, 255, 255))
            elif (i==125 or j==75) or (i==35 or j==25) or (i==205 or j==115):
                draw.point((i, j),(255, 255, 255))
            else:
                draw.point((i, j),(r, g, 2*b))
        elif mode==157:
            if not(100<i<150 and 40<j<110):
                draw.point((i, j),(255, 255, 0))
            elif i==125 or j==75:
                draw.point((i, j),(255, 255, 0))
            else:
                draw.point((i, j),(r, g, 2*b))
        elif mode==158:
            if not(100<i<150 and 40<j<110) and not(10<i<60 and 10<j<80):
                draw.point((i, j),(255, 255, 0))
            elif (i==125 or j==75) or (i==35 or j==45):
                draw.point((i, j),(255, 255, 0))
            else:
                draw.point((i, j),(r, g, 2*b))
        elif mode==159:
            if not(100<i<150 and 40<j<110) and not(10<i<60 and 0<j<70) and not(190<i<240 and 80<j<150):
                draw.point((i, j),(255, 255, 0))
            elif (i==125 or j==75) or (i==35 or j==25) or (i==205 or j==115):
                draw.point((i, j),(255, 255, 0))
            else:
                draw.point((i, j),(r, g, 2*b))
        elif mode==160:
            if not(100<i<150 and 40<j<110):
                draw.point((i, j),(255, 205, 0))
            elif i==125 or j==75:
                draw.point((i, j),(255, 205, 0))
            else:
                draw.point((i, j),(r, g, 2*b))
        elif mode==161:
            if not(100<i<150 and 40<j<110) and not(10<i<60 and 10<j<80):
                draw.point((i, j),(255, 205, 0))
            elif (i==125 or j==75) or (i==35 or j==45):
                draw.point((i, j),(255, 255, 0))
            else:
                draw.point((i, j),(r, g, 2*b))
        elif mode==162:
            if not(100<i<150 and 40<j<110) and not(10<i<60 and 0<j<70) and not(190<i<240 and 80<j<150):
                draw.point((i, j),(255, 205, 0))
            elif (i==125 or j==75) or (i==35 or j==25) or (i==205 or j==115):
                draw.point((i, j),(255, 205, 0))
            else:
                draw.point((i, j),(r, g, 2*b))
        elif mode==163:
            if not(100<i<150 and 40<j<110):
                draw.point((i, j),(2*r, g, 0))
            elif i==125 or j==75:
                draw.point((i, j),(2*r, g, 0))
            else:
                draw.point((i, j),(r, g, 2*b))
        elif mode==164:
            if not(100<i<150 and 40<j<110) and not(10<i<60 and 10<j<80):
                draw.point((i, j),(2*r, g, 0))
            elif (i==125 or j==75) or (i==35 or j==45):
                draw.point((i, j),(2*r, g, 0))
            else:
                draw.point((i, j),(r, g, 2*b))
        elif mode==165:
            if not(100<i<150 and 40<j<110) and not(10<i<60 and 0<j<70) and not(190<i<240 and 80<j<150):
                draw.point((i, j),(2*r, g, 0))
            elif (i==125 or j==75) or (i==35 or j==25) or (i==205 or j==115):
                draw.point((i, j),(2*r, g, 0))
            else:
                draw.point((i, j),(r, g, 2*b))
        elif mode==166:
            if not(100<i<150 and 40<j<110):
                draw.point((i, j),(r, 0, 0))
            elif i==125 or j==75:
                draw.point((i, j),(r, 0, 0))
            else:
                draw.point((i, j),(r, g, 2*b))
        elif mode==167:
            if not(100<i<150 and 40<j<110) and not(10<i<60 and 10<j<80):
                draw.point((i, j),(r, 0, 0))
            elif (i==125 or j==75) or (i==35 or j==45):
                draw.point((i, j),(r, 0, 0))
            else:
                draw.point((i, j),(r, 0, 2*b))
        elif mode==168:
            if not(100<i<150 and 40<j<110) and not(10<i<60 and 0<j<70) and not(190<i<240 and 80<j<150):
                draw.point((i, j),(r, 0, 0))
            elif (i==125 or j==75) or (i==35 or j==25) or (i==205 or j==115):
                draw.point((i, j),(r, 0, 0))
            else:
                draw.point((i, j),(r, g, 2*b))
        elif mode==169:
            if not(100<i<150 and 40<j<110):
                draw.point((i, j),(0, g, 0))
            elif i==125 or j==75:
                draw.point((i, j),(0, g, 0))
            else:
                draw.point((i, j),(r, g, 2*b))
        elif mode==170:
            if not(100<i<150 and 40<j<110) and not(10<i<60 and 10<j<80):
                draw.point((i, j),(0, g, 0))
            elif (i==125 or j==75) or (i==35 or j==45):
                draw.point((i, j),(0, g, 0))
            else:
                draw.point((i, j),(r, 0, 2*b))
        elif mode==171:
            if not(100<i<150 and 40<j<110) and not(10<i<60 and 0<j<70) and not(190<i<240 and 80<j<150):
                draw.point((i, j),(0, g, 0))
            elif (i==125 or j==75) or (i==35 or j==25) or (i==205 or j==115):
                draw.point((i, j),(0, g, 0))
            else:
                draw.point((i, j),(r, g, 2*b))
        elif mode==172:
            if not(100<i<150 and 40<j<110):
                draw.point((i, j),(0, g, b))
            elif i==125 or j==75:
                draw.point((i, j),(0, g, b))
            else:
                draw.point((i, j),(r, g, 2*b))
        elif mode==173:
            if not(100<i<150 and 40<j<110) and not(10<i<60 and 10<j<80):
                draw.point((i, j),(0, g, b))
            elif (i==125 or j==75) or (i==35 or j==45):
                draw.point((i, j),(0, g, b))
            else:
                draw.point((i, j),(r, 0, 2*b))
        elif mode==174:
            if not(100<i<150 and 40<j<110) and not(10<i<60 and 0<j<70) and not(190<i<240 and 80<j<150):
                draw.point((i, j),(0, g, b))
            elif (i==125 or j==75) or (i==35 or j==25) or (i==205 or j==115):
                draw.point((i, j),(0, g, b))
            else:
                draw.point((i, j),(r, g, 2*b))
                
                        
    image.save("Image"+str(k)+".jpg", "JPEG")


