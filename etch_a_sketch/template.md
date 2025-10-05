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


# If running as script (not imported), wait for click to exit
if __name__ == "__main__" and created:
    screen.exitonclick()