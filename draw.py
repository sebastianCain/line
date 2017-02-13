from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
    x = x0
    y = y0
    A = y1 - y0
    B = -(x1 - x0)
    d = (2 * A) + B
    A *= 2
    B *= 2
    while x <= x1:
        plot(screen, color, x, y)
        if d > 0:
            y += 1
            d += B
        x += 1
        d += A
