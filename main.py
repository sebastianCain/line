from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
for i in range(25):
    draw_line(screen, 0, 0, 500, i*20, color)  

display(screen)
save_extension(screen, 'img.png')
