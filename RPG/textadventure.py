import random

# HERO CLASSES
class knight (object):
    health = 30
    tempHealth = 30
    strength = 10
    dexterity = 6
    intelligence = 3
    pdefense = 10
    mdefense = 3
    accuracy = 100
    reflex = 3
    luck = 5
    gold = 0
    name = "Knight"
    meleeEquipped = None
    rangedEquipped = None
    magicEquipped = None
    armorEquipped = None
    accessoryEquipped = None
    patkMod = 0
    ratkMod = 0
    matkMod = 0
    location = 0
    progress = 0

class hunter (object):
    health = 25
    tempHealth = 25
    strength = 6
    dexterity = 10
    intelligence = 5
    pdefense = 7
    mdefense = 6
    accuracy = 8
    reflex = 10
    luck = 5
    gold = 0
    name = "Hunter"
    meleeEquipped = None
    rangedEquipped = None
    magicEquipped = None
    armorEquipped = None
    accessoryEquipped = None
    patkMod = 0
    ratkMod = 0
    matkMod = 0
    location = 0
    progress = 0

class scholar (object):
    health = 20
    tempHealth = 20
    strength = 3
    dexterity = 6
    intelligence = 10
    pdefense = 5
    mdefense = 10
    accuracy = 5
    reflex = 6
    luck = 5
    gold = 0
    name = "Scholar"
    meleeEquipped = None
    rangedEquipped = None
    magicEquipped = None
    armorEquipped = None
    accessoryEquipped = None
    patkMod = 0
    ratkMod = 0
    matkMod = 0
    location = 0
    progress = 0

# ENEMY CLASSES
class carrionCrow (object):
    name = "Carrion Crow"
    health = 10
    tempHealth = 10
    intro = "A giant, black crow feasts on fetid flesh, and eyes you hungrily."
    strength = 3
    dexterity = 6
    intelligence = 0
    pdefense = 3
    mdefense = 0
    accuracy = 6
    reflex = 4
    luck = 2
    rarity = 0

class desperateVagrant (object):
    name = "Desperate Vagrant"
    health = 12
    tempHealth = 12
    intro = "An emaciated vagrant steps out from the shadows and pulls a wicked knife on you."
    strength = 5
    dexterity = 1
    intelligence = 0
    pdefense = 5
    mdefense = 1
    accuracy = 3
    reflex = 3
    luck = 1
    rarity = 0

class rottedHound (object):
    name = "Rotted Hound"
    health = 15
    tempHealth = 15
    intro = "Flayed and wretched, a hound snarls at you viciously."
    strength = 7
    dexterity = 5
    intelligence = 0
    pdefense = 5
    mdefense = 0
    accuracy = 4
    reflex = 6
    luck = 5
    rarity = 1

class mugger (object):
    name = "Mugger"
    health = 20
    tempHealth = 20
    intro = "A dark figure, his face concealed, draws a wicked knife on you."
    strength = 10
    dexterity = 5
    intelligence = 2
    pdefense = 9
    mdefense = 3
    accuracy = 8
    reflex = 8
    luck = 7
    rarity = 2

class heretic (object):
    name = "Heretic"
    health = 20
    tempHealth = 20
    intro = "Ominous chants and strange lights emanate from a shadowy figure as he reaches out for you."
    strength = 4
    dexterity = 6
    intelligence = 10
    pdefense = 5
    mdefense = 12
    accuracy = 6
    reflex = 6
    luck = 8
    rarity = 2

class infantDeepOne (object):
    name = "Infant Deep One"
    health = 25
    tempHealth = 25
    intro = "A black sludge takes a vaguely humanoid form and lashes out at you."
    strength = 14
    dexterity = 10
    intelligence = 4
    pdefense = 15
    mdefense = 5
    accuracy = 8
    reflex = 10
    luck = 10
    rarity = 3

