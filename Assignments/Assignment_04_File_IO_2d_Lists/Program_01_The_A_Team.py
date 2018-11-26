#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Ethan Matthews
Program Title:  The A-Team
Description:    Design and write a program that reads the text from a provided text file into a list,
                displays the text on-screen, makes some alterations to the text and outputs the changed
                text to the screen, then saves the altered text as a new file. 
"""

"""
1. Read file entire contents of ateam_Original.txt and output using .read() loop.
2. Read text lines into list to create range of random numbers using readline() loop.
3. Import random function to generate random number, use len() of list to complete range for random function.
4. Read altered text with IF, ELIF and/or ELSE clauses for random line deletion and upper-lowercase thresholds using readline() loop.
"""

# Import random function
import random

# Terminal lines function
def terminalLines():
    print("-"*40)

# Main function
def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    # Pre-declared variables for lower random range number, lettercase threshold, and the random counter for the last loop.
    lowerRandomRange = 1
    caseThreshold = 20
    randomCounter = 1

    # File needed with accessmode
    fileName = "ateam_Original.txt"
    accessMode = "r"

    # Open file
    myFile = open(fileName, accessMode)

    # Header for program output. 
    terminalLines()
    print("Original Text")
    terminalLines()

    # Read unaltered file contents into terminal 
    print(myFile.read(), end="")
    print("\n")

    # Close file
    myFile.close()

    # Accessmode
    accessMode = "r"

    # Open file
    myFile = open(fileName, accessMode)

    # Header for altered program output.
    terminalLines()
    print("Altered Text")
    terminalLines()

    # Loop to readlines into list for range of random function.
    randomLengthList = []
    singleLine = myFile.readline()
    while singleLine:
        randomLengthList.append(singleLine)
        singleLine = myFile.readline()

    # Close file
    myFile.close()

    # Accessmode
    accessMode = "r"

    # Open file
    myFile = open(fileName, accessMode)

    # Variable for singlelines from file
    singleLine = myFile.readline()

    # Random fuction for random line deletion
    randomLine = random.randint(lowerRandomRange, len(randomLengthList))

    # Loop for outputing altered text into terminal
    # First IF clause is for random line deletion.
    # Second IF inside ELSE clause is for lines that are more than 20 characters long.
    # ELIF clause is is for lines that are less than 20 characters long.
    while singleLine:
        if randomLine == randomCounter:
            print("")
            singleLine = myFile.readline()
            randomCounter += 1
        else:
            if len(singleLine) > caseThreshold:
                print("{0}: {1}".format(randomCounter, singleLine).lower(), end="")
                singleLine = myFile.readline()
                randomCounter += 1
            elif len(singleLine) <= caseThreshold:
                print("{0}: {1}".format(randomCounter, singleLine).upper(), end="")
                singleLine = myFile.readline()
                randomCounter += 1

    myFile.close()

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()