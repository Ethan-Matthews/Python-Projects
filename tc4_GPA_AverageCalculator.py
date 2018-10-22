############################################
# Tech Check 4 - Provided Starter File
############################################

#FUNCTION

def welcome():

    print("Grade Point Calculator\n")
    print("Valid letter grades that can be entered: A, B, C, D, F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0.\n")

def GPA(course):

    numericGrade = 0.0
    
    #Gather user inputs
    letterGrade = input("Please enter a letter grade for {0}: ".format(course)).upper()
    modifier = input("Please enter a modifier (+, - or nothing) : ")

    # Determine base numeric value of the grade
    if letterGrade == "A":
        numericGrade = 4.0
    elif letterGrade == "B":
        numericGrade = 3.0
    elif letterGrade == "C":
        numericGrade = 2.0
    elif letterGrade == "D":
        numericGrade = 1.0
    elif letterGrade == "F":
        numericGrade = 0.0
    else:
        #If an invalid entry is made
        print("You entered an invalid letter grade.")
    
    # Determine whether to apply a modifier
    if modifier == "+":
        if letterGrade != "A" and letterGrade != "F": # Plus is not valid on A or F
            numericGrade += 0.3
    elif modifier == "-":
        if letterGrade != "F":     # Minus is not valid on F
            numericGrade -= 0.3
    return numericGrade

    # Output final message and result, with formatting
    #print("The numeric value is: {0:.1f}".format(numericGrade))

def average(prog1700, netw1700, osys1200, webd1000, comm1700, dbas1007):
    courseAverage = (prog1700 + netw1700 + osys1200 + webd1000 + comm1700 + dbas1007) / 6
    return courseAverage

def individualOutput(prog1700, netw1700, osys1200, webd1000, comm1700, dbas1007):
    print("The numeric value for PROG1700 is: {0}".format(prog1700))
    print("The numeric value for NETW1700 is: {0}".format(netw1700))
    print("The numeric value for OSYS1200 is: {0}".format(osys1200))
    print("The numeric value for WEBD1000 is: {0}".format(webd1000))
    print("The numeric value for COMM1700 is: {0}".format(comm1700))
    print("The numeric value for DBAS1007 is: {0}".format(dbas1007)) 


def output(gpaOutput):
    print("Your grade point average for the semester is: {0}".format(gpaOutput))

def main():
    welcome()
    prog1700 = GPA("PROG1700")
    netw1700 = GPA("NETW1700")
    osys1200 = GPA("OSYS1200")
    webd1000 = GPA("WEBD1000")
    comm1700 = GPA("COMM1700")
    dbas1007 = GPA("DBAS1007")
    gpaOutput = average(prog1700, netw1700, osys1200, webd1000, comm1700, dbas1007)
    individualOutput(prog1700, netw1700, osys1200, webd1000, comm1700, dbas1007)
    output(gpaOutput)


#PROGRAM STARTS HERE
if __name__ == "__main__":
    main()