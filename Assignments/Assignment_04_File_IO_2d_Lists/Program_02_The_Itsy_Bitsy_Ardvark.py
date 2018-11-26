#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Ethan Matthews
Program Title:  The Itsy Bitsy Ardvark
Description:    Design and develop a program that presents the user with a “Mad Libs”
                type game, where a random choice of words are read from a file,
                then interjected into a story read from another file.
"""
# Import CSV Library
import csv

# inputLoops function.  Loops through the_choices_file, presents input choices and gather user input for all choices.
def inputLoops(choicesFileName, accessModeChoices):
    # letterString for adding letter options to output loops.
    letterString = "abcde"
    # Pre-initialized list made to contain user choices from file.
    userChoiceList = []
    # Pre-initialized counter starting at 1 not 0.
    counter = 1

    # Read single lines from file using csv reader. Uses nested for loop to print all choices from each line before use inputs string.
    with open(choicesFileName, accessModeChoices) as csvReader:
        choices = csv.reader(csvReader)
        for row in choices:
            print("\nPlease Enter {0}: ".format(row[0]))
            for letter in letterString:
                print("{0}) {1}".format(letter[0], row[counter]))
                counter += 1
            counter = 1
            # Verifies user input. If input is incorrect, will re-prompt user with same message. 
            inputCheck = False
            while inputCheck == False:
                userChoice = input("Enter a choice (a-e): ").lower()
                for letter in letterString:
                    if userChoice == letter:
                        inputCheck = True
                        break
            # IF and ELIF statements assign values to user input letters by indices.
            if userChoice == "a":
                userChoice = row[counter]
            elif userChoice == "b":
                userChoice = row[counter + 1]
            elif userChoice == "c":
                userChoice = row[counter + 2]
            elif userChoice == "d":
                userChoice = row[counter + 3]
            elif userChoice == "e":
                userChoice = row[counter + 4]
            # Appends user choice to userChoiceList at the end of each row loop. All user choices are stored in this list.
            userChoiceList.append(userChoice)
    # Function returns a list containing all user choices in chronological order.
    return userChoiceList

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    # A switch for quitting the program.
    quitSwitch = False

    # Whole program runs in while loop in order to exit when prompted.
    while quitSwitch == False:
        # names of files required.
        choicesFileName = "the_choices_file.csv"
        storyFileName = "the_story_file.txt"
        # Access modes for files required.
        accessModeChoices = "r"
        accessModeStory = "r"
        # Opens story file.
        storyFile = open(storyFileName, accessModeStory)
        # Reads story file into variable as one string.
        storyPhrase = storyFile.read() 

        print("\nThe Itsy Bitsy Aardvark")
        # Function for gathering user input.
        userChoiceList = inputLoops(choicesFileName, accessModeChoices)
        # Replaces placeholders in story string with values from userChoiceList
        for counter in range(len(userChoiceList)):
            storyPhrase =  storyPhrase.replace("_{0}_".format(counter + 1), userChoiceList[counter])
        
        print("Your Completed Story\n")
        print(storyPhrase)
        # Switch for continuing program.
        continueSwitch = True
        # while loop repeats until user input is correct. Asks user if they wish to restart the program or quit.
        while continueSwitch == True:
            quitProgram = input("\nDo you want to restart the program (y/n): ").lower()
            if quitProgram == "y":
                storyFile.close()
                break
            elif quitProgram == "n":
                print("Thanks for Playing!\n")
                storyFile.close()
                continueSwitch = False
                quitSwitch = True
                break
            else:
                print("WRONG INPUT FOO!!!\nPlease try again.")

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()