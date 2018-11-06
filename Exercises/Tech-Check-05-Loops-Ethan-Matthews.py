#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Ethan Matthews  
Program Title:  Highest common devisor
Description:    Tech Check 05 Highest Common Divisor testing loops
"""

def userInputOne():
    # firstNumber = int(input("Enter your first number: "))
    firstNumber = "32"
    while firstNumber.isnumeric() == False:
        print("Enter a valid first Number.")
        continue
    return firstNumber

def userInputTwo():
    # secondNumber = int(input("Enter your second number: "))\
    secondNumber = "56"
    while secondNumber.isnumeric() == False:
        print("Enter a valid second Number:.")
        continue
    return secondNumber

def mathFunc(numb1, numb2):
    counter = 0
    while counter <= numb1 and counter <= numb2:
        if numb1 % counter == 0 and numb2 % counter == 0:
        counter = counter + 1
        continue

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    continues = True
    while continues == True:
        firstNumber = userInputOne()
        secondNumber = userInputTwo()
        Highestdivisor = mathFunc(firstNumber, secondNumber)


        usercontinue = input("Would you like to try again? (y/n): ").lower()
        if usercontinue == "y":
            continue
        elif usercontinue == "n":
            break
            print("Thankyou for using the HCD program.")





    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()