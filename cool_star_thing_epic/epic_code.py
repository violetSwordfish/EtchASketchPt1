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


##Code Here#
#Functions
def draw_star(size):
    pendown()
    seth(288)
    begin_fill()
    for i in range(5):
        forward(size) #Note: The size variable is used to control the star's size
        right(180-36)
    end_fill()
    penup()

def draw_whole_star(size):
    colors = ["black","red","yellow"]
    for i in range(3):
        color(colors[i])
        draw_star(size)
        seth(270)
        forward(50)
        size += -100

#Main Code
penup()
size = 400
bgcolor("#8bacaa") #Replace with a hex code from your chosen color palette if you want to
speed(0)
seth(90)
forward(200)
   
draw_whole_star(size)

# If running as script (not imported), wait for click to exit
if __name__ == "__main__" and created:
    screen.exitonclick()