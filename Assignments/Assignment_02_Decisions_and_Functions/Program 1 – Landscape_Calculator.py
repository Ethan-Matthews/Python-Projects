#Don't forget to rename this file after copying the template
#for a new program! 
"""
Student Name:   Ethan Matthews
Program Title:  Landscape Calculator
Description:    Calculates cost of landscaping job.
"""

"""
1. Create separate function containers for user inputs.
2. Create calculation function (passing perameters through from inputs) to calculate square footage and total cost.
3. Create function to output values to user.
4. Create main function to define and call other functions in proper sequence.
"""

#User address input
def userAddressF():
    return int(input("Enter House Number: "))

#User property depth in feet.
def propertyDepthF():
    return float(input("\nEnter property depth (feet): "))

#User property width in feet.
def propertyWidthF():
    return float(input("\nEnter property width (feet): "))

#Grass type the user wants to use. 
def grassTypeF():
    return input("\nEnter type of grass (fescue, bentgrass, campus): ").lower()

#Number of trees the user wants planted. $100 each
def numberOfTreesF():
    return int(input("\nEnter the number of trees: "))

#Calculation for square footage and total cost. Base rate of $1000 applied. Anything over 5000 feet squared is an additional $500.
#fescue $0.05, bentgrass $0.02, campus $0.01.
def calculationF(depth, width, grass, trees):
    cost = 1000.00
    fescuePrice = 0.05
    bentPrice = 0.02
    campusPrice = 0.01
    treePrice = 100.00

    surfaceArea = depth * width
    if surfaceArea > 5000:
        cost = cost + 500.00

    if grass == "fescue":
        grassCost = surfaceArea * fescuePrice
    if grass == "bentgrass":
        grassCost = surfaceArea * bentPrice
    if grass == "campus":
        grassCost = surfaceArea * campusPrice

    treeCost = trees * treePrice

    totalCost = cost + grassCost + treeCost
    return totalCost

#Output to user with address and total cost of work.
def outputF(address, costOfWork):
    print("\nTotal cost for house {0} is: ${1:.2f}".format(address, costOfWork))

#Main Function. Defines and calls functions for use as perameters.
def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    address = userAddressF()
    propertyDepth = propertyDepthF()
    propertyWidth = propertyWidthF()
    grassType = grassTypeF()
    numberOfTrees = numberOfTreesF()
    costOfWork = calculationF(propertyDepth, propertyWidth, grassType, numberOfTrees)
    outputF(address, costOfWork)
    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()