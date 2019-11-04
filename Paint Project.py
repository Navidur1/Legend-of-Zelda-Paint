#Paint Project
#The Legend of Zelda Paint
#By: Navidur Rahman

######################################################
#Prerequisites
######################################################
#importing all needed modules
from random import *
from math import *
from pickle import *
from tkinter import *
from tkinter.messagebox import *
from pygame import *

#initializing
init()
font.init()
mixer.init()
root = Tk()
root.withdraw()

#colours
RED  = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,247,60)
LIME = (112,244,48)
TEAL = (136,219,253)
PINK = (240,116,191)
ORANGE = (242,131,52)
PURPLE = (189,64,175)
PEACH = (241,123,108)

#start up
width,height = screensize = (1320,650)
screen = display.set_mode(screensize)
myClock = time.Clock()
display.set_caption("Zelda Paint")
running = True
tool = "no tool"

#canvas surface
canvas = Surface((800,450))

#######################################################
#Importing Pictures
######################################################
#Stamps
####################################
#Characters
####################################

#loading images
#transforming images for box
Ganon = image.load("Zelda/Stamps/Characters/Ganon.png")
Ganonimg = transform.smoothscale(Ganon,(80,80))

Ganondorf = image.load("Zelda/Stamps/Characters/Ganondorf.png")
Ganondorfimg = transform.smoothscale(Ganondorf,(80,80))

Ghirahim = image.load("Zelda/Stamps/Characters/Ghirahim.png")
Ghirahimimg = transform.smoothscale(Ghirahim,(80,80))

Link = image.load("Zelda/Stamps/Characters/Link.png")
Linkimg = transform.smoothscale(Link,(80,80))

Midna = image.load("Zelda/Stamps/Characters/Midna.png")
Midnaimg = transform.smoothscale(Midna,(80,80))

Navi = image.load("Zelda/Stamps/Characters/Navi.png")
Naviimg = transform.smoothscale(Navi,(80,80))

Sheik = image.load("Zelda/Stamps/Characters/Sheik.png")
Sheikimg = transform.smoothscale(Sheik,(80,80))

SkullKid = image.load("Zelda/Stamps/Characters/Skull Kid.png")
SkullKidimg = transform.smoothscale(SkullKid,(80,80))

Tingle = image.load("Zelda/Stamps/Characters/Tingle.png")
Tingleimg = transform.smoothscale(Tingle,(80,80))

Zelda = image.load("Zelda/Stamps/Characters/Zelda.png")
Zeldaimg = transform.smoothscale(Zelda,(80,80))

####################################
#Items
####################################

Boat = image.load("Zelda/Stamps/Items/Boat.png")
Boatimg = transform.smoothscale(Boat,(80,80))

Bomb = image.load("Zelda/Stamps/Items/Bomb.png")
Bombimg = transform.smoothscale(Bomb,(80,80))

Boomerang = image.load("Zelda/Stamps/Items/Boomerang.png")
Boomerangimg = transform.smoothscale(Boomerang,(80,80))

Bow = image.load("Zelda/Stamps/Items/Bow.png")
Bowimg = transform.smoothscale(Bow,(80,80))

Hookshot = image.load("Zelda/Stamps/Items/Hookshot.png")
Hookshotimg = transform.smoothscale(Hookshot,(80,80))

Mask = image.load("Zelda/Stamps/Items/Mask.png")
Maskimg = transform.smoothscale(Mask,(80,80))

Ocarina = image.load("Zelda/Stamps/Items/Ocarina.png")
Ocarinaimg = transform.smoothscale(Ocarina,(80,80))

Shield = image.load("Zelda/Stamps/Items/Shield.png")
Shieldimg = transform.smoothscale(Shield,(80,80))

Sword = image.load("Zelda/Stamps/Items/Sword.png")
Swordimg = transform.smoothscale(Sword,(80,80))

WindWaker = image.load("Zelda/Stamps/Items/Wind Waker.png")
WindWakerimg = transform.smoothscale(WindWaker,(80,80))

####################################
#Backgrounds
####################################

BG1 = image.load("Zelda/BGS/BG 1.jpg")
BG1img = transform.smoothscale(BG1,(132,70))

BG2 = image.load("Zelda/BGS/BG 2.jpg")
BG2img = transform.smoothscale(BG2,(132,70))

BG3 = image.load("Zelda/BGS/BG 3.jpg")
BG3img = transform.smoothscale(BG3,(132,70))

BG4 = image.load("Zelda/BGS/BG 4.jpg")
BG4img = transform.smoothscale(BG4,(132,70))

BG5 = image.load("Zelda/BGS/BG 5.jpg")
BG5img = transform.smoothscale(BG5,(132,70))

BG = image.load("Zelda/BGS/BG.jpg")
screen.blit(BG,(0,0))

####################################
#Icons
####################################
#Tools
####################################

Pencilimg = image.load("Zelda/Pictures/Pencil.png")
Pencilimg = transform.smoothscale(Pencilimg,(80,80))

Eraserimg = image.load("Zelda/Pictures/Eraser.png")
Eraserimg = transform.smoothscale(Eraserimg,(80,80))

Brushimg = image.load("Zelda/Pictures/Brush.png")
Brushimg = transform.smoothscale(Brushimg,(80,80))

Sprayimg = image.load("Zelda/Pictures/Spray.png")
Sprayimg = transform.smoothscale(Sprayimg,(80,80))

Highlighterimg = image.load("Zelda/Pictures/Highlighter.png")
Highlighterimg = transform.smoothscale(Highlighterimg,(80,80))

Fillimg = image.load("Zelda/Pictures/Fill.png")
Fillimg = transform.smoothscale(Fillimg,(80,80))

Textimg = image.load("Zelda/Pictures/Text.png")
Textimg = transform.smoothscale(Textimg,(80,80))

Dropperimg = image.load("Zelda/Pictures/Dropper.png")
Dropperimg = transform.smoothscale(Dropperimg,(80,80))

####################################
#Shapes
####################################

Rectangleimg = image.load("Zelda/Pictures/Rectangle.png")
Rectangleimg = transform.smoothscale(Rectangleimg,(80,80))

Circleimg = image.load("Zelda/Pictures/Circle.png")
Circleimg = transform.smoothscale(Circleimg,(80,80))

Triangleimg = image.load("Zelda/Pictures/Triangle.png")
Triangleimg = transform.smoothscale(Triangleimg,(80,80))

Polygonimg = image.load("Zelda/Pictures/Polygon.png")
Polygonimg = transform.smoothscale(Polygonimg,(80,80))

Lineimg = image.load("Zelda/Pictures/Line.png")
Lineimg = transform.smoothscale(Lineimg,(80,80))

####################################
#Filters
####################################

Pixilateimg = image.load("Zelda/Pictures/Pixilate.png")
Pixilateimg = transform.smoothscale(Pixilateimg,(132,70))

