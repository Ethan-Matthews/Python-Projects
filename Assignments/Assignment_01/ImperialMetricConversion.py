"""
The first few lines of code are going to be my user input values and a banner. The input variables will be:
impTons, stones, pounds, ounces. Following that, there will two equations. One to convert all user given imperial
numbers to ounces. The second to convert all ounces into metric kilos. Variables used will be: totalOunces, totalKilos.
Then the totalKilos will be split into appropriate metric units via subtraction. Variables used will be: MetricTons,
kilos, grams. The program will then output a banner followed by a string displaying the converted weight values.
"""

#Don't forget to rename this file after copying the template
#for a new program! 
"""
Student Name:    Ethan Matthews
Program Title:   Imperial to Metric Conversion Program
Description:     This program will convert user given imperial units to metric units.
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    print("Imperial to Metric Conversion.\n")                               #A banner message.
    impTons = float(input("Enter the number of imperial tons: "))           #User input imperial tons.
    stones = float(input("Enter the number of stones: "))                   #User input stones.
    pounds = float(input("Enter the number of pounds: "))                   #User input pounds.
    ounces = float(input("Enter the number of ounces: "))                   #User input ounces.

    totalOunces = 35840 * impTons + 224 * stones + 16 * pounds + ounces     #Total number of ounces calculation.
    totalKilos = totalOunces / 35.274                                       #Total number of kilos from total number of ounces.

    metricTons = int(totalKilos / 1000)                                     #MetricTons calculation.
    kilos = int(totalKilos - (metricTons * 1000))                           #Kilos left over after metric tons have been subtracted.
    grams = (totalKilos - (int(totalKilos))) * 1000                         #Grams left over after rounded kilos have been subtracted. muliplied by 1000 to move decimal.

    print("\nThe metric weight is {0} metric tons, {1} kilos, and {2:.1f} grams.".format(metricTons, kilos, grams))     #Output to user.


    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()