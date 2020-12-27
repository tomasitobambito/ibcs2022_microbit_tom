from microbit import *
import random

class Light: #custom light commands for easier understanding and automation with arrays
    def on(colour):
        if colour == 1:
            pin13.write_digital(1)
        elif colour == 2:
            pin14.write_digital(1)
        else:
            pin15.write_digital(1)
    
    def off(colour):
        if colour == 1:
            pin13.write_digital(0)
        elif colour == 2:
            pin14.write_digital(0)
        else:
            pin15.write_digital(0)

class Game: #contains all variables and functions for the main game part
    combination = []
    playerInput = []
    integer = 0

    def __init__(self, length): #creates initial combination
        i = 0
        while i < length:
            integer = random.randint(1, 3)
            if len(self.combination) >= 2:
                if self.combination[i - 2] == integer and self.combination[i - 1] == integer: #checks if a number is repeating more than twice
                    continue
            self.combination.append(integer)
            i += 1
    
    def hardReset(self, length): #used on failed attempt to reset variables and create new combination
        self.combination = []
        self.playerInput = []
        i = 0
        while i < length:
            integer = random.randint(1, 3)
            if len(self.combination) >= 2:
                if self.combination[i - 2] == integer and self.combination[i - 1] == integer:
                    continue
            self.combination.append(integer)
            i += 1
    
    def increment(self): #increments combination by 1
        while True:
            integer = random.randint(1, 3)
            if self.combination[-2] == integer and self.combination[-1] == integer: #checks if a number is repeating more than twice
                continue
            self.combination.append(integer)
            break
        self.playerInput = [] #resets input
    
    def verifyInput(self, index):
        if self.combination[index] != self.playerInput[index]:
            return False
        return True

gameObj = Game(3)
success = True

while True:
    for n in range(7): #eventual combination length of 9

        #display combination
        for j in gameObj.combination:
            Light.on(j)
            sleep(1000)
            Light.off(j)
            sleep(500)

        i = 0 #defines and resets counter

        #user tries to guess combination
        while i < (n + 3):
            if pin0.is_touched():
                gameObj.playerInput.append(1)
                if not gameObj.verifyInput(i):
                    success = False
                    break
                i += 1
                sleep(500)
            if pin1.is_touched():
                gameObj.playerInput.append(2)
                if not gameObj.verifyInput(i):
                    success = False
                    break
                i += 1
                sleep(500)
            if pin2.is_touched():
                gameObj.playerInput.append(3)
                if not gameObj.verifyInput(i):
                    success = False
                    break
                i += 1
                sleep(500)
        
        #restarts game on unsuccessful try 
        if not success:
            Light.on(1)
            sleep(4000)
            Light.off(1)
            sleep(2000)
            gameObj.hardReset(3)
            break

        #increment to next combination
        gameObj.increment()

    #win condition; ends game
    if success:
        Light.on(3)
        break

    success = True #resets success variable after failed attempt
