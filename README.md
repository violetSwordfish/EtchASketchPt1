# EtchASketchPt1

A Python Turtle Graphics project featuring an Etch A Sketch-like drawing and a launcher interface for running multiple turtle examples. The main drawing script is `etchASketch.py` and uses the built-in `turtle` module.

## Features

- Interactive launcher interface with buttons
- Etch A Sketch-style frame drawing
- Modular design allowing multiple examples to be added
- Clean screen management between examples
- Animated drawing with configurable speed

## Requirements

- Python 3.7+ (recommended 3.8+)
- Uses only the Python standard library (`turtle`)

## Project Structure

- `launcher.py` - Main entry point with button interface
- `etch_a_sketch/etchASketch.py` - Etch A Sketch drawing implementation
- `utils/screen_setup.py` - Shared screen management utilities

## How to Run

You can run either the launcher or the Etch A Sketch directly:

### Using the Launcher (Recommended)

```bash
python3 launcher.py
```

This will open the launcher window with buttons at the bottom. Click the "EtchASketch" button to run the drawing. You can click it multiple times to redraw.

### Running Etch A Sketch Directly

```bash
python3 etch_a_sketch/etchASketch.py
```

## What it Does

The Etch A Sketch example:
- Draws an outer square frame
- Creates an inner rectangle drawing area
- Adds control circles and directional arrows
- Sets a sky blue background
- Uses animated drawing with configurable speed

The launcher:
- Provides a clean interface with buttons
- Manages screen clearing between runs
- Preserves UI elements while examples run
- Handles proper cleanup between examples

## Technical Details

- Uses Python's module system for clean imports
- Manages turtle screen state properly
- Supports shared screen usage between launcher and examples
- Handles animation speed control
- Preserves UI elements while clearing drawing area

## Notes and Suggestions

- The launcher is designed to be extensible - new examples can be added easily
- Each example can control its own background color and drawing speed
- The Etch A Sketch code is intentionally kept flat (without functions) for easy learning and modification
- Examples run with animation enabled for visual interest
- If running inside an environment without a display (headless server), Turtle will not open a window; run locally on a machine with GUI support
