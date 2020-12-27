from microbit import *
import random

class Light:
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

class Game:
    combination = []
    playerInput = []
    integer = 0

    def __init__(self, length):
        i = 0
        while i < length:
            integer = random.randint(1, 3)
            if len(self.combination) >= 2:
                if self.combination[i - 2] == integer and self.combination[i - 1] == integer:
                    continue
            self.combination.append(integer)
            i += 1
    
    def reset(self, length):
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
    
    def increment(self):
        while True:
            integer = random.randint(1, 3)
            if self.combination[len(self.combination) - 2] != integer and self.combination[len(self.combination) - 1] != integer:
                self.combination.append(integer)
                break
    
    def verifyInput(self, index):
        if self.combination[index] != self.playerInput[index]:
            return False
        return True

gameObj = Game(3)

i = 0

for j in gameObj.combination:
    Light.on(j)
    sleep(1000)
    Light.off(j)
    sleep(500)

while i < 3:
    if pin0.is_touched():
        gameObj.playerInput.append(1)
        if not gameObj.verifyInput(i):
            Light.on(1)
            break
        i += 1
        sleep(500)
    if pin1.is_touched():
        gameObj.playerInput.append(2)
        if not gameObj.verifyInput(i):
            Light.on(1)
            break
        i += 1
        sleep(500)
    if pin2.is_touched():
        gameObj.playerInput.append(3)
        if not gameObj.verifyInput(i):
            Light.on(1)
            break
        i += 1
        sleep(500)
