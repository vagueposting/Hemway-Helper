import random
import time
# in order: HP, ATK, DEF, SPD, EVA, ACC, LUK, guard status, strengthen status
player = [250, 65, 25, 50, 25, 2, 2, 2, 2, False, False]
enemy = [200, 50, 25, 50, 25, 2, 2, 2, 2, False, False]
P = False
E = False
instructions = ["   Attack - 1", "  Guard - 2", "   Strengthen - 3"]
turns = 0
Pasturn = -1
rounds = 0
time.sleep(1)
splystats = str(input("See player stats? Y/N"))


if splystats == "Y" or splystats == "y":
    print("PLAYER STATS")
    print("HP:",player[0])
    print("ATK:",player[1])
    print("DEF:",player[2])
    print("SPD:",player[5])
    print("EVA:",player[6])
    print("ACC:",player[7])
    print("LUK:",player[8])
elif splystats == "N" or splystats == "n":
    print("     You chose not to display player stats.")

time.sleep(0.5)

senestats = str(input("See enemy stats? Y/N"))
if senestats == "Y" or senestats == "y":
    time.sleep(1)
    print("ENEMY STATS")
    print("HP:",enemy[0])
    print("ATK:",enemy[1])
    print("DEF:",enemy[2])
    print("SPD:",enemy[5])
    print("EVA:",enemy[6])
    print("ACC:",enemy[7])
    print("LUK:",enemy[8])
elif senestats == "N" or senestats == "n":
    print("     You chose not to display enemy stats.")

# DIE VARIABLE SUMMARY: 
# "hitdie" stands for the die roll value used in accuracy rolls
# "evadie" stands for the die roll value used in evasion rolls
# "damdie1" stands for the die roll value used in player attack rolls
# "damdie2" stands for the die roll value used in enemy attack rolls

compromp = str(input("Initiate combat? Y/N"))
if compromp  == "Y" or compromp == "y":
    while enemy[0] > 0:
        turns = turns + 1
        print("")
        print("")
        print("Turn",turns)
        if not(turns % 2 == 0):
            P = True
        elif (turns % 2 == 0):
            E = True

        if P == True:
            time.sleep(1)
            print(instructions[0])
            print(instructions[1])
            print(instructions[2])
            choice = int(input("Command?"))
            if choice == 1:
                for x in range(1):
                    hitdie = random.randint(1,20)
                print("     YOU ROLLED:",hitdie)
                Pacc = hitdie + player[7]
                print("     PLAYER ACCURACY CHECK:", Pacc)
                for x in range(1):
                    evadie = random.randint(1,20)
                print("     ENEMY ROLLED:",evadie)
                Eeva = evadie + enemy[6]
                print("     ENEMY EVASION CHECK:", Eeva)
                if Pacc > Eeva:
                    print("Player attacks!")
                    for x in range(1):
                        damdie1 = random.randint(1,20)
                    print("     YOU ROLLED:",damdie1)
                    if player[10] is True:
                        Patk = (player[1] + damdie1) + ((player[1] + damdie1) // 4)
                    else:
                        Patk = player[1] + damdie1 
                    if enemy[9] is True:
                        Edmg = (Patk - enemy[2]) - ((Patk - enemy[2]) // 4)
                    else:
                        Edmg  = Patk - enemy[2]
                    print("Enemy took",Edmg,"damage!")
                elif Pacc <= Eeva:
                    print("Enemy evaded!")
            elif choice == 2:
                print("You guarded!")
                print("You will take 25% less damage until the next round!")
                player[9] = True
            elif choice == 3:
                print("You strengthened!")
                print("You will deal 25% more damage on the next round!")
                player[10] = True
            P = False
        # enemy choice is randomized as of the moment because that's what's easier,
        # however i WILL construct a simple AI based on event flags
        # when the prototype is finished.
        # "enchoice" is short for "enemy choice"
        if E == True:
            time.sleep(1)
            print("It's the enemy's turn.")
            for x in range(1):
                enchoice = random.randint(1,9)
            if 1 <= enchoice <= 5:
                for x in range(1):
                    hitdie = random.randint(1,20)
                print("     ENEMY ROLLED:",hitdie)
                Eacc = hitdie + enemy[7]
                print("     ENEMY ACCURACY CHECK:", Eacc)
                for x in range(1):
                    evadie = random.randint(1,20)
                print("     YOU ROLLED:",evadie)
                Peva = evadie + player[6]
                print("     YOUR EVASION CHECK:", Peva)
                if Eacc > Peva:
                    print("Enemy attacks!")
                    for x in range(1):
                        damdie2 = random.randint(1,20)
                    print("     ENEMY ROLLED:",damdie2)
                    if enemy[10] is True:
                        Eatk = (enemy[1] + damdie2) + ((enemy[1] + damdie2) // 2)
                    else:
                        Eatk = enemy[1] + damdie2
                    if player[9] is True:
                        Pdmg = (Eatk - player[2]) - ((Eatk - player[2]) // 4)
                    else:
                        Pdmg  = Eatk - player[2]
                    print("You took",Pdmg,"damage!")
                elif Eacc < Peva:
                    print("You evaded!")
            elif 6 <= enchoice <= 7:
                print("Enemy guarded!")
                print("They will take 25% less damage until the next round!")
                enemy[9] = True
            elif 8 <= enchoice <= 9:
                print("Enemy strengthened!")
                print("They will deal 25% more damage on the next round!")
                enemy[10] = True
            E = False

    

    if enemy[0] <= 0:
        print("Enemy died!")
        print("You win!")

    if player[0] <= 0:
        print("YOU DIED")
