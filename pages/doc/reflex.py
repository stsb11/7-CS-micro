# Reflex testing game.
# After a random interval, the display will change
# Which player will hit A or B first?

from microbit import *
import random

random.seed()

while True:
    targetTime = random.randint(3, 6)
    display.show(Image.MEH)
    
    while targetTime > 1:
        targetTime -=1
        sleep(1000)
        if button_a.is_pressed() or button_b.is_pressed():
            display.show(Image.SAD)
    
    while button_a.is_pressed() == False and button_b.is_pressed() == False:
        display.show(Image.HAPPY)

    if button_a.is_pressed():
        display.show("A")
    elif button_b.is_pressed():
        display.show("B")
            
    sleep(2000)
    display.clear()
