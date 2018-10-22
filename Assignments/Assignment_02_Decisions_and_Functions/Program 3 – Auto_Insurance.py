#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Ethan Matthews
Program Title:  Auto Insurance
Description:    Program to calculate monthly payment of auto insurance.
"""

"""
1. Create individual functions for each user input, retrun as a variable in main function.
2. Create individual functions for calculations based on gender.
3. Gender calculations will hold age brackets aswell.
4. Create output function inform user of monthly payment.
5. Create male or female logical statement in main function. 
"""

def userGender():
    return input("Are you 'male' of 'female': ".lower())

def userAge():
    return int(input("\nEnter your age: "))

def vehicleCost():
    return float(input("\nEnter the purchase price of the vehicle: "))

def femaleInsurance(age, vehiclePrice):
    if age >= 40 and age < 70:
        vehiclePayment = vehiclePrice * 0.10 / 12
    elif age >= 25 and age < 40:
        vehiclePayment = vehiclePrice * 0.15 / 12
    elif age >= 15 and age < 25:
        vehiclePayment = vehiclePrice * 0.20 / 12
    return vehiclePayment

def maleInsurance(age, vehiclePrice):
    if age >= 40 and age < 70:
        vehiclePayment = vehiclePrice * 0.10 / 12
    elif age >= 25 and age < 40:
        vehiclePayment = vehiclePrice * 0.17 / 12
    elif age >= 15 and age < 25:
        vehiclePayment = vehiclePrice * 0.25 / 12
    return vehiclePayment

def output(vehiclePayment):
    print("\nYour monthly insurance will be ${0:.2f}".format(vehiclePayment))

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    gender = userGender()
    age = userAge()
    vehiclePrice = vehicleCost()
    if gender == "male":
        vehiclePayment = maleInsurance(age, vehiclePrice)
    if gender == "female":
        vehiclePayment = femaleInsurance(age, vehiclePrice)
    output(vehiclePayment)

    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()