# GAME-START FUNCTIONS
def intro():
    print("#"*80)
    print("##","."*74, "##")
    print("##", "."*19, "P L A G U E - IN - P E R G A M U M", "."*19, "##")
    print("##","."*74, "##")
    print("#"*80)
    print("##","."*74, "##")
    print("##...", "You've come to the great city, PERGAMUM, in search of a cure for the", "...##")
    print("##.....", "ROTTED PLAGUE. It has devastated your homeland, and rumor has it", ".....##")
    print("##....", "that a cure had been found by the MINISTRY OF MEDICINE here in the", "....##")
    print("##...", "city. But PERGAMUM collapsed after the plague ripped through it, and", "...##")
    print("##.....", "now the cure, if it even exists, remains lost somewhere inside.", "......##")
    print("##","."*74, "##")
    print("##","."*74, "##")
    print("##...", "An annonymous contact promises to know where the cure is being kept,", "...##")
    print("##.....", "if only someone brave enough to confront the dangers of the city", ".....##")
    print("##........................", "were willing to meet him.", ".........................##")
    print("##","."*74, "##")
    print("#"*80)

def startGame():
    global character
    print("Select a Profession to begin your adventure:")
    choice = int(input("1. Knight\n2. Hunter\n3. Scholar\nSelect a Class: "))
    if choice ==1:
        character = (knight)
    elif choice ==2:
        character = (hunter)
    elif choice ==3:
        character = (scholar)
    else:
        print("Please select a Profession")
        choice = int(input("1. Knight\n2. Hunter\n3. Scholar"))
    print ("Good choice, you are a " + character.name + "!")

# INVENTORY
def inventoryWipe():
    file = open("inventory.txt", "w")
    file.close()

def inventoryShow():
    global contents
    print("You're carrying the following on your person: ")
    file = open("inventory.txt", "r")
    contents = file.read()
    contents = contents.split(",")
    print(contents)
    length = len(contents)-1
    for i in range(length):
        print(contents[i])

def lootCheck(lootX):
    file = open("inventory.txt", "r")
    contents = file.read()
    contents = contents.split(",")
    if lootX in contents:
        print("You already have this item, so you leave it behind.")
    else:
        inventory(lootX)

def inventory(lootX):
    file = open("inventory.txt" ,"a")
    file.write(str(lootX + ","))
    file.close()