Blurimg = image.load("Zelda/Pictures/Blur.png")
Blurimg = transform.smoothscale(Blurimg,(132,70))

Sepiaimg = image.load("Zelda/Pictures/Sepia.png")
Sepiaimg = transform.smoothscale(Sepiaimg,(132,70))

Greyscaleimg = image.load("Zelda/Pictures/Greyscale.png")
Greyscaleimg = transform.smoothscale(Greyscaleimg,(132,70))

Invertimg = image.load("Zelda/Pictures/Invert.png")
Invertimg = transform.smoothscale(Invertimg,(132,70))

####################################
#Others
####################################

Saveimg = image.load("Zelda/Pictures/Save.png")
Saveimg = transform.smoothscale(Saveimg,(60,60))

Loadimg = image.load("Zelda/Pictures/Load.png")
Loadimg = transform.smoothscale(Loadimg,(60,60))

Undoimg = image.load("Zelda/Pictures/Undo.png")
Undoimg = transform.smoothscale(Undoimg,(60,60))

Redoimg = image.load("Zelda/Pictures/Redo.png")
Redoimg = transform.smoothscale(Redoimg,(60,60))

Filledimg = image.load("Zelda/Pictures/Filled.png")
Filledimg = transform.smoothscale(Filledimg,(60,60))

Trashimg = image.load("Zelda/Pictures/Trash.png")
Trashimg = transform.smoothscale(Trashimg,(60,60))

PlayPauseimg = image.load("Zelda/Pictures/Play Pause.png")
PlayPauseimg = transform.smoothscale(PlayPauseimg,(60,60))

Skipimg = image.load("Zelda/Pictures/Skip.png")
Skipimg = transform.smoothscale(Skipimg,(60,60))

Upimg = image.load("Zelda/Pictures/Up.png")
Upimg = transform.smoothscale(Upimg,(80,25))

Downimg = image.load("Zelda/Pictures/Down.png")
Downimg = transform.smoothscale(Downimg,(80,25))

palette = image.load("Zelda/Palette.png")
palette = transform.scale(palette,(180,180))

#######################################################
#Music
######################################################

#list of all music so you can change songs
music = ["Main.mp3","Song of Storms.mp3","Gerudo Valley.mp3","Hyrule Field.mp3","Kakariko Village.mp3","Zelda's Lullaby.mp3"]
musicpos = 0

mixer.music.load("Zelda/Songs/Main.mp3")
mixer.music.play(-1)
                 

#######################################################
#Rectangles
######################################################

#all the rectangles in the program
pencilRect = Rect(35,40,80,80)
eraserRect = Rect(135,40,80,80)
paintbrushRect = Rect(35,140,80,80)
spraypaintRect = Rect(135,140,80,80)
highlighterRect = Rect(35,240,80,80)
fillRect = Rect(135,240,80,80)
textRect = Rect(35,340,80,80)
dropperRect = Rect(135,340,80,80)

rectangleRect = Rect(1105,20,80,80)
circleRect = Rect(1105,120,80,80)
triangleRect = Rect(1105,220,80,80)
polygonRect = Rect(1105,320,80,80)
lineRect = Rect(1105,420,80,80)

stamp1Rect = Rect(1205,40,80,80)
stamp2Rect = Rect(1205,130,80,80)
stamp3Rect = Rect(1205,220,80,80)
stamp4Rect = Rect(1205,310,80,80)
stamp5Rect = Rect(1205,400,80,80)

prevpgRect = Rect(1205,10,80,25)
nextpgRect = Rect(1205,485,80,25)

saveRect = Rect(1060,520,60,60)
loadRect = Rect(1125,520,60,60)
undoRect = Rect(1190,520,60,60)
redoRect = Rect(1255,520,60,60)
filledRect = Rect(1060,585,60,60)
trashRect = Rect(1125,585,60,60)
playpauseRect = Rect(1190,585,60,60)
skipRect = Rect(1255,585,60,60)

bg1Rect = Rect(320,490,132,70)
bg2Rect = Rect(467,490,132,70)
bg3Rect = Rect(614,490,132,70)
bg4Rect = Rect(761,490,132,70)
bg5Rect = Rect(908,490,132,70)
sepiaRect = Rect(320,570,132,70)
greyscaleRect = Rect(467,570,132,70)
invertRect = Rect(614,570,132,70)
pixilateRect = Rect(761,570,132,70)
blurRect = Rect(908,570,132,70)

canvasRect = Rect(260,25,800,450)
paletteRect = Rect(15,455,180,180)

canvas.fill(WHITE)

col = BLUE
omx = omy = 300

#buffers
screenBuff = screen.copy()
canvasBuff = canvas.copy()

#list for undo and redo
undoList = []
redoList = []

#sizes
size = "no size"
toolsize = 10
shapesize = 5
stampsize = 25

#lists and variables for tools
polyPoints = []
usedPixels = set()
filled = False
shift = False
clicked = False
horizontal = False
vertical = False
saved = False
playing = True
page = 1
rotoangle = 0

####################################################################
#Functions
####################################################################
#Tools
####################################
def pencil():
    if mb[0]:
        draw.line(canvas,col,(ocmx,ocmy),(cmx,cmy))
        
def eraser():
    #draws white circles based on change in x and y 
    dx=cmx-ocmx
    dy=cmy-ocmy
    dist=int(sqrt(dx**2+dy**2))
    if dist > 0:
        for i in range(1,dist+1):
            dotX=int(ocmx+i*dx/dist)  
            dotY=int(ocmy+i*dy/dist)
            draw.circle(canvas,WHITE,(dotX,dotY),toolsize)

    else:
        draw.circle(canvas,WHITE,(cmx,cmy),toolsize)

def brush():
    #draws circles based on change in x and y
    dx=cmx-ocmx
    dy=cmy-ocmy
    dist=int(sqrt(dx**2+dy**2))
    if dist > 0:
        for i in range(1,dist+1):
            dotX=int(ocmx+i*dx/dist)  
            dotY=int(ocmy+i*dy/dist)
            draw.circle(canvas,col,(dotX,dotY),toolsize)

    else:
        draw.circle(canvas,col,(cmx,cmy),toolsize)

def spray():
    #generates a random point near the mouse position
    speed = int(toolsize/9)+int(toolsize/9)
    for i in range(speed):
        cx = randint(cmx-toolsize,cmx+toolsize)
        cy = randint(cmy-toolsize,cmy+toolsize)
        #if the point is in the desired circle, sets the pixel to the chosen colour
        if (((cmx-cx)**2+(cmy-cy)**2)**0.5) <= toolsize:
            canvas.set_at((cx,cy),col)

