
import random
import time
from pprint import pprint


class hero:
    def __init__ (self, Hhealth, Hattack, Hluck, Hranged, Hdefense, Hmagic, Hname):
        self.health = Hhealth
        self.attack = Hattack
        self.luck = Hluck
        self.ranged = Hranged
        self.defense = Hdefense
        self.magic = Hmagic
        self.name = Hname

        def getHealth(self):
            return self.health
        def getAttack(self):
            return self.attack
        def getLuck(self):
            return self.luck
        def getRanged(self):
            return self.ranged
        def getDefense(self):
            return self.defense
        def getMagic(self):
            return self.magic
        def getName(self):
            return self.name
        
        def setHealth(self, newHealth):
            self.health = newHealth
        def setAttack(self, newAttack):
            self.attack = newAttack
        def setLuck(self, newLuck):
            self.luck = newLuck
        def setRanged(self, newRanged):
            self.ranged = newRanged
        def setDefense(Self, newDefense):
            self.defense = newDefense
        def setMagic(self, newMagic):
            self.magic = newMagic
        def setName(self, newName):
            self.name = newName

def createClass():
    a = input("Are you more strategic(1) or more of a warrior(2)?...")
    while a!= "1" and a!= "2":
        print("invalid selection")
        a = input("Are you more strategic(1) or more of a warrior(2)?...")
    if a == "1":
        heroAttack = 50
        heroDefense = 100
    elif a == "2":
        heroAttack = 100
        heroDefense = 50
    
    b = input("Press ENTER to roll the dice...")
    time.sleep(0.2)
    print ("Rolling dice...")
    heroLuck = random.randint(0, 10)
    print("Your hero has", heroLuck, " Luck out of 10.")

    c = input("Are you more of a bowyer(1) or a magician(2)?...")
    while c != "1" and c != "2":
        print("invalid selection")
        c = input("Are you more of a bowyer(1) or a magician(2)?")
    if c == "1":
        heroRanged = 100
        heroMagic = 50
    elif c == "2":
        heroRanged = 50
        heroMagic = 100
    
    heroName = input("What is your name?")
    print("Welcome ", heroName, "!")

    return (heroName, heroAttack, heroDefense, heroLuck, heroRanged, heroDefense, heroMagic)

class_data = createClass()

character = hero(100, class_data[0], class_data[1], class_data[2], class_data[3], class_data[4], class_data[5])
pprint(vars(character))
        