def inventoryUse(decisionX, contents, lootX):
    if "Health Drop" in contents and decisionX == "Health Drop":
        print("What would you like to do with the Health Drop?")
        decision = int(input("1. Drink it. \n2. Examine it. \n3. Put it away."))
        if decision > 3:
            print("That's not an option.")
        elif decision == 1:
            print("You place the drop under your tongue and feel its rejuvinating effects right away.")
            print("You are healed for 5 points of health.")
            character.tempHealth == character.tempHealth + 5
            print("You now have ", character.tempHealth, " health.")
            inventoryDelete(decisionX)
        elif decision == 2:
            print("A dropper with a small dose of liquid. It will restore 5 points of health.")
        elif decision == 3:
            print("You put it away.")
    else:
        print("You can't seem to find that item...")
    
    if "Health Vial" in contents and decisionX == "Health Vial":
        print("What would you like to do with the Health Vial?")
        decision = int(input("1. Drink it. \n2. Examine it. \n3. Put it away."))
        if decision > 3:
            print("That's not an option.")
        elif decision == 1:
            print("You quickly drink the contents of the vial and feel your stamina return to you.")
            print("You are healed for 10 points of health.")
            character.tempHealth == character.tempHealth + 10
            print("You now have ", character.tempHealth, " health.")
            inventoryDelete(decisionX)
        elif decision == 2:
            print("A fizzy liquid in a simple vial. It will restore 10 points of health.")
        elif decision == 3:
            print("You put it away.") 
    else:
        print("You can't seem to find that item...")
    
    if "Health Syrum" in contents and decisionX == "Health Syrum":
        print("What would you like to do with the Health Syrum?")
        decision = int(input("1. Drink it.\n2. Examine it.\n3. Put it away."))
        if decision > 3:
            print("That's not an option.")
        elif decision == 1:
            print("You gulp down the syrum and suddenly your wounds stop hurting.")
            print("You are healed for 20 points of health.")
            character.tempHealth == character.tempHealth + 20
            print("You now have ", character.tempHealth, " health.")
            inventoryDelete(decisionX)
        elif decision == 2:
            print("A frothing liquid in a small jar. It will restore 20 points of health.")
        elif decision == 3:
            print("You put it away.")
    else:
        print("You can't seem to find that item...")
    
    if "Health Elixir" in contents and decisionX == "Health Elixir":
        print("What would you like to do with the Health Elixir?")
        decision = int(input("1. Drink it. \n2. Examine it. \n3. Put it away."))
        if decision > 3:
            print("That's not an option.")
        elif decision == 1:
            print("You chug the entirety of the bottle and notice your wounds healing instantly.")
            print("Your health is completely restored.")
            character.tempHealth == character.health
            print("You now have ", character.tempHealth, " health.")
            inventoryDelete(decisionX)
        elif decision == 2:
            print("A bottle of liquid that hums with energy. It will restore all of your health.")
        elif decision == 3:
            print("You put it away.")
    else:
        print("You can't seem to find that item...")
    
    if "Rusted Shortsword" in contents and decisionX == "Rusted Shortsword":
        print("What would you like to do with the Rusted Shortsword?")
        decision = int(input("1. Wield it.\n2. Examine it.\n3. Put it away."))
        if decision > 3:
            print("That's not an option. What would you like to do with the Rusted Shortsword?")
            decision = int(input("1. Wield it.\n2. Examine it.\n3. Put it away."))
        elif decision == 1:
            print("You equip the Rusted Shortsword.")
            character.meleeEquipped = None
            character.meleeEquipped = "Rusted Shortsword"
        elif decision == 2:
            print("An old shortsword that has seen considerable use.")
        elif decision == 3:
            print("You put it away.")
    else:
        print("You can't seem to find that item.")

def inventoryDelete(decisionX):
    file = open("inventory.txt", "r")
    contents = file.read()
    contents = contents.split(",")
    file.close()
    print(contents)
    if decisionX in contents:
        i = contents.index(decisionX)
        del contents[i]
        print(contents)
        print(decisionX)
        contents = contents[:-1]
        print(contents)

        file = open("inventory.txt", "w")
        for x in range (0, len(contents)):
            print(contents[x])
            file.write(contents[x] + ",")
        file.close()

# EQUIPMENT

# class equipValues:
#     def equipment(self, eType, pAtk, rAtk, mAtk, pDef, mDef, price)
#         self.equipmentType = eType
#         self.physicalAttack = pAtk
#         self.rangedAttack = rAtk
#         self.magicAttack = mAtk
#         self.physicalDefense = pDef
#         self.magicDefense = mDef
#         self.price = price

equipment = {
    'Rusted Shortsword': {
        'Type': 'Melee Weapon',
        'Physical Attack': 3,
        'Ranged Attack': 0,
        'Magic Attack': 0,
        'Physical Defense': 0,
        'Magic Defense': 0,
        'Price': 100}
}

def equipmentWipe():
    character.meleeEquipped = ""
    character.rangedEquipped = ""
    character.magicEquipped = ""
    character.armorEquipped = ""

def equipmentShow():
    if character.meleeEquipped:
        print("Melee Weapon: ", character.meleeEquipped)
    
    if character.rangedEquipped:
        print("Ranged Weapon: ", character.rangedEquipped)
    
    if character.magicEquipped:
        print("Relic: ", character.magicEquipped)
    
    if character.armorEquipped:
        print("Armor: ", character.armorEquipped)

# Looting

