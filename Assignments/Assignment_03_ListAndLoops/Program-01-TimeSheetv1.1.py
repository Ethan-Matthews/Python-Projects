#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    Ethan Matthews
Program Title:   Time Sheet
Description:     Design and write a program that accepts the number of hours worked
                 on each of five work days from the user, then displays different
                 information calculated about those entries as output.
"""

"""
1. Prompt user to input hours worked 5 times using a FOR loop.
2. Check with for loop for highest value in list. Output string and with most days worked.
3. Calculate total hours and average hours using a function.
4. Output total hours and average hours.
5. Check list for values less than 7 using FOR loop.
6. Output days worked with hours less than 7.
"""

#The total and average hours calculation inside recallable function.  Passes list through as perameter, retruns two values average and total hours.
def average(hourslist):
    weeklyHours = hourslist
    totalHours = weeklyHours[0] + weeklyHours[1] + weeklyHours[2] + weeklyHours[3] + weeklyHours[4]
    averageHours = totalHours / 5
    return averageHours, totalHours

#Main function call.
def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    #The list that will contian the user input hours.
    weeklyHours = []

    #The user input in FOR loop. Appends to list, and increments day number output by 1.
    for counter in range(1, 6):
        weeklyHours.append(int(input("Enter the hours worked on day #{0}: ".format(counter))))
        
    print("-" * 100)

    #Checks for highest value in list. Then outputs most hours worked and on what day.
    for counter2 in range(len(weeklyHours)):
        if weeklyHours[counter2] == max(weeklyHours):
            print("You worked the most on day #" + str(counter2 + 1) + " when you worked " +  str(weeklyHours[counter2]) + " hours")

    print("-" * 100)

    #Call function for average and total hours.
    averageHours, totalHours = average(weeklyHours)

    #Output total hours worked and average hours worked.
    print("The total number of hours worked was: {0}.\nThe average number of hours worked each day was: {1}.".format(totalHours, averageHours))

    print("-" * 100)
    
    print("Days you slacked off (i.e worked less than 7 hours): ")

    print("-" * 100)

    #Outputs all days worked with less than seven hours.
    for counter3 in range(len(weeklyHours)):
        if weeklyHours[counter3] < 7:
            print("Day #{0}: {1} hours".format(counter3 + 1, weeklyHours[counter3])) 

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()