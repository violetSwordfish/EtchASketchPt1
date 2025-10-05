# EtchASketchPt1

A small Python Turtle drawing script created for "Tracy's world" that renders an Etch A Sketch-like frame and some basic shapes and arrows. The main script is `etchASketch.py` and uses the built-in `turtle` module.

## Requirements

- Python 3.7+ (recommended 3.8+)
- Uses only the Python standard library (`turtle`).

## How to run

Open a terminal and run:

```bash
python3 etchASketch.py
```

On macOS, the Turtle graphics window will open and display the drawing. The script calls `exitonclick()` so click the window to close it.

## What it does

- Draws an outer square and an inner rectangle using the turtle API
- Draws two small circles and several arrow-like shapes
- Sets a high turtle speed so the drawing completes quickly

## Notes and suggestions

- This script was created specifically for "Tracy's world" and draws the frame and controls intended for that environment.
- If you want to modify the drawing, edit `etchASketch.py` with your preferred coordinates and drawing commands.
- If running inside an environment without a display (headless server), Turtle will not open a window; run locally on a machine with GUI support.
