"""Simple launcher UI that shows buttons at the bottom of the screen.

Click a button to run the corresponding module's main(screen) function.
"""
from turtle import Screen, Turtle
import sys


def make_button(t, x, y, w, h, label, cb):
    """Draw a rectangular button with label and attach a click callback.

    t: Turtle used for drawing
    cb: function(screen) -> None
    """
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("lightgray")
    t.begin_fill()
    for _ in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()
    t.penup()
    t.goto(x + w/2, y + h/2 - 8)
    t.write(label, align="center", font=("Arial", 12, "normal"))


def launcher_main():
    # Set up the main screen
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.title("EtchASketch Launcher")
    screen.tracer(0)  # Turn off animation for setup

    # Create button drawer turtle
    drawer = Turtle(visible=False)
    drawer.hideturtle()
    drawer.speed(0)

    # Button layout (three example slots) along bottom
    btn_w, btn_h = 140, 36
    spacing = 20
    total_w = btn_w * 3 + spacing * 2
    start_x = -total_w/2
    y = -260

    def clear_drawing_area():
        """Clear everything except bottom button area."""
        # Reset all turtles except our button drawer
        for turtle in screen.turtles():
            if turtle != drawer:
                turtle.reset()
                turtle.hideturtle()
        screen.update()

    def run_etch(s):
        """Run the etch-a-sketch program."""
        clear_drawing_area()
        
        # Remove any existing import so we can reload fresh
        module_name = 'etch_a_sketch.etchASketch'
        if module_name in sys.modules:
            del sys.modules[module_name]
        
        # Temporarily enable animation for the drawing
        screen.tracer(1)
            
        # Set screen before importing so module uses our screen
        import etch_a_sketch.etchASketch as sketch_module
        sys.modules[module_name].LAUNCHER_SCREEN = screen
        
        # Clean up and restore UI state
        screen.tracer(0)  # Turn off animation for UI updates
        screen.update()
        draw_buttons()
        
        # Clean up module for next time
        if module_name in sys.modules:
            del sys.modules[module_name]

    # Draw the buttons
    def draw_buttons():
        drawer.clear()
        drawer.penup()
        make_button(drawer, start_x, y, btn_w, btn_h, "EtchASketch", run_etch)
        make_button(drawer, start_x + btn_w + spacing, y, btn_w, btn_h, 
                   "Placeholder", lambda s: None)
        make_button(drawer, start_x + 2*(btn_w + spacing), y, btn_w, btn_h,
                   "Placeholder", lambda s: None)
        screen.update()

    # Simple click handler: translate clicks to which button and call callback
    buttons = [
        (start_x, y, btn_w, btn_h, run_etch),
        (start_x + (btn_w + spacing), y, btn_w, btn_h, lambda s: None),
        (start_x + 2*(btn_w + spacing), y, btn_w, btn_h, lambda s: None),
    ]

    def on_click(x, y):
        for bx, by, bw, bh, cb in buttons:
            if bx <= x <= bx + bw and by <= y <= by + bh:
                cb(screen)

    # Set up initial state
    screen.onclick(on_click)
    draw_buttons()
    screen.update()
    screen.mainloop()


if __name__ == "__main__":
    launcher_main()