def highlighter():
    dx=cmx-ocmx
    dy=cmy-ocmy
    dist=int(sqrt(dx**2+dy**2))
    #creates a transparent surface based on the toolsize
    brushSurface = Surface((toolsize*2,toolsize*2),SRCALPHA)
    draw.circle(brushSurface,(col[0],col[1],col[2],3),(int(toolsize),int(toolsize)),toolsize)
    #based on the change in x and y draws a semi transparent circle on the surface then blits the surface
    for i in range(1,dist+1):
        dotX=int(ocmx+i*dx/dist)  
        dotY=int(ocmy+i*dy/dist)        
        canvas.blit(brushSurface,(dotX-toolsize,dotY-toolsize))

def fill():
    if mb[0]:
        cmx = mouse.get_pos()[0]-260
        cmy = mouse.get_pos()[1]-25
        pixels = [(cmx,cmy)]#list of the pixels
        colStart = canvas.get_at((cmx,cmy)) #starting colour 
        if colStart != col:
            while len(pixels) > 0:#while there are pixels in the list checks to see if a point is the starting colour then sets that pixel to the chosen colour
                if canvasRect.collidepoint((pixels[0][0]+260,pixels[0][1]+25)) and canvas.get_at(pixels[0]) == colStart:
                    canvas.set_at((pixels[0]),col)
                    pixels.append((pixels[0][0],pixels[0][1]-1))#appends the pixels around the last pixel
                    pixels.append((pixels[0][0],pixels[0][1]+1))
                    pixels.append((pixels[0][0]-1,pixels[0][1]))
                    pixels.append((pixels[0][0]+1,pixels[0][1]))
                del pixels[0]

    if mb[2]:
        canvas.fill(col)#fills whole canvas
    
####################################
#Shapes
####################################
        
def polygon():
    global polyPoints,screenBuff
    if len(polyPoints) > 0:#draws lines to show where your next point will be
        draw.line(screen,col,(polyPoints[-1][0]+260,polyPoints[-1][1]+25),(mx,my))
    
    if (cmx,cmy) not in polyPoints and click and mb[0]:#appends points that were clicked into a list and draws lines from one to another
        polyPoints.append((cmx,cmy))
        if len(polyPoints) > 1:
            draw.line(canvas,col,(polyPoints[-2]),(polyPoints[-1]))

    if mb[2] == 1:#closes the shape if right clicked
        if filled:
            try:
                draw.polygon(canvas,col,(polyPoints),0)
                polyPoints = []
                
            except:
                pass

        else:
            try:
                draw.polygon(canvas,col,(polyPoints),1)
                polyPoints = []

            except:
                pass

def rectangle(perfect):
    global canvasBuff
    dx = cmx-sx
    dy = cmy-sy
    if perfect:#if statements for distance for squares
        if dx > 0 and dy > 0:
            if dx > dy:

                dy = dx

            else:
                dx = dy

        if dx < 0 and dy < 0:
            if dx > dy:
                dx = dy

            else:
                dy = dx
            
        if  dx > 0 and dy < 0:
            if dx > abs(dy):
                dy = dx*-1

            if abs(dy) > dx:
                dx = dy*-1

        if dx < 0 and dy > 0:
            if dy > abs(dx):
                dx = dy*-1

            if abs(dx) > dy:
                dy = dx*-1
    rectRect = Rect(sx,sy,dx,dy)
    canvas.blit(canvasBuff,(0,0))#buffer
    if filled:
        if mb[0]:
            draw.rect(canvas,col,(rectRect),0)
       
    else:
        canvas.blit(canvasBuff,(0,0))#draws a rectangle using draw.rect then draws more 1 thick rectangles based on the shapesize
        for i in range(shapesize):
            for j in range(shapesize):
                draw.rect(canvas,col,[sx-i,sy-j,dx,dy],1)
                draw.rect(canvas,col,[sx-i,sy+j,dx,dy],1)
                draw.rect(canvas,col,[sx+i,sy-j,dx,dy],1)
                draw.rect(canvas,col,[sx+i,sy+j,dx,dy],1)

        draw.rect(canvas,col,[sx,sy,dx,dy],shapesize)
        
            
def circle(perfect):
    global canvasBuff
    dx = cmx-sx#distances for x and y
    dy =  my-sy
    if perfect:
        if dx > 0 and dy > 0:
            if dx > dy:
                dy = dx

            else:
                dx = dy

        if dx < 0 and dy < 0:
            if dx > dy:
                dx = dy

            else:
                dy = dx
            
        if  dx > 0 and dy < 0:
            if dx > abs(dy):
                dy = dx*-1

            if abs(dy) > dx:
                dx = dy*-1

        if dx < 0 and dy > 0:
            if dy > abs(dx):
                dx = dy*-1

            if abs(dx) > dy:
                dy = dx*-1
                
    ellipseRect = Rect(sx,sy,dx,dy)
    ellipseRect.normalize()
    canvas.blit(canvasBuff,(0,0))
    if filled:
        draw.ellipse(canvas,col,ellipseRect,0)

    else:       
        try:#draws 5 ellipses with each being +1/-1 in the x and y of the original rectangle
            draw.ellipse(canvas,col,ellipseRect,shapesize)
            draw.ellipse(canvas,col,(ellipseRect[0]-1,ellipseRect[1],ellipseRect[2],ellipseRect[3]),shapesize)
            draw.ellipse(canvas,col,(ellipseRect[0]+1,ellipseRect[1],ellipseRect[2],ellipseRect[3]),shapesize)
            draw.ellipse(canvas,col,(ellipseRect[0],ellipseRect[1]-1,ellipseRect[2],ellipseRect[3]),shapesize)
            draw.ellipse(canvas,col,(ellipseRect[0],ellipseRect[1]+1,ellipseRect[2],ellipseRect[3]),shapesize)
                    
        except:
            draw.ellipse(canvas,col,ellipseRect,0)
    
def line():
    canvas.blit(canvasBuff,(0,0))
    draw.line(canvas,col,(sx,sy),(cmx,cmy),shapesize)#draws a line from click point to current mouse

def triangle():
    dx = cmx-sx
    canvas.blit(canvasBuff,(0,0))
    if filled:
        draw.polygon(canvas,col,[(sx,sy),(cmx,cmy),(sx-dx,cmy)],0)#draws a triangle from click point, current point, and reflection of current point

    else:
        draw.polygon(canvas,col,[(sx,sy),(cmx,cmy),(sx-dx,cmy)],shapesize)
        
####################################
#Filters              
####################################
    
def sepia():
    for x in range(800):
        for y in range(450):#goes through every pixel in the canvas and sets it a brownish tone
            r,g,b,a = canvas.get_at((x,y))
            r2=min(255,int(r*.393 + g*.769 + b*.189))
            g2=min(255,int(r*.349 + g*.686 + b*.168))
            b2=min(255,int(r*.272 + g*.534 + b*.131))
            canvas.set_at((x,y),(r2,g2,b2))

def greyscale():
    for x in range(800):
        for y in range(450):#goes through every pixel in the canvas and sets it a greyish tone
            r,g,b,a = canvas.get_at((x,y))
            r2=min(255,int(r*.21 + g*.72 + b*.07))
            g2=min(255,int(r*.21 + g*.72 + b*.07))
            b2=min(255,int(r*.21 + g*.72 + b*.07))
            canvas.set_at((x,y),(r2,g2,b2))

