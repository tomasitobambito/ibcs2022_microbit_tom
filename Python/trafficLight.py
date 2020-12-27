from microbit import *

# turns on one red and one green light
pin14.write_digital(1)
pin15.write_digital(1)

while True:
    if button_a.is_pressed():
        sleep(5000)
        pin16.write_digital(1)
        sleep(5000)
        pin15.write_digital(0)
        sleep(2000)
        pin14.write_digital(0)
        pin13.write_digital(1)
        sleep(10000)
        pin13.write_digital(0)
        pin14.write_digital(1)
        sleep(5000)
        pin15.write_digital(1)
        sleep(3000)
        pin16.write_digital(0)