def loot(enemyList, enemyNo):
    file = open("loot.txt", "r")
    lootTableCommon = file.readline()
    lootTableUncommon = file.readline()
    lootTableRare = file.readline()
    lootTableUltraRare = file.readline()

    lootTableCommon = lootTableCommon.split(",")
    lootTableUncommon = lootTableUncommon.split(",")
    lootTableRare = lootTableRare.split(",")
    lootTableUltraRare = lootTableUltraRare.split(",")

    lootTableCommon = lootTableCommon[:-1]
    lootTableUncommon = lootTableUncommon[:-1]
    lootTableRare = lootTableRare[:-1]
    lootTableUltraRare = lootTableUltraRare[:-1]

    global lootX

    if enemyList[enemyNo].rarity ==0:
        length = len(lootTableCommon)-1
        lootX = str(lootTableCommon[random.randint(0, length)])
        print("The enemy has left behind a ", lootX)
        lootCheck(lootX)
    
    elif enemyList[enemyNo].rarity ==1:
        length = len(lootTableUncommon)-1
        lootX = str(lootTableUncommon[random.randint(0, length)])
        print("The enemy has left behind a ", lootX)
        lootCheck(lootX)

    elif enemyList[enemyNo].rarity ==2:
        length = len(lootTableRare)-1
        lootX = str(lootTableRare[random.randint(0, length)])
        print("The enemy has left behind a ", lootX)
        lootCheck(lootX)

    elif enemyList[enemyNo].rarity ==3:
        length = len(lootTableUltraRare)-1
        lootX = str(lootTableUltraRare[random.randint(0, length)])
        print("The enemy has left behind a ", lootX)
        lootCheck(lootX)

# Combat

