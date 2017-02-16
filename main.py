from display import *
from draw import *
import random

screen = new_screen()
color = [ 0, 255, 0 ]
for i in range(100):
    draw_line(screen, 250, 250, int(random.random() * 500), int(random.random() * 500), color)  
'''
draw_line(screen, 250, 250, 100, 0, color)
draw_line(screen, 120, 0, 250, 250, color)
'''
color = [ 255, 0, 255 ]
draw_line(screen, 250, 250, 0, 0, color)
draw_line(screen, 250, 250, 0, 250, color)
draw_line(screen, 250, 250, 0, 500, color)
draw_line(screen, 250, 250, 250, 500, color)
draw_line(screen, 250, 250, 500, 500, color)
draw_line(screen, 250, 250, 500, 250, color)
draw_line(screen, 250, 250, 500, 0, color)
draw_line(screen, 250, 250, 250, 0, color)

display(screen)
save_extension(screen, 'img.png')
