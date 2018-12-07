#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    
Program Title:  
Description:    
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    weeklySalary = float(input("Please enter the amount of your weekly salary?: "))
    depenndants = float(input("How many dependants do you have?: "))

    provTax = weeklySalary * 0.06
    fedTax = weeklySalary * 0.25
    depndpercent = depenndants * 0.02
    refund = depndpercent * weeklySalary
    totalWithHeld = provTax + fedTax
    totalTakehome = weeklySalary - totalWithHeld + refund
    



    print("the provicial tax is: ${0:.2f}.".format(provTax))
    print("The federal tax is: ${0:.2f}.".format(fedTax))
    print("Number of dependants claimed: {0}.".format(depndpercent))
    print("Dependant refund is: ${0:.2f}.".format(depndpercent))
    print("The total amount withheld is: ${0:.2f}.".format(totalWithHeld))
    print("Total income is: ${0:.2f}.".format(totalTakehome))


    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()