def battlestate():
    battlestate = 1
    if character.location == 1:
        enemyList = [carrionCrow, desperateVagrant]
        enemyNo = random.randint(0,len(enemyList))
    attackList = [character.strength, character.intelligence, character.dexterity]
    print ("An enemy charges at you!")
    print("It's a ", enemyList[enemyNo].name, "!")
    print("You draw your weapon!")
    
    while battlestate == 1:
        decision = int(input("1. Attack\n2. Inventory\n3. Run\n"))
        if decision > 3:
            print("That's not an option.")
            decision = int(input("1. Attack\n2. Inventory\n3. Run\n"))
        elif decision == 1:
            print("How do you attack?")
            attack = int(input("1. Melee\n2. Ranged\n3. Magic\n"))
            x = attack -1
            miss = random.randint(0,5) + character.accuracy
            if miss < random.randint(0,5) + enemyList[enemyNo].reflex:
                print("Your attack missed!")
            elif miss > random.randint(0,5) + enemyList[enemyNo].reflex:
                if attack == 1:
                    damage = round(attackList[x] + character.patkMod / enemyList[enemyNo].pdefense, 2)
                    print("You swing your melee weapon and do ", damage, " damage")
                    enemyList[enemyNo].tempHealth = enemyList[enemyNo].tempHealth - damage
                    print("The enemy has ", enemyList[enemyNo].tempHealth, " health remaining.")
                    if enemyList[enemyNo].tempHealth <1:
                        print("You've slain the ", enemyList[enemyNo].name, ".")
                        enemyList[enemyNo].tempHealth = enemyList[enemyNo].health
                        battlestate = 0
                        loot(enemyList, enemyNo)
                
                elif attack == 2:
                    damage = round(attackList[x] + character.ratkMod / enemyList[enemyNo].pdefense, 2)
                    print("You attack with your ranged weapon, dealing ", damage, " damage.")
                    enemyList[enemyNo].tempHealth = enemyList[enemyNo].tempHealth - damage
                    print("the enemy has ", enemyList[enemyNo].tempHealth, " health remaining.")
                    if enemyList[enemyNo].tempHealth <1:
                        print("You've slain the ", enemyList[enemyNo].name, ".")
                        enemyList[enemyNo].tempHealth = enemyList[enemyNo].health
                        battlestate = 0
                        loot(enemyList, enemyNo)
                
                elif attack== 3:
                    damage = round(attackList[x] + character.matkMod / enemyList[enemyNo].mdefense, 2)
                    print("You fire a bolt of energy from your hands, dealing ", damage, " damage!")
                    enemyList[enemyNo].tempHealth = enemyList[enemyNo].tempHealth - damage
                    print("the enemy has ", enemyList[enemyNo].tempHealth, " health remaining.")
                    if enemyList[enemyNo].tempHealth <1:
                        print("You've slain the ", enemyList[enemyNo].name, ".")
                        enemyList[enemyNo].tempHealth = enemyList[enemyNo].health
                        battlestate = 0
                        loot(enemyList, enemyNo)
                
                else:
                    print("That's not an option.")
                    decision = int(input("1. Attack\n2. Inventory\n3. Run\n"))
                    x = attack - 1
            
            print("The ", enemyList[enemyNo].name, "attacks!")
            enemyMiss = random.randint(0, 5) + enemyList[enemyNo].accuracy
            characterDodge = random.randint(0, 5) + character.reflex
            if enemyMiss >= characterDodge:
                if enemyList[enemyNo].strength >= enemyList[enemyNo].intelligence:
                    damage = round(enemyList[enemyNo].strength / character.pdefense, 2)
                    character.tempHealth = character.tempHealth - damage
                    print("You have ", character.tempHealth, " health remaining.")
                    if character.tempHealth < 1:
                        print("Your wounds proved fatal...")
                        print("Game Over.")
                else:
                    damage = round(enemyList[enemyNo].intelligence / character.mdefense, 2)
                    character.tempHealth = character.tempHealth - damage
                    print("You have ", character.tempHealth, " health remaining.")
                    if character.tempHealth < 1:
                        print("Your wounds proved fatal...")
                        print("Game Over.")
            else:
                print("...but the ", enemyList[enemyNo].name, "'s attack missed!")

        elif decision == 2:
            battlestate == 0
            inventoryShow()
            decisionX = input("What would you like to use?")
            inventoryUse(decisionX, contents, lootX)
            battlestate == 1
            print("The ", enemyList[enemyNo].name, "attacks!")
            enemyMiss = random.randint(0, 5) + enemyList[enemyNo].accuracy
            characterDodge = random.randint(0, 5) + character.reflex
            if enemyMiss >= characterDodge:
                if enemyList[enemyNo].strength >= enemyList[enemyNo].intelligence:
                    damage = round(enemyList[enemyNo].strength / character.pdefense, 2)
                    character.tempHealth = character.tempHealth - damage
                    print("You have ", character.tempHealth, " health remaining.")
                    if character.tempHealth < 1:
                        print("Your wounds proved fatal...")
                        print("Game Over.")
                else:
                    damage = round(enemyList[enemyNo].intelligence / character.mdefense, 2)
                    character.tempHealth = character.tempHealth - damage
                    print("You have ", character.tempHealth, " health remaining.")
                    if character.tempHealth < 1:
                        print("Your wounds proved fatal...")
                        print("Game Over.")
            else:
                print("...but the ", enemyList[enemyNo].name, "'s attack missed!")

            
        elif decision == 3:
            run = random.randint(1, 5) + character.luck
            if run >= random.randint(1, 5) + enemyList[enemyNo].luck:
                print("You managed to get away.")
                battlestate == 0
            else:
                print("You failed to get away.")
                print("The ", enemyList[enemyNo].name, "attacks!")
                enemyMiss = random.randint(0, 5) + enemyList[enemyNo].accuracy
                characterDodge = random.randint(0, 5) + character.reflex
                if enemyMiss >= characterDodge:
                    if enemyList[enemyNo].strength >= enemyList[enemyNo].intelligence:
                        damage = round(enemyList[enemyNo].strength / character.pdefense, 2)
                        character.tempHealth = character.tempHealth - damage
                        print("You have ", character.tempHealth, " health remaining.")
                        if character.tempHealth < 1:
                            print("Your wounds proved fatal...")
                            print("Game Over.")
                    else:
                        damage = round(enemyList[enemyNo].intelligence / character.mdefense, 2)
                        character.tempHealth = character.tempHealth - damage
                        print("You have ", character.tempHealth, " health remaining.")
                        if character.tempHealth < 1:
                            print("Your wounds proved fatal...")
                            print("Game Over.")
                else:
                    print("...but the ", enemyList[enemyNo].name, "'s attack missed!")
            
        else:
            print("That's not an option.")
            decision = int(input("1. Attack\n2. Inventory\n3. Run\n"))

