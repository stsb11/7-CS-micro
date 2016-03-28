# Multiplication table show-er
# ----------------------------

# Use GPIO 0 and 2 to choose a table.
# Then use A and B buttons to browse the table you've chosen.
from microbit import *
table = 1
timesWhat = 1

display.scroll("Choose table")
while True:

    if pin0.is_touched() and table>1:
        table -= 1
        timesWhat = 1
        display.scroll(str(table) + "x") 
    elif pin2.is_touched() and table<12:
        table += 1
        timesWhat = 1
        display.scroll(str(table) + "x")

    if button_a.is_pressed() and timesWhat > 1:
        timesWhat -= 1
        result= table * timesWhat
        display.scroll(str(result))
    if button_b.is_pressed() and timesWhat < 12:
        timesWhat += 1
        result= table * timesWhat
        display.scroll(str(result))
