"""
Build a Python program to calculate whether a surcharge will be applied, based on the weight of an airline passenger's luggage.
When passengers check in at the airline counter, they are allowed a maximum luggage weight of 50 lbs.
If luggage exceeds the weight limit, a $25 surcharge is applied.
Write a program to allow passengers to enter the total weight of their luggage and calculate whether to apply a surcharge.
Your program should display a message indicating whether a surcharge is required, or not.
"""
"""
Set up hard variables: surcharge is $25.00. WeightLimit is 50lbs.
Will print welcome banner, then prompt user to input their luggage weight. Variables used will be weightLbs.
Then create a conditional statments (greater/less than). Is the luggage more than 50lbs?
    If more than weightLimit, then surchage ($25) will be applied.
    If less than weightLimit, then no surachage will be applied.
Will output conclusions to user with correctly formatted numbers.
Will then print goodbye/thankyou banner.
"""


#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    Ethan Matthews
Program Title:   Luggage Weights
Description:     Evaluate whether or not a surcharge will be applied to the user using IF statment.
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    surcharge = 25.00       #surcharge in dollars.
    weightLimit = 50        #weight limit 50lbs.

    print("Welcome to the Surcharge Application!\n")
    weightLbs = float(input("Please enter the weight of your luggage in pounds: "))     #User input luggage weight.

    if weightLbs > weightLimit:     #conditional statment - greater than.
        print("\nYou will be charged ${0:.2f}. Your luggage is over the {1}lbs. weight limit.".format(surcharge, weightLimit))      #print if greater than, surcharge and weight limit.

    if weightLbs <= weightLimit:        #conditional statment - less than or equal too.
        print("\nYou will not be charged an extra ${0:.2f}. Your luggage is not over the {1}lbs. weight limit.".format(surcharge, weightLimit))     #print if les than or equal too.
    
    print("\nThankyou, have a nice trip!")      #print goodbye/thankyou banner.

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()