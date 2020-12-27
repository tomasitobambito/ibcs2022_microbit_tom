from microbit import *

while True:
    temp = temperature()
    if temp > 21:   
        pin16.write_digital(1)
    else:
        pin16.write_digital(0)