# Skill Checks

def skillCheckOne():
    check = random.randint(1, 3)
    if check == 1:
        print("Pass an easy strength skill check")
        if character.strength >= 6:
            print("You passed!")
            print("You are rewarded with an item!")
            file = open("loot.txt", "r")
            lootTableCommon = file.readline()
            lootTableCommon = lootTableCommon.split(",")
            lootTableCommon = lootTableCommon[:-1]
            length = len(lootTableCommon)-1
            lootX = str(lootTableCommon[random.randint(0, length)])
            print("You found a ", lootX)
            lootCheck(lootX)
        else:
            print("You failed!")
    if check == 2:
        print("Pass an easy dexterity skill check")
        if character.dexterity >= 6:
            print("You passed!")
            print("You are rewarded with an item!")
            file = open("loot.txt", "r")
            lootTableCommon = file.readline()
            lootTableCommon = lootTableCommon.split(",")
            lootTableCommon = lootTableCommon[:-1]
            length = len(lootTableCommon)-1
            lootX = str(lootTableCommon[random.randint(0, length)])
            print("You found a ", lootX)
            lootCheck(lootX)
        else:
            print("You failed!")
    if check == 3:
        print("Pass an easy intelligence skill check")
        if character.intelligence >= 6:
            print("You passed!")
            print("You are rewarded with an item!")
            file = open("loot.txt", "r")
            lootTableCommon = file.readline()
            lootTableCommon = lootTableCommon.split(",")
            lootTableCommon = lootTableCommon[:-1]
            length = len(lootTableCommon)-1
            lootX = str(lootTableCommon[random.randint(0, length)])
            print("You found a ", lootX)
            lootCheck(lootX)
        else:
            print("You failed!")

# Map Actions

def mapOneSearch():
    print("You search the area around you for anything of interest...")
    search = random.randint(1, 5)
    if search == 1:
        character.progress = character.progress + 1
        print("You didn't find anything interesting. Perhaps you should continue searching.")
    elif search ==2:
        character.progress = character.progress + 1
        print("You've attracted the attention of an enemy!+")
        battlestate()
    elif search ==3:
        character.progress = character.progress + 1
        print("You've attracted the attention of an enemy!+")
        battlestate()
    elif search ==4:
        character.progress = character.progress + 1
        skillCheckOne()
    else:
        character.progress = character.progress + 1
        print("Upon a long-deceased corpse you find a satchel with something in it...")
        file = open("loot.txt", "r")
        lootTableCommon = file.readline()
        lootTableCommon = lootTableCommon.split(",")
        lootTableCommon = lootTableCommon[:-1]
        length = len(lootTableCommon)-1
        lootX = str(lootTableCommon[random.randint(0, length)])
        print("Within the satchel, you discover a ", lootX)
        lootCheck(lootX)





# Maps

def mapOne():
    character.location = 1
    print("#"*80)
    print("##","."*74, "##")
    print("##......................", "R O A D - TO - P E R G A M U M", "......................##")
    print("##","."*74, "##")
    print("#"*80)
    print("\n After weeks of travel, the road to Pergamum cuts through a dying forest. The \nskeletal trees are gnarled and stripped of all foliage.")
    print("How would you like to proceed?")
    decision = int(input("1. Continue down the path.\n2. Search the area.\n3. Check inventory."))
    if decision > 3:
        print("That's not an option.")
    elif decision == 1:
        if character.progress >= 5:
            print("You progress to the next map.")
        else:
            mapOneSearch()

    elif decision == 2:
        mapOneSearch()
    elif decision == 3:
        inventoryShow()
        print("How would you like to proceed?")
        decision = int(input("1. Continue down the path.\n2. Search the area.\n3. Check inventory."))


#############################      G A M E          S T A R T      #####################################

inventoryWipe()
intro()
startGame()
mapOne()