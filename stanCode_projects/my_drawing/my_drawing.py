"""
File: my_drawing.py
Name: Luke
----------------------
TODO:
"""

import math
from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gcolor import GColor
from campy.graphics.gwindow import GWindow

# Declare constants
SIDES = 4                                                           # Canvas is rectangle.
SEGMENTS = 6                                                        # Segments for each side.
LINES = 51                                                          # Best if factor of 255, lower renders faster.
INCREMENT = 255//LINES                                              # Calculate increment amount for rgb values.

# Declare globals
canvas_size = SEGMENTS * LINES
window = GWindow(canvas_size, canvas_size, title='my_drawing.py')   # Canvas size is segment count times line count.
center_x = window.width // 2                                        # Calculate center point for each line to end at.
center_y = window.height // 2


def main():
    """
    This program might take half a minute to finish,
    it draws an abstract tunnel,
    using loops and incrementing rgb values for walls and white circles simulating distance.
    """
    lines()
    circles()


def lines():
    """
    Draw lines from each side to center, alternating fade in each segment to create pattern.
    :return: Nothing.
    """
    for i in range(0, SEGMENTS * SIDES):                            # Start loop for total segments.
        for x in range(0, LINES):                                   # Start loop for lines in segment.
            if i // SEGMENTS == 0:                                  # Top side start points: x increment, y at top.
                start_x = i % SEGMENTS * LINES + x                      # Increment starts after adding prior segment.
                start_y = 0
            elif i // SEGMENTS == 1:                                # Right side start points: x at right, y increment.
                start_x = window.width
                start_y = i % SEGMENTS * LINES + x
            elif i // SEGMENTS == 2:                                # Bottom side start points: x decrement, y bottom.
                start_x = window.width - (i % SEGMENTS * LINES + x)     # Decrements by subtracting from edge.
                start_y = window.height
            elif i // SEGMENTS == 3:                                # Left side start points: x at left, y decrement.
                start_x = 0
                start_y = window.height - (i % SEGMENTS * LINES + x)
            end_x = center_x                                        # End points for line fixed at canvas center.
            end_y = center_y
            if i % 2 == 1:                                          # Odd segments increment rgb values
                rgb = x * INCREMENT
            else:                                                   # Even segments decrement instead
                rgb = LINES * INCREMENT - x * INCREMENT
            line = GLine(start_x, start_y, end_x, end_y)
            line.color = GColor(rgb, rgb, rgb)
            window.add(line)
    return


def circles():
    """
    Draw circles in Fibonacci sequence.
    :return: Nothing.
    """
    m = 1                                                           # First number.
    n = 1                                                           # Second number.
    max_n = math.sqrt(window.width**2/2) * 2                        # Use window width to calculate max diameter needed.
    while n <= max_n:
        fib = m+n
        circle = GOval(fib, fib)
        circle.color = 'white'
        circle.x = center_x - fib//2                                # Center circle.
        circle.y = center_y - fib//2
        window.add(circle)
        m = n                                                       # Update first number with second number.
        n = fib                                                     # Update second number with sum.
    return


if __name__ == '__main__':
    main()
