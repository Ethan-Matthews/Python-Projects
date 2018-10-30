#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    Ethan Matthews
Program Title:   Exercise 08 Program 02. 
Description:     Write a program that reads a word and prints each character
                 of the word on a separate line.
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!





    userString = input("Enter a word: ")

    letterList = list(userString)

    counter = 0

    for counter in range(len(letterList)):
        print(letterList[counter])
        
    print("Your string has been sliced!")

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()