def invert():
    for x in range(800):
        for y in range(450):#goes through every pixel in the canvas and inverts the colours by subtracting the r,g,b from 255
            r,g,b,a = canvas.get_at((x,y))
            r2= 255-r
            g2= 255-g
            b2= 255-b
            canvas.set_at((x,y),(r2,g2,b2))
   
def pixilate():
    surf = canvas.copy()#copys the canvas, transforms it really small then back to normal size for pixilating effect
    smallsurf = transform.scale(surf,(int(800/4),int(450/4)))
    bigsurf = transform.scale(smallsurf,(800,450))
    canvas.blit(bigsurf,(0,0))

def blur():
    for x in range(800):
        for y in range(450):#goes through every pixel in the canvas and averages out the r,g,b based on the pixels around it
            try:
                blur1 = canvas.get_at((x,y))
                blur2 = canvas.get_at((x-1,y))
                blur3 = canvas.get_at((x+1,y))
                blur4 = canvas.get_at((x,y-1))
                blur5 = canvas.get_at((x,y+1))

                blurred = int((blur1[0]+blur2[0]+blur3[0]+blur4[0]+blur5[0])/5)
                blurgreen = int((blur1[1]+blur2[1]+blur3[1]+blur4[1]+blur5[1])/5)
                blurblue = int((blur1[2]+blur2[2]+blur3[2]+blur4[2]+blur5[2])/5)
                blurcol = (blurred,blurgreen,blurblue)
                canvas.set_at((x,y),blurcol)

            except:
                pass

####################################
#Others
####################################
            
def sizeDisplay():
    if mb[0] == 0:
        canvas.blit(canvasBuff,(0,0))#draws a circle on the screen indicating the current toolsize
    draw.circle(screen,BLACK,(mx,my),toolsize,1)

#was not finished

def rainbow():#makes the col a rainbow
    global col
    r,g,b = col[0],col[1],col[2] 
    if r==255 and b==0 and g!=255:
        g+=1
        col[1],col[2],col[3] = r,g,b
        
    elif b==0 and g==255 and r!=0:
        r-=1
        col[1],col[2],col[3] = r,g,b
        
    elif r==0 and g==255 and b!=255:
        b+=1
        col[1],col[2],col[3] = r,g,b
    
    elif b==255 and r==0 and g!=0:
        g-=1
        col[1],col[2],col[3] = r,g,b
        
    elif g==0 and b==255 and r!=255:
        r+=1
        col[1],col[2],col[3] = r,g,b
        
    elif g==0 and r==255 and b!=0:
        b-=1
        col[1],col[2],col[3] = r,g,b

def undoact():#moves the last item in undo list to redo list
    try:
        redoList.append(undoList[-1])
        del undoList[-1]
        canvas.blit(undoList[-1],(0,0))#blits the second last item of undo list

    except:
        canvas.fill(WHITE)

def redoact():#moves the last item in redo list to undo list
    try:
        canvas.blit(redoList[-1],(0,0))#blits the last item of redo list
        undoList.append(redoList[-1])
        del redoList[-1]

    except:
        pass

#########################################################################
#Drawing
#########################################################################

draw.rect(screen,YELLOW,pencilRect,0)
draw.rect(screen,YELLOW,eraserRect,0)
draw.rect(screen,YELLOW,paintbrushRect,0)
draw.rect(screen,YELLOW,spraypaintRect,0)
draw.rect(screen,YELLOW,highlighterRect,0)
draw.rect(screen,YELLOW,fillRect,0)
draw.rect(screen,YELLOW,textRect,0)
draw.rect(screen,YELLOW,dropperRect,0)

screen.blit(Pencilimg,(35,40))
screen.blit(Eraserimg,(135,40))
screen.blit(Brushimg,(35,140))
screen.blit(Sprayimg,(135,140))
screen.blit(Highlighterimg,(35,240))
screen.blit(Fillimg,(135,240))
screen.blit(Textimg,(35,340))
screen.blit(Dropperimg,(135,340))

draw.rect(screen,LIME,rectangleRect,0)
draw.rect(screen,LIME,circleRect,0)
draw.rect(screen,LIME,triangleRect,0)
draw.rect(screen,LIME,polygonRect,0)
draw.rect(screen,LIME,lineRect,0)

screen.blit(Rectangleimg,(1105,20))
screen.blit(Circleimg,(1105,120))
screen.blit(Triangleimg,(1105,220))
screen.blit(Polygonimg,(1105,320))
screen.blit(Lineimg,(1105,420))

draw.rect(screen,TEAL,stamp1Rect,0)
draw.rect(screen,TEAL,stamp2Rect,0)
draw.rect(screen,TEAL,stamp3Rect,0)
draw.rect(screen,TEAL,stamp4Rect,0)
draw.rect(screen,TEAL,stamp5Rect,0)

draw.rect(screen,PURPLE,prevpgRect,0)
draw.rect(screen,PURPLE,nextpgRect,0)

screen.blit(Upimg,(1205,10))
screen.blit(Downimg,(1205,485))

draw.rect(screen,PINK,saveRect,0)
draw.rect(screen,PINK,loadRect,0)
draw.rect(screen,PINK,undoRect,0)
draw.rect(screen,PINK,redoRect,0)
draw.rect(screen,PINK,filledRect,0)
draw.rect(screen,PINK,trashRect,0)
draw.rect(screen,PINK,playpauseRect,0)
draw.rect(screen,PINK,skipRect,0)

screen.blit(Saveimg,(1060,520))
screen.blit(Loadimg,(1125,520))
screen.blit(Undoimg,(1190,520))
screen.blit(Redoimg,(1255,520))
screen.blit(Filledimg,(1060,585))
screen.blit(Trashimg,(1125,585))
screen.blit(PlayPauseimg,(1190,585))
screen.blit(Skipimg,(1255,585))

draw.rect(screen,YELLOW,bg1Rect,1)
draw.rect(screen,YELLOW,bg2Rect,1)
draw.rect(screen,YELLOW,bg3Rect,1)
draw.rect(screen,YELLOW,bg4Rect,1)
draw.rect(screen,YELLOW,bg5Rect,1)

screen.blit(BG1img,(320,490))
screen.blit(BG2img,(467,490))
screen.blit(BG3img,(614,490))
screen.blit(BG4img,(761,490))
screen.blit(BG5img,(908,490))
    
draw.rect(screen,ORANGE,sepiaRect,1)
draw.rect(screen,ORANGE,greyscaleRect,1)
draw.rect(screen,ORANGE,invertRect,0)
draw.rect(screen,ORANGE,pixilateRect,1)
draw.rect(screen,ORANGE,blurRect,0)

