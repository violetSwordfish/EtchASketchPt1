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


##Code Here
speed(500)
radius_choice=int(input("what is the range of the bulleye? (1-30): "))
def draw_bulleye():
    radius = radius_choice
    for i in range(4):
        print(4-i)
        circle_i = 4-i
        print(radius*circle_i)
        color_choice=str(input("what is the color of the bulleye? (blue orange yellow red): "))
        color(color_choice)
        pendown()
        begin_fill()
        seth(0)
        circle(radius*circle_i, 360, 999)
        end_fill()
        penup()
        seth(90)
        forward(radius_choice)
        
        
penup()
setposition(0,-radius_choice*4)
#penup()
#seth(270)
#forward(25)
#seth(0)
draw_bulleye()

# If running as script (not imported), wait for click to exit
if __name__ == "__main__" and created:
    screen.exitonclick()