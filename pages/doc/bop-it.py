# Bop-it style game.

# User must push either A, B or GPIO 0, 1 or 2.
# The amount of time allowed to respond to the instructions  slowly decreases.
# Score shown at the end. 

# The accelerometer code is a bit flaky, but can be re-enabled by changing the randint() line to pick from 1-6 rather than 1-5.  
from microbit import *
import random

def pickMove():
    nextMove = random.randint(1, 5)
    if nextMove == 1:
        showAction="A"
    if nextMove == 2:
        showAction="B"
    if nextMove == 3:
        showAction="0"
    if nextMove == 4:
        showAction="1"
    if nextMove == 5:
        showAction="2"
    if nextMove == 6:
        showAction="S"
        
    return nextMove, showAction

def checkAnswer(currMove):
    gotItRight = True
    gesture = accelerometer.current_gesture()
    print(gesture)
    if button_a.is_pressed() and currMove == 1:
        display.show(Image.HAPPY)
    elif button_b.is_pressed() and currMove == 2:
        display.show(Image.HAPPY)
    elif pin0.is_touched() and currMove == 3:
        display.show(Image.HAPPY)
    elif pin1.is_touched() and currMove == 4:
        display.show(Image.HAPPY)
    elif pin2.is_touched() and currMove == 5:
        display.show(Image.HAPPY)
    elif gesture == "shake" and currMove == 6:
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)
        gotItRight = False
    
    sleep(1500)
    display.clear()
    return gotItRight
    
random.seed()
score=0
level=250

display.scroll("3")
display.scroll("2")
display.scroll("1")
display.scroll("Go!")

while True:
    currMove, showAction = pickMove()
    countdown = level
    level -= 10
    
    while countdown > 0 and button_a.is_pressed() == False and button_b.is_pressed() == False and pin0.is_touched() == False and pin1.is_touched() == False and pin2.is_touched() == False and accelerometer.was_gesture("shake") == False:
        display.show(showAction)
        sleep(1)
        countdown -=1
    
    if countdown == 0:
        break
        
    if checkAnswer(currMove) == True:
        score += 1
    else:
        break

while True:
    display.show(Image.SAD)
    sleep(2000)
    display.scroll(str(score))
