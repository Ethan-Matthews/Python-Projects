#Paint Shop Calculator
#Program to calculate the number of gallons of paint required to paint a room, if provided the room dimensions

#Import the math class, for using ceiling rounding
import math

#Intro messages
def welcome():
    print("Welcome to the Paint Shop!")
    print("This program will help you calculate how many cans of paint you need to buy, based on the dimensions of your room.")

#Get Dimensions of the room
def userInput():
    length = float(input("\nEnter the length of the room, in feet: "))
    width = float(input("Enter the width of the room, in feet: "))
    height = float(input("Enter the height of the room, in feet: "))
    return length, width, height

#Calculate the area of the walls
#Divide the area by 150 square feet and
#round number of gallons up to the nearest whole number
def totalAreaF():
    length, width, height = userInput()
    totalArea = (length * height * 2) + (width * height * 2)
    #Declare variable for # of sq. ft. covered by one gallon of paint
    square_feet_per_gallon = 150.0
    gallons_of_paint = math.ceil(totalArea / square_feet_per_gallon)
    return totalArea, gallons_of_paint

#OUTPUT - Display number of gallons needed
def output():
    totalArea, gallons_of_paint = totalAreaF()
    print("\nThe total wall area of your room is {0} square feet.".format(totalArea))
    print("You will need {0} gallon(s) of paint. \n\nHappy Painting!".format(gallons_of_paint))

def main():
    welcome()
    output()
main()