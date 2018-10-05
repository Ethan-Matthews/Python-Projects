#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    Ethan Matthews
Program Title:   Hogwarts Sorting Hat
Description:     Does it need one? The title says it all!
"""


def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    import random

    randomNumber = random.randint(1, 4) 
    houseName = ""

    lastName = input("Enter last Name: ")

    if lastName.lower() == "potter":
        houseName = "Gryffendor"
    elif lastName.lower() == "malfoy":
        houseName = "Slytherin"
    else:
        if randomNumber == 1:
            houseName = "Gryffendor"
        elif randomNumber == 2:
            houseName = "Hufflepuff"
        elif randomNumber == 3:
            houseName = "Ravenclaw"
        elif randomNumber == 4:
            houseName = "Slytherin"

    print ("You've been assigned to {0}!".format(houseName))

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()