screen.blit(Sepiaimg,(320,570))
screen.blit(Greyscaleimg,(467,570))
screen.blit(Invertimg,(614,570))
screen.blit(Pixilateimg,(761,570))
screen.blit(Blurimg,(908,570))

screen.blit(palette,(15,455))
    
####################################################################
#Main Loop
####################################################################

while running:
    #variables that reset
    click = False
    eventText = ""
    done = False
    ##################################################################
    #Event Loop
    ##################################################################
    for evt in event.get():   
        if evt.type == QUIT:
            if saved == False:#asks the user to save their work when exiting
                    title="Save".title()
                    message="Would you like to save?"
                    ask=askquestion(title,message,type="yesnocancel")
                    if ask=="yes":
                        filename=filedialog.asksaveasfilename(defaultextension="png")
                        if filename!=None:
                            running=False
                            
                    if ask=="no":
                            running=False
                            
                    if ask=="cancel":
                            pass
            
            else:
                running=False

        if evt.type == MOUSEBUTTONDOWN:#if clicked and not scroll
            if not evt.button == 4 and not evt.button == 5:
                
                sx,sy = evt.pos
                sx -= 260
                sy -= 25
                
            click = True
            #changing sizes with scroll
            if evt.button == 4:
                if size == "toolsize":
                    if toolsize > 1:
                        toolsize = int((toolsize+1)*1.1)
                        
                    if toolsize == 1:
                        toolsize += 1

                if size == "shapesize":
                    if shapesize > 1:
                        shapesize = int((shapesize+1)*1.1)
                        
                    if shapesize == 1:
                        shapesize += 1

                if size == "stampsize":
                    if stampsize > 1:
                        stampsize = int((stampsize+1)*1.1)
                        
                    if stampsize == 1:
                        stampsize += 1

            if evt.button == 5:
                if size == "toolsize":
                    if toolsize > 1:
                        toolsize = int(toolsize/1.1)

                if size == "shapesize":
                    if shapesize > 1:
                        shapesize = int(shapesize/1.1)

                if size == "stampsize":
                    if stampsize > 1:
                        stampsize = int(stampsize/1.1)

        if evt.type == MOUSEBUTTONUP:
            #takes copy of canvas
            if canvasRect.collidepoint(mx,my):
                if evt.button != 4 and evt.button != 5:
                    canvasBuff = canvas.copy()
                    undo = canvas.copy()
                    undoList.append(undo)

        if evt.type == KEYDOWN:
            #variables for flipping stamps horizontally and vertically
            if evt.key == K_h and tool == "stamp":
                if horizontal:
                    horizontal = False

                else:
                    horizontal = True

            if evt.key == K_v and tool == "stamp":
                if vertical:
                    vertical = False

                else:
                    vertical = True

            if evt.key != K_TAB and evt.key != K_RETURN and evt.key != K_BACKSPACE:
                #key that was last pressed for text tool
                eventText += chr(evt.key)
                

            if evt.key == K_RETURN:
                done = True
                
                    
    mx,my = mouse.get_pos()
    cmx,cmy = mx-260,my-25
    mb = mouse.get_pressed()
    ########################################################################
    #Current Colour and Canvas
    ########################################################################

    #shows current colour and canvas
    draw.circle(screen,col,(255,535),40,0)
    screen.blit(canvas,(260,25))

    ########################################################################
    #Displaying Stamps
    ########################################################################

    #shows the stamps based on the current page
    if page == 1:
        draw.rect(screen,TEAL,stamp1Rect,0)
        draw.rect(screen,TEAL,stamp2Rect,0)
        draw.rect(screen,TEAL,stamp3Rect,0)
        draw.rect(screen,TEAL,stamp4Rect,0)
        draw.rect(screen,TEAL,stamp5Rect,0)
        
        screen.blit(Ganonimg,(1205,40))
        screen.blit(Ganondorfimg,(1205,130))
        screen.blit(Ghirahimimg,(1205,220))
        screen.blit(Linkimg,(1205,310))
        screen.blit(Midnaimg,(1205,400))

    if page == 2:
        draw.rect(screen,TEAL,stamp1Rect,0)
        draw.rect(screen,TEAL,stamp2Rect,0)
        draw.rect(screen,TEAL,stamp3Rect,0)
        draw.rect(screen,TEAL,stamp4Rect,0)
        draw.rect(screen,TEAL,stamp5Rect,0)
        
        screen.blit(Naviimg,(1205,40))
        screen.blit(Sheikimg,(1205,130))
        screen.blit(SkullKidimg,(1205,220))
        screen.blit(Tingleimg,(1205,310))
        screen.blit(Zeldaimg,(1205,400))

    if page == 3:
        draw.rect(screen,TEAL,stamp1Rect,0)
        draw.rect(screen,TEAL,stamp2Rect,0)
        draw.rect(screen,TEAL,stamp3Rect,0)
        draw.rect(screen,TEAL,stamp4Rect,0)
        draw.rect(screen,TEAL,stamp5Rect,0)
        
        screen.blit(Boatimg,(1205,40))
        screen.blit(Bombimg,(1205,130))
        screen.blit(Boomerangimg,(1205,220))
        screen.blit(Bowimg,(1205,310))
        screen.blit(Hookshotimg,(1205,400))

    if page == 4:
        draw.rect(screen,TEAL,stamp1Rect,0)
        draw.rect(screen,TEAL,stamp2Rect,0)
        draw.rect(screen,TEAL,stamp3Rect,0)
        draw.rect(screen,TEAL,stamp4Rect,0)
        draw.rect(screen,TEAL,stamp5Rect,0)
        
        screen.blit(Maskimg,(1205,40))
        screen.blit(Ocarinaimg,(1205,130))
        screen.blit(Shieldimg,(1205,220))
        screen.blit(Swordimg,(1205,310))
        screen.blit(WindWakerimg,(1205,400))
        
    ######################################################################
    #Selecting Tools
    ######################################################################

    #if clicked on the tool rect sets the current tool
    if pencilRect.collidepoint(mx,my) and click and mb[0] == 1:
        tool = "pencil"
          
    if eraserRect.collidepoint(mx,my) and click and mb[0] == 1:
        tool = "eraser"

    if paintbrushRect.collidepoint(mx,my) and click and mb[0] == 1:
        tool = "paint brush"

    if spraypaintRect.collidepoint(mx,my) and click and mb[0] == 1:
        tool = "spray paint"

    if highlighterRect.collidepoint(mx,my) and click and mb[0] == 1:
        tool = "highlighter"

    if fillRect.collidepoint(mx,my) and click and mb[0] == 1:
        tool = "fill"

    if textRect.collidepoint(mx,my) and click and mb[0] == 1:
        tool = "text"

    if dropperRect.collidepoint(mx,my) and click and mb[0] == 1:
        tool = "dropper"

    if rectangleRect.collidepoint(mx,my) and click and mb[0] == 1:
        tool = "rectangle"

    if circleRect.collidepoint(mx,my) and click and mb[0] == 1:
        tool = "circle"

    if triangleRect.collidepoint(mx,my) and click and mb[0] == 1:
        tool = "triangle"

    if polygonRect.collidepoint(mx,my) and click and mb[0] == 1:
        tool = "polygon"

    if lineRect.collidepoint(mx,my) and click:
        tool = "line"

    ######################################################################
    #Selecting Stamps and Backgrounds
    ######################################################################
    #Stamps
    ######################################################

    #sets the current stamp based on the stamp rectangle number and the current page
    if stamp1Rect.collidepoint(mx,my) and click:
        tool = "stamp"
        draw.rect(screen,GREEN,stamp1Rect,2)
        if page == 1:
            stamp = "ganon"

        if page == 2:
            stamp = "navi"

        if page == 3:
            stamp = "boat"

        if page == 4:
            stamp = "mask"

    if stamp2Rect.collidepoint(mx,my) and click:
        tool = "stamp"
        draw.rect(screen,GREEN,stamp2Rect,2)
        if page == 1:
            stamp = "ganondorf"

        if page == 2:
            stamp = "sheik"

        if page == 3:
            stamp = "bomb"

        if page == 4:
            stamp = "ocarina"

    if stamp3Rect.collidepoint(mx,my) and click:
        tool = "stamp"
        draw.rect(screen,GREEN,stamp3Rect,2)
        if page == 1:
            stamp = "ghirahim"

        if page == 2:
            stamp = "skull kid"

        if page == 3:
            stamp = "boomerang"

        if page == 4:
            stamp = "shield"

    if stamp4Rect.collidepoint(mx,my) and click:
        tool = "stamp"
        draw.rect(screen,GREEN,stamp4Rect,2)
        if page == 1:
            stamp = "link"

        if page == 2:
            stamp = "tingle"

        if page == 3:
            stamp = "bow"

        if page == 4:
            stamp = "sword"

    if stamp5Rect.collidepoint(mx,my) and click:
        tool = "stamp"
        draw.rect(screen,GREEN,stamp5Rect,2)
        if page == 1:
            stamp = "midna"

        if page == 2:
            stamp = "zelda"

        if page == 3:
            stamp = "hookshot"

        if page == 4:
            stamp = "wind waker"
            
    ######################################################
    #Backgrounds
    ######################################################

    #blits the background after resizing
    if bg1Rect.collidepoint(mx,my) and click:
        BG1 = transform.smoothscale(BG1,(880,500))
        canvas.blit(BG1,(0,0))
        canvasBuff = canvas.copy()

    if bg2Rect.collidepoint(mx,my) and click:
        BG2 = transform.smoothscale(BG2,(880,500))
        canvas.blit(BG2,(0,0))
        canvasBuff = canvas.copy()

    if bg3Rect.collidepoint(mx,my) and click:
        BG3 = transform.smoothscale(BG3,(880,500))
        canvas.blit(BG3,(0,0))
        canvasBuff = canvas.copy()

    if bg4Rect.collidepoint(mx,my) and click:
        BG4 = transform.smoothscale(BG4,(880,500))
        canvas.blit(BG4,(0,0))
        canvasBuff = canvas.copy()

    if bg5Rect.collidepoint(mx,my) and click:
        BG5 = transform.smoothscale(BG5,(880,500))
        canvas.blit(BG5,(0,0))
        canvasBuff = canvas.copy()
        
    #####################################################################
    #Other Rects
    #####################################################################
        
    if filledRect.collidepoint(mx,my) and click:
        if filled:
            filled = False

        else:
            filled = True

    #changes pages down
    if prevpgRect.collidepoint(mx,my) and click:
        if page > 0:
            page-=1

        if page == 0:
            page = 4

    #changes pages up
    if nextpgRect.collidepoint(mx,my) and click:
        if page < 5:
            page+=1

        if page == 5:
            page = 1

    #clears the whole screen
    if trashRect.collidepoint(mx,my) and click:
        canvas.fill(WHITE)
        canvasBuff = canvas.copy()
  
    if playpauseRect.collidepoint(mx,my) and click:
        if playing:
            mixer.music.pause()
            playing = False

        else:
            mixer.music.unpause()
            playing = True

    if skipRect.collidepoint(mx,my) and click:
        if musicpos < 6:
            musicpos+=1

        if musicpos == 6:
            musicpos = 0
            
        pos = "Zelda/Songs/" + music[musicpos]
        mixer.music.load(pos)
        mixer.music.play(-1)
            
    #####################################################################
    #Size
    #####################################################################
    #changes a size variable based on current tool
    if tool == "eraser" or tool == "paint brush" or tool == "spray paint" or tool == "highlighter":
        size = "toolsize"

    if tool == "line" or tool == "circle" or tool == "rectangle":
        size = "shapesize"

    if tool == "stamp":
        size = "stampsize"
            
    #####################################################################
    #Load/Save
    #####################################################################

    #asks the user to load a file then blits it to the canvas
    if loadRect.collidepoint(mx,my) and click:
        draw.rect(screen,GREEN,loadRect,2)
        try:
            fname=filedialog.askopenfilename(filetypes=[("Images","*.png;*.bmp;*.jpg;*.jpeg")])
            file = image.load(fname)
            canvas.blit(file,(0,0))
            canvasBuff = canvas.copy()
        except:
            pass

    #asks the user to save a copy of the canvas
    if saveRect.collidepoint(mx,my) and click:
        draw.rect(screen,GREEN,saveRect,2)
        try:
            fname=filedialog.asksaveasfilename(defaultextension=".png")            
            image.save(canvas,fname)
            saved = True
            
        except:
            pass
        
    #####################################################################
    #Undo/Redo
    ######################################################################

    #does the undo action
    if undoRect.collidepoint(mx,my) and click:
        undoact()
        canvasBuff = canvas.copy()

    #does the redo action
    if redoRect.collidepoint(mx,my) and click:
        redoact()
        canvasBuff = canvas.copy()

    ######################################################################
    #Using Tools
    ######################################################################

    #uses tool based on current "tool" selected
    if canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect)#limits the user to the canvas
        if tool == "pencil":
            pencil()
            
        if tool == "eraser":
            sizeDisplay()
            if mb[0]:
                eraser()

        if tool == "paint brush":
            sizeDisplay()
            if mb[0] == 1:
                rainbow()
                brush()

        if tool == "spray paint":
            sizeDisplay()
            if mb[0]:
                spray()
                
        if tool == "highlighter":
            sizeDisplay()
            if mb[0]:
                highlighter()
            
        if tool == "fill":
            fill()

        if tool == "text":
            if click:
                clicked = True
                usedText = ""#resets the word if they click again
            
            if clicked:
                usedText += eventText#adds the text from the event loop
                dispText = comicFont.render(usedText,True,col)#renders the text and blits it to the canvas
                canvas.blit(dispText,(sx,sy))

            if done:
                usedText = ""#resets the text               
           
        if tool == "rectangle" and mb[0] == 1:#rectangles
            rectangle(False)

        if tool == "rectangle" and mb[2] == 1:#squares
            rectangle(True)

        if tool == "circle" and mb[0] == 1:#ellipses
            circle(False)

        if tool == "circle" and mb[2] == 1:#circles
            circle(True)

        if tool == "triangle" and mb[0] == 1:
            triangle()

        if tool == "polygon":
            polygon()
            
        if tool == "line" and mb[0] == 1:
            line()
      
        screen.set_clip(None)
        saved = False
        
    ######################################################################
    #Using Stamps
    ######################################################################
    #################################
    #For every stamp
    #scales the stamp based on stamp size, rotates the stamp if right clicked
    #flips the stamp if H or V is pressed
    #then blits the final image to the canvas
        
    if tool == "stamp":
        if stamp == "ganon":
            newGanon = transform.smoothscale(Ganon,(4*stampsize,4*stampsize))
            if mb[2]:
                rotoangle += 1
                newGanon = transform.rotate(newGanon,rotoangle)         
            if horizontal:
                newGanon = transform.flip(newGanon,True,False)
            if vertical:
                newGanon = transform.flip(newGanon,False,True)
            xpos = cmx-(stampsize*2)
            ypos = cmy-(stampsize*2)            
            canvas.blit(canvasBuff,(0,0))
            canvas.blit(newGanon,(xpos,ypos))

        if stamp == "ganondorf":
            newGanondorf = transform.smoothscale(Ganondorf,(4*stampsize,4*stampsize))
            if mb[2]:
                rotoangle += 1
                newGanondorf = transform.rotate(newGanondorf,rotoangle)         
            if horizontal:
                newGanondorf = transform.flip(newGanondorf,True,False)
            if vertical:
                newGanondorf = transform.flip(newGanondorf,False,True)
            xpos = cmx-(stampsize*2)
            ypos = cmy-(stampsize*2)            
            canvas.blit(canvasBuff,(0,0))
            canvas.blit(newGanondorf,(xpos,ypos))

        if stamp == "ghirahim":
            newGhirahim = transform.smoothscale(Ghirahim,(4*stampsize,4*stampsize))
            if mb[2]:
                rotoangle += 1
                newGhirahim = transform.rotate(newGhirahim,rotoangle)         
            if horizontal:
                newGhirahim = transform.flip(newGhirahim,True,False)
            if vertical:
                newGhirahim = transform.flip(newGhirahim,False,True)
            xpos = cmx-(stampsize*2)
            ypos = cmy-(stampsize*2)            
            canvas.blit(canvasBuff,(0,0))
            canvas.blit(newGhirahim,(xpos,ypos))

        if stamp == "link":
            newLink = transform.smoothscale(Link,(4*stampsize,5*stampsize))
            if mb[2]:
                rotoangle += 1
                newLink = transform.rotate(newLink,rotoangle)         
            if horizontal:
                newLink = transform.flip(newLink,True,False)
            if vertical:
                newLink = transform.flip(newLink,False,True)
            xpos = cmx-(stampsize*2)
            ypos = cmy-(stampsize*2)            
            canvas.blit(canvasBuff,(0,0))
            canvas.blit(newLink,(xpos,ypos))

        if stamp == "midna":
            newMidna = transform.smoothscale(Midna,(4*stampsize,4*stampsize))
            if mb[2]:
                rotoangle += 1
                newMidna = transform.rotate(newMidna,rotoangle)         
            if horizontal:
                newMidna = transform.flip(newMidna,True,False)
            if vertical:
                newMidna = transform.flip(newMidna,False,True)
            xpos = cmx-(stampsize*2)
            ypos = cmy-(stampsize*2)            
            canvas.blit(canvasBuff,(0,0))
            canvas.blit(newMidna,(xpos,ypos))

        if stamp == "navi":
            newNavi = transform.smoothscale(Navi,(4*stampsize,4*stampsize))
            if mb[2]:
                rotoangle += 1
                newNavi = transform.rotate(newNavi,rotoangle)         
            if horizontal:
                newNavi = transform.flip(newNavi,True,False)
            if vertical:
                newNavi = transform.flip(newNavi,False,True)
            xpos = cmx-(stampsize*2)
            ypos = cmy-(stampsize*2)            
            canvas.blit(canvasBuff,(0,0))
            canvas.blit(newNavi,(xpos,ypos))

        if stamp == "sheik":
            newSheik = transform.smoothscale(Sheik,(4*stampsize,4*stampsize))
            if mb[2]:
                rotoangle += 1
                newv = transform.rotate(newSheik,rotoangle)         
            if horizontal:
                newSheik = transform.flip(newSheik,True,False)
            if vertical:
                newSheik = transform.flip(newSheik,False,True)
            xpos = cmx-(stampsize*2)
            ypos = cmy-(stampsize*2)            
            canvas.blit(canvasBuff,(0,0))
            canvas.blit(newSheik,(xpos,ypos))

        if stamp == "skull kid":
            newSkullKid = transform.smoothscale(SkullKid,(4*stampsize,4*stampsize))
            if mb[2]:
                rotoangle += 1
                newSkullKid = transform.rotate(newSkullKid,rotoangle)         
            if horizontal:
                newSkullKid = transform.flip(newSkullKid,True,False)
            if vertical:
                newSkullKid = transform.flip(newSkullKid,False,True)
            xpos = cmx-(stampsize*2)
            ypos = cmy-(stampsize*2)            
            canvas.blit(canvasBuff,(0,0))
            canvas.blit(newSkullKid,(xpos,ypos))

        if stamp == "tingle":
            newTingle = transform.smoothscale(Tingle,(4*stampsize,4*stampsize))
            if mb[2]:
                rotoangle += 1
                newTingle = transform.rotate(newTingle,rotoangle)         
            if horizontal:
                newTingle = transform.flip(newTingle,True,False)
            if vertical:
                newTingle = transform.flip(newTingle,False,True)
            xpos = cmx-(stampsize*2)
            ypos = cmy-(stampsize*2)            
            canvas.blit(canvasBuff,(0,0))
            canvas.blit(newTingle,(xpos,ypos))

        if stamp == "zelda":
            newZelda = transform.smoothscale(Zelda,(4*stampsize,6*stampsize))
            if mb[2]:
                rotoangle += 1
                newZelda = transform.rotate(newZelda,rotoangle)         
            if horizontal:
                newZelda = transform.flip(newZelda,True,False)
            if vertical:
                newZelda = transform.flip(newZelda,False,True)
            xpos = cmx-(stampsize*2)
            ypos = cmy-(stampsize*2)            
            canvas.blit(canvasBuff,(0,0))
            canvas.blit(newZelda,(xpos,ypos))

        if stamp == "boat":
            newBoat = transform.smoothscale(Boat,(4*stampsize,4*stampsize))
            if mb[2]:
                rotoangle += 1
                newBoat = transform.rotate(newBoat,rotoangle)         
            if horizontal:
                newBoat = transform.flip(newBoat,True,False)
            if vertical:
                newBoat = transform.flip(newBoat,False,True)
            xpos = cmx-(stampsize*2)
            ypos = cmy-(stampsize*2)            
            canvas.blit(canvasBuff,(0,0))
            canvas.blit(newBoat,(xpos,ypos))

        if stamp == "bomb":
            newBomb = transform.smoothscale(Bomb,(4*stampsize,4*stampsize))
            if mb[2]:
                rotoangle += 1
                newBomb = transform.rotate(newBomb,rotoangle)         
            if horizontal:
                newBomb = transform.flip(newBomb,True,False)
            if vertical:
                newBomb = transform.flip(newBomb,False,True)
            xpos = cmx-(stampsize*2)
            ypos = cmy-(stampsize*2)            
            canvas.blit(canvasBuff,(0,0))
            canvas.blit(newBomb,(xpos,ypos))

        if stamp == "boomerang":
            newBoomerang = transform.smoothscale(Boomerang,(4*stampsize,4*stampsize))
            if mb[2]:
                rotoangle += 1
                newBoomerang = transform.rotate(newBoomerang,rotoangle)         
            if horizontal:
                newBoomerang = transform.flip(newBoomerang,True,False)
            if vertical:
                newBoomerang = transform.flip(newBoomerang,False,True)
            xpos = cmx-(stampsize*2)
            ypos = cmy-(stampsize*2)            
            canvas.blit(canvasBuff,(0,0))
            canvas.blit(newBoomerang,(xpos,ypos))

        if stamp == "bow":
            newBow = transform.smoothscale(Bow,(4*stampsize,4*stampsize))
            if mb[2]:
                rotoangle += 1
                newBow = transform.rotate(newBow,rotoangle)         
            if horizontal:
                newBow = transform.flip(newBow,True,False)
            if vertical:
                newBow = transform.flip(newBow,False,True)
            xpos = cmx-(stampsize*2)
            ypos = cmy-(stampsize*2)            
            canvas.blit(canvasBuff,(0,0))
            canvas.blit(newBow,(xpos,ypos))

        if stamp == "hookshot":
            newHookshot = transform.smoothscale(Hookshot,(4*stampsize,4*stampsize))
            if mb[2]:
                rotoangle += 1
                newHookshot = transform.rotate(newHookshot,rotoangle)         
            if horizontal:
                newHookshot = transform.flip(newHookshot,True,False)
            if vertical:
                newHookshot = transform.flip(newHookshot,False,True)
            xpos = cmx-(stampsize*2)
            ypos = cmy-(stampsize*2)            
            canvas.blit(canvasBuff,(0,0))
            canvas.blit(newHookshot,(xpos,ypos))

        if stamp == "mask":
            newMask = transform.smoothscale(Mask,(4*stampsize,4*stampsize))
            if mb[2]:
                rotoangle += 1
                newMask = transform.rotate(newMask,rotoangle)         
            if horizontal:
                newMask = transform.flip(newMask,True,False)
            if vertical:
                newMask = transform.flip(newMask,False,True)
            xpos = cmx-(stampsize*2)
            ypos = cmy-(stampsize*2)            
            canvas.blit(canvasBuff,(0,0))
            canvas.blit(newMask,(xpos,ypos))

        if stamp == "ocarina":
            newOcarina = transform.smoothscale(Ocarina,(4*stampsize,4*stampsize))
            if mb[2]:
                rotoangle += 1
                newOcarina = transform.rotate(newOcarina,rotoangle)         
            if horizontal:
                newOcarina = transform.flip(newOcarina,True,False)
            if vertical:
                newOcarina = transform.flip(newOcarina,False,True)
            xpos = cmx-(stampsize*2)
            ypos = cmy-(stampsize*2)            
            canvas.blit(canvasBuff,(0,0))
            canvas.blit(newOcarina,(xpos,ypos))

        if stamp == "shield":
            newShield = transform.smoothscale(Shield,(4*stampsize,4*stampsize))
            if mb[2]:
                rotoangle += 1
                newShield = transform.rotate(newShield,rotoangle)         
            if horizontal:
                newShield = transform.flip(newShield,True,False)
            if vertical:
                newShield = transform.flip(newShield,False,True)
            xpos = cmx-(stampsize*2)
            ypos = cmy-(stampsize*2)            
            canvas.blit(canvasBuff,(0,0))
            canvas.blit(newShield,(xpos,ypos))

        if stamp == "sword":
            newSword = transform.smoothscale(Sword,(5*stampsize,4*stampsize))
            if mb[2]:
                rotoangle += 1
                newSword = transform.rotate(newSword,rotoangle)         
            if horizontal:
                newSword = transform.flip(newSword,True,False)
            if vertical:
                newSword = transform.flip(newSword,False,True)
            xpos = cmx-(stampsize*2)
            ypos = cmy-(stampsize*2)            
            canvas.blit(canvasBuff,(0,0))
            canvas.blit(newSword,(xpos,ypos))

        if stamp == "wind waker":
            newWindWaker = transform.smoothscale(WindWaker,(4*stampsize,4*stampsize))
            if mb[2]:
                rotoangle += 1
                newWindWaker = transform.rotate(newWindWaker,rotoangle)         
            if horizontal:
                newWindWaker = transform.flip(newWindWaker,True,False)
            if vertical:
                newWindWaker = transform.flip(newWindWaker,False,True)
            xpos = cmx-(stampsize*2)
            ypos = cmy-(stampsize*2)            
            canvas.blit(canvasBuff,(0,0))
            canvas.blit(newWindWaker,(xpos,ypos))
                        
    ######################################################################
    #Using Filters
    ######################################################################

    #uses the filter functions and copies the new canvas
    if sepiaRect.collidepoint(mx,my) and click:
        sepia()
        canvasBuff = canvas.copy()

    if greyscaleRect.collidepoint(mx,my) and click:
        greyscale()
        canvasBuff = canvas.copy()

    if invertRect.collidepoint(mx,my) and click:
        invert()
        canvasBuff = canvas.copy()

    if pixilateRect.collidepoint(mx,my) and click:
        pixilate()
        canvasBuff = canvas.copy()

    if blurRect.collidepoint(mx,my) and click:
        blur()
        canvasBuff = canvas.copy()
        
    ######################################################################
    #Colour Changer
    ######################################################################

    #sets the current colour to the colour at the clicked pixel  
    if paletteRect.collidepoint(mx,my) and mb[0] == 1 and click:
        col = screen.get_at((mx,my))

    if tool == "dropper" and not dropperRect.collidepoint(mx,my):
        if click:
            col = screen.get_at((mx,my))
                
    omx,omy = mx,my
    ocmx,ocmy = omx-260,omy-25
    display.flip()
    myClock.tick(1000)
    
quit()
