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
speed(200)

# Outer Square
penup()
goto(-175,175)
pendown()
seth(360)
for i in range(4):
    forward(350)
    right(90)

penup()
seth(0)#Right

# Inner Square
penup()
goto(-150,150)#start
pendown()

for i in range(2):
    pendown()
    forward(300)
    right(90)
    forward(250)
    right(90)
    
penup()
   
radius = 25
circleY = -135
circle1X = -125
circle2X =  125

for i in range(2):
    if i == 0:
        goto(circle1X, circleY - radius)
    else:
        goto(circle2X, circleY - radius)
    pendown()
    circle(radius)
    penup()


# Left Arrow
goto(-165,-135)
seth(270)#left
pendown()
goto(-155,-130)
goto(-155, -140)
goto(-165, -135)
penup()

# Right Arrow
goto(-85,-135)
seth(270)#left
pendown()
goto(-95,-140)
goto(-95, -130)
goto(-85, -135)
penup()

# Down Arrow
goto(85,-130)
seth(270)#left
pendown()
goto(90,-140)
goto(95, -130)
goto(85, -130)
penup()

# Right Arrow
goto(160, -130)
seth(270)#left
pendown()
goto(165,-140)
goto(155, -140)
goto(160, -130)
penup()
goto(0,0)

# If running as script (not imported), wait for click to exit
if __name__ == "__main__" and created:
    screen.exitonclick()