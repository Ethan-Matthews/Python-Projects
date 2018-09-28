"""
The first few lines of code will be my user input values. Variables used will be: princialAmount, ratePercent,
numberOfYears. The there will ccalculations for the interest rate and the weekly payment. Variables used will be:
interstRate, weeklyPayment. The program will then out put the weelkyPayment to the user in a string. Will be rounded
to two decimal places. 
"""

#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Ethan Matthews
Program Title:  Weekly Loan Calculator
Description:    This program will calculate the intrest on a loan over time.
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    print("Weely Loan Calculator\n")
    principalAmount = float(input("Enter the amount of the loan (dollars): "))  #user enters principal amount.
    ratePercent = float(input("Enter the interst rate (percent): "))            #user enters interest rate in percent.
    numberOfYears = float(input("Enter the lenght of time (years): "))          #user enters the length of loan in years.

    interestRate = ratePercent / 5200                                                                       #Line preps interest rate for calculation.
    weeklyPayment = (interestRate / (1 - (1 + interestRate) ** (-52 * numberOfYears)) * principalAmount)    #This line calculates the cost of the weekly payment.

    print("\nYour weekly payment will be: ${0:.2f}".format(weeklyPayment))    #This is my output. Displays the weekly repayment amount to the user.

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()