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
# Copy and paste the code from your Sandbox once you've completed the challenge
speed(0)
outerSquare=350
cornerSize=20

def draw_border():
    penup()
    goto(-175,-175+cornerSize)
    seth(270)
    pendown()
    color("red")
    begin_fill()
    for i in range(4):
        circle(cornerSize,90,10)
        forward(350-(cornerSize*2))
    end_fill()
    penup()
    
def draw_screen():
    penup()
    goto(-150,150)#start
    pendown()
    color("light grey")
    begin_fill()
    for i in range(2):
        pendown()
        forward(300)
        right(90)
        forward(250)
        right(90)
    end_fill()    
    penup()

def draw_knob():
    radius = 25
    circleY = -135
    circle1X = -125
    circle2X =  125
    color("white")
    for i in range(2):
        if i == 0:
            goto(circle1X, circleY - radius)
        else:
            goto(circle2X, circleY - radius)
       
        pendown()
        begin_fill()
        circle(radius)
        end_fill()
        penup()  
 
def draw_triangles(): 
    # Left Arrow
    goto(-165,-135)
    seth(270)#left
    pendown()
    color("gold")
    begin_fill()
    goto(-155,-130)
    goto(-155, -140)
    goto(-165, -135)
    end_fill()
    penup()
    
    # Right Arrow
    goto(-85,-135)
    seth(270)#left
    pendown()
    color("gold")
    begin_fill()
    goto(-95,-140)
    goto(-95, -130)
    goto(-85, -135)
    end_fill()
    penup()
    
    # Down Arrow
    goto(85,-130)
    seth(270)#left
    pendown()
    color("gold")
    begin_fill()
    goto(90,-140)
    goto(95, -130)
    goto(85, -130)
    end_fill()
    penup()
    
    # Right Arrow
    goto(160, -130)
    seth(270)#left
    pendown()
    color("gold")
    begin_fill()
    goto(165,-140)
    goto(155, -140)
    goto(160, -130)
    end_fill()
    penup()

def draw_label():
    goto(0,-145)
    color("gold")
    write("Etch A Sketch",align="center",font=("Brush Script MT", 20))
    color("black")


# Outer Square
draw_border()
seth(0)#Right
draw_screen()
draw_knob()
draw_triangles()

draw_label()
goto(0,0)

# If running as script (not imported), wait for click to exit
if __name__ == "__main__" and created:
    screen.exitonclick()
