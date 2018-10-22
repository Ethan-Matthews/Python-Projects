#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Ethan Matthews
Program Title:  Erewhon Mobile Data Plans 
Description:    Calculates the cost of data the user has used based on amount.
"""

"""
1.Create user input function.
2.Create cost calculation for data usage using if's and elifs.
3.Create ouput function that displays total cost of data usage.
"""

#user input function, data usage in MB.
def userInput():
    return int(input("Enter data usage (Mb): "))

#cost calculation function. calculates cost in $ for data used in MB.
def dataCostCalculation(dataAmount):
    cost = 0.00
    if dataAmount > 1000:
        cost = cost + 118.00
    elif dataAmount > 500 and dataAmount <= 1000:
        cost = cost + (0.110 * dataAmount)
    elif dataAmount > 200 and dataAmount <= 500:
        cost = cost + (0.105 * dataAmount)
    elif dataAmount < 200:
        cost = cost + 20.00
    return cost

#Output cost to user in $ via .format
def output(totalCost):
    print("\nTotal Charge is ${0:.2f}".format(totalCost))

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    dataUsage = userInput()
    totalCost = dataCostCalculation(dataUsage)
    output(totalCost)

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()