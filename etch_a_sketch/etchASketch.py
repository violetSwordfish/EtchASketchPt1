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
speed(10)
bgcolor("#87ceeb")  # Sky blue
# Outer Square
penup()
goto(-175,175)
pendown()
heading = 360
for i in range(4):
    seth(heading)
    forward(350)
    heading = heading - 90

penup()
seth(0)  # Right

# Inner Square
penup()
goto(-150,150)  # start
pendown()
forward(300)
seth(270)  # Down
forward(250)
seth(180)  # left
forward(300)
seth(90)
forward(250)
penup()
seth(0)  # Right

# circle C
goto(-125,-160)
pendown()
circle(25)
penup()

# Left Arrow
goto(-165,-135)
seth(270)  # left
pendown()
goto(-155,-130)
goto(-155, -140)
goto(-165, -135)
penup()

# Right Arrow
goto(-85,-135)
seth(270)  # left
pendown()
goto(-95,-140)
goto(-95, -130)
goto(-85, -135)
penup()

# circle D
goto(100,-135)
pendown()
circle(25)
penup()

# Down Arrow
goto(85,-130)
seth(270)  # left
pendown()
goto(90,-140)
goto(95, -130)
goto(85, -130)
penup()

# Right Arrow
goto(160, -130)
seth(270)  # left
pendown()
goto(165,-140)
goto(155, -140)
goto(160, -130)
penup()
goto(0,0)

# If running as script (not imported), wait for click to exit
if __name__ == "__main__" and created:
    screen.exitonclick()