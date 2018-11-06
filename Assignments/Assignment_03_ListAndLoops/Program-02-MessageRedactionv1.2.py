#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    Ethan Matthews
Program Title:   Message Redaction
Description:     Design and write a program that removes all desired letters from any user-entered sentence or phrase.
"""

""" 
1. Create while loop (Switch) that will exit the program when user enters 'quit'.
2. Prompt user for phrase.
3. Promt user for a list of letters.
4. Use FOR loop to cycle through letters of phrase. Replace each letter specified by user in list of letters with _.
5. Output count of letters replaced and phrase without user list letters.
"""

#LetterRedact function. Passes both list in as perameters. Using FOR loop checks each letter in user phrase against letter list.  If letters are found
# to be same, replaces that letter with an underscore. 
# **** Special thanks @Baden for discovery and explanation of __contains__. ****
#Contains checks values in letterList against userPhrase counter in current iteration of loop.
#Count function to calculate the number of underscores in redacted phrase.

def letterRedact(P_userPhrase, P_letterList):
    letterOutput = ""
    userPhrase = P_userPhrase
    letterList = P_letterList
    for counter in range(len(userPhrase)):
        if letterList.__contains__(userPhrase[counter]):
            letterOutput = letterOutput + "_"
        else:
            letterOutput = letterOutput + userPhrase[counter]
    redactedLetters = letterOutput.count("_")
    return letterOutput, redactedLetters

#main function call.
def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    #Quit switch for whole program.
    quitSwitch = False

    #While loop for quiting the program when user enters 'quit'. Will also prompt user for 'phrase' input.
    while quitSwitch == False:
        userPhrase = input("Type a phrase (or quit to exit program): ").lower()
        if userPhrase == "quit":
            quitSwitch = True
            break

        #Input of letters in a string format.
        letterList = input("\nType a comma-separated list of letters to redact: ")

        #Call letterRedact function. Compare list values and replaces letters with underscores. Also provides count of underscores in redacted output.
        letterOutput, redactedLetters = letterRedact(userPhrase, letterList)

        #Outputs number of redacted letters and redacted phrase.
        print("Number of redacted letters: {0}".format(redactedLetters))
        print("Redacted Phrase: {0}\n".format(letterOutput))        


    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()