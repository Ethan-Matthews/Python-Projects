#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Ethan Matthews
Program Title:  Hipsteres Vinyl Records
Description:    This program will output the cost of a delivery.
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    """
    These next two lines are my hard coded values. First delivery rate, second sales tax.
    """
    deliveryRate = 15.00    #This is the current delivery rate in dollars.
    tax = 1.14              #This is the starndard sales tax of 14%.
    
    """
    These three next lines of code are the user input values. The first will be customer name,
    second will be the distance of delivery in Kilometers.
    The third will be the original cost of records perchased in dollars.
    """

    customerName = input("Customer Name: ")
    distanceKM = float(input("Distance of Delivery: "))
    recordCost = float(input("Cost of Records Perchased: "))

    deliveryCost = distanceKM * deliveryRate #Delivery cost calculation disatance in KM multiplied by the delivery rate.
    perchaseCost = recordCost * tax          #Perchase calculations. Origanial record cost plus tax of 14% in dollars.
    totalCost = perchaseCost + deliveryCost  #The total cost calculation. The perchase cost(already taxed) plus delivery cost.

    """
    The next five lines are my final output. The first line is a banner displayed when the order has been calculated.
    The second line displays the customer name. Third line displays ONLY the delivery cost. Fourth line displays ONLY the perchase cost (already taxed at 14%). The fifth and final line displays the total cost of the entire order.
    All values will be rounded down to the second decimal place.
    """

    print("Hippsters Vinyl Records - Customer Order Details")   #Display Banner.
    print("Perchase Summary for {0}.".format(customerName))     #Customer Name.
    print("Delivery Cost: ${0:.2f}".format(deliveryCost))       #Delivery Cost.
    print("Purchase Cost: ${0:.2f}".format(perchaseCost))       #Perchase Cost with 14% sales tax included.
    print("Total Cost: ${0:.2f}".format(totalCost))             #Total cost of the entire order.


    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()