from turtle import *
import random
from pathlib import Path
import sys

# Ensure project root is on sys.path so root-level packages like `utils`
# can be imported even when running this script from inside the package.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import utils.screen_setup as screen_setup

# Set up turtle screen (use provided screen if called from launcher)
screen, created = screen_setup.setup(globals(), getattr(sys.modules[__name__], 'LAUNCHER_SCREEN', None))

#Code Goes Here
import random

speed(0)
def draw_bolt():
    pendown()
    color("#fffeb5")
    boltLength = random.randint(20,40)
    seth(random.randint(260,275))
    pensize(random.randint(1,4))
    for i in range(6):
        forward(boltLength)
        left(random.randint(20,40))
        forward(boltLength)
        right(random.randint(20,40))
        forward(boltLength-10)
        right(random.randint(20,40))
        forward(boltLength-15)
        left(random.randint(20,40))
        
    penup()

def draw_orange(size):
    pendown()
    seth(random.randint(0,360))
    begin_fill()
    color("#ebad13")
    circle(size)
    end_fill()
    color("#23b019")
    pensize(size/2+1)
    forward(size/3+1)
    pensize(2)
    penup()
    backward(10)

def draw_cloud(length, cloudBumps=3):
    cloudHeightDivisor = 10
    cloudLength = length
    cloudHeight = cloudLength/cloudHeightDivisor
    bumpDiamator = cloudLength/cloudBumps
    bumpRadius = bumpDiamator/2
    pendown()
    color("#dfe6f5")
    begin_fill()
    seth(0)
    forward(cloudLength)
    circle(cloudHeight,180,50)
    for i in range(cloudBumps):
        seth(90)
        circle(bumpRadius,180,50)
    seth(180)
    circle(cloudHeight,180,50)
    end_fill()
    penup()
    
def draw_cloud_outline(length, cloudBumps=3):
    cloudHeightDivisor = 10
    cloudLength = length
    cloudHeight = cloudLength/cloudHeightDivisor
    bumpDiamator = cloudLength/cloudBumps
    bumpRadius = bumpDiamator/2
    print(cloudHeight)
    pendown()
    pensize(2)
    color("black")
    seth(0)
    forward(cloudLength)
    circle(cloudHeight,180,50)
    for i in range(cloudBumps):
        seth(90)
        circle(bumpRadius,180,50)
    seth(180)
    circle(cloudHeight,180,50)
    penup()
    pensize(1)
    
def draw_cloud_with_outline(length, cloudBumps=3):
    draw_cloud(length, cloudBumps)
    draw_cloud_outline(length, cloudBumps)
    
def draw_orange_rain(cloudLength, startX):
    orangeSize = (cloudLength/18) +1
    for y in range(1,100,20):
        randomX = random.randint(40,100)
        for x in range(1,cloudLength, randomX):
            seth(0)
            setx(startX+x)
            draw_orange(orangeSize)
        seth(270)
        forward(y+random.randint(20,50))
        setx(startX)
                
#draw rectangle
def draw_rectangle(width, height, rectColor):
    pendown()
    color(rectColor)
    begin_fill()
    seth(0)
    forward(width)
    left(90)
    forward(height)
    left(90)
    forward(width)
    left(90)
    forward(height)
    end_fill()
    penup()
    
#Start
bgcolor("#bbcbed")
penup()
pensize(2)



#Draw Cloud 1
goto(-200,150)
draw_orange_rain(80, -200)
goto(-200,150)
draw_cloud_with_outline(80)

#Draw Cloud 2
goto(-150,150)
draw_orange_rain(100, -150)
goto(-150,150)
draw_cloud_with_outline(100)

#Draw Cloud 3
goto(-90,150)
draw_cloud_with_outline(80)

#Draw Cloud 4
goto(10,150)
draw_orange_rain(160, 10)
goto(10,150)
draw_cloud_with_outline(160)

#Draw Cloud 5 With Lightning
goto(100,150)
draw_bolt()
goto(110,150)
draw_bolt()
goto(130,150)
draw_bolt()
goto(160,150)
draw_bolt()
goto(180,150)
draw_bolt()
goto(200,150)
draw_bolt()
goto(100,150)
draw_cloud_with_outline(120)

goto(-200,-200)
draw_rectangle(400, 60, "black")
goto(-192,-192)
draw_rectangle(384, 44, "silver")
goto(-190,-190)
draw_rectangle(380, 40, "#ebb52f")
color("white")
penup()
goto(-200,-200)
forward(-100)
left(90)
forward(200)
left(-90)
goto(0,-175)
seth(0)
write("Orange Rain", align="center", font=("Fantasy",20))
#Move Tracy Away
goto(-2000,-2000)

# If running as script (not imported), wait for click to exit
if __name__ == "__main__" and created:
    screen.exitonclick()