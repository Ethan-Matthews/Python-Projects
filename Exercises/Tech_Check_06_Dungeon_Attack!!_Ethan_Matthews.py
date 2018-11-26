#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Ethan Matthews
Program Title:  Dungeon Attack
Description:    Tech Check 06
"""

import csv

def terminalLines():
    print("=" * 100)

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    quitSwitch = False

    while quitSwitch == False:

        print("Welcome to the dungeon Attack application where none shall survice! Simply try to live as long as you can.")
        userContinueSwitch = input("hit any key to continue ('Q' or 'q' to quit): ").upper()
        if userContinueSwitch == "Q":
            quitSwitch = True
            print("That's it. Retreat in fear and warn your friends!")
            break

        userHitPointsCheck = False

        while userHitPointsCheck == False:
            userHitPoints = input("Please enter your initial hit points (1-200): ")
            if userHitPoints.isnumeric() == True:
                if int(userHitPoints) > 0 and int(userHitPoints) <= 200:
                    userHitPointsCheck = True
                    break
                else:
                    print("You don't listen very well do you? Think you are going to survive this dungeon?")
                    continue
            else:
                print("You don't listen very well do you? Think you are going to survive this dungeon?")
                continue

        terminalLines()

        fileName = "Tech_Check_06_CSV.txt"
        accessMode = "r"

        with open(fileName, accessMode) as csvFile:
            creatureList = csv.reader(csvFile)
            for row in creatureList:
                hitPointsLeft = int(userHitPoints) - int(row[2])
                print("You were attacked by a {0} with a {1} attack for {2} damage. Current hit points: {3}".format(row[0], row[1], row[2], hitPointsLeft))

        print("That was sad. And Brief. at least the elf feels better about himself!!!\n")    




       





    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()