#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    Ethan Matthews
Program Title:   Girl guide cookie sell off
Description:     The organizers of the annual Girl Guide cookie sale event want
                 to raise the stakes on the number of cookies sold and are offering cool prizes to those
                 guides who go above and beyond in their sales efforts.
                 The organizers want a program to print the guide list and their prizes.
"""

""" 
1. Prompt user for number of guides in competition.
2. Append lists with user input data. Guide name and boxes of cookies sold.
3. Add boxes of cookies sold by each guide with FOR loop. 
4. Calculate average number of boxes sold.
5. Output what guide got what prize for amount of cookies sold.
"""

#Averages function. Passes list and variable in as perameters. Retruns the average of boxes sold.
def averages(P_guideBoxes, P_numberOfGuides):
    total = 0
    guideBoxes = P_guideBoxes
    for boxes in range(len(guideBoxes)):
        total = total + guideBoxes[boxes]
    totalAverage = total / P_numberOfGuides
    return totalAverage

#Main function call.
def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    #User input for number of guids.
    numberOfGuides = int(input("Enter the number of guides selling cookies: "))

    #Initialize lists.
    guideNames = []
    guideBoxes = []
    prizeList = []

    #User input for names and number of boxes sold. Values appended to lists.
    for counter in range(int(numberOfGuides)):
        guideNames.append(input("\nEnter the name of guide {0}: ".format(counter + 1)))
        guideBoxes.append(int(input("Enter the number of boxes sold by {0}: ".format(guideNames[counter]))))
        prizeList.append("-")

    #Average function call.  Retruns average number of cookie boxes sold.
    totalAverage = averages(guideBoxes, numberOfGuides)

    #Output average number of boxes sold.
    print("\nThe average of boxes sold by each guide was {0:.1f}\n".format(totalAverage))

    #FOR loop that checks values against prize guidelines. Must check for the greatest value first. Primes values (string) in prize list for output.
    for prizes in range(int(numberOfGuides)):
        if guideBoxes[prizes] == max(guideBoxes):
            prizeList[prizes] = "Trip to Girl Guide Jamboree in Aruba!"
        elif guideBoxes[prizes] > totalAverage:
            prizeList[prizes] = "Super Seller Badge"
        elif guideBoxes[prizes] >= 1:
            prizeList[prizes] = "Left over cookies"

    print("Guide                 Prizes Won:")
    print("-" * 100)

    #FOR loop that outputs guide names and prizes won.
    #****Thanks @Garrison for 's' string operator.**** - Makes things nicely spaced.
    for guide in range(int(numberOfGuides)):
        print("{0:20s}-{1}".format(guideNames[guide], prizeList[guide]))



    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()