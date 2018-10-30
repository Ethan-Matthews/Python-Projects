#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    Ethan Matthews
Program Title:   Exercise 08 Program 03.
Description:     Write programs that read a sequence of integer inputs and print
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    myList = []

    # myList.append(int(input("Please enter number: "))) Do this instead of individual variables.

    firstNumber = int(input("Please enter frist number: "))
    myList.append(firstNumber)
    secondNumber = int(input("Please enter second number: "))
    myList.append(secondNumber)
    thirdNumber = int(input("Please enter third number: "))
    myList.append(thirdNumber)
    fourthNumber = int(input("Please enter fourth number: "))
    myList.append(fourthNumber)

    myList.sort()

    valueOfList = myList[0] + myList[1] + myList[2] + myList[3]

    print("The lowest value is {0}".format(myList[0]))
    print("The highest value is {0}".format(myList[3]))
    print("The list total is: {0}".format(valueOfList))

    for counter in range(3):
        if myList[counter] == myList[counter + 1]:
            print("You have a duplicate number {0}".format(myList[counter]))

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()