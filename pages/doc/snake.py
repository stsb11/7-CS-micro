# Simple snake style game. 
from microbit import *
x = 2
y = 2

while True:
    display.set_pixel(x, y, 7)

    readingX = accelerometer.get_x()
    readingY = accelerometer.get_y()

    if readingX > 60 and x<4:
        x += 1
    elif readingX < -60 and x>0:
        x -= 1

    if readingY > 60 and y<4:
        y += 1
    elif readingY < -60 and y>0:
        y -= 1
        
    sleep(500)
