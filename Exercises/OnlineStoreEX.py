"""
Ask the user to input the cost of their order. Ask what country they're in. Ask what province they're in.
Calculate by using total plus the correct tax for the region. Output to the user.
Variables should be: cost, country, province, totalCostAlberta, totalCostHarmonized, totalCostOther.
"""
#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    Ethan Matthews
Program Title:   Online Store
Description:     Create an online store that sells to all provinces and outside the country.
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    albertTax = 1.05
    harmonizedTax = 1.15
    otherTax = 1.11

    print("Welcome to the Online Store! \n")
    cost = float(input("Enter the cost of your perchase: "))
    country = input("Enter your country: ")

    if country.upper() == "CANADA":
        province = input("Enter your province: ")
        if province.upper() == "ALBERTA":
            totalCostAlberta = cost * albertTax
            print("Your total will be ${0:.2f}. \nThank you for using the online store!".format(totalCostAlberta))
        elif province.upper() == "NOVA SCOTIA":
            totalCostHarmonized = cost * harmonizedTax
            print("Your total will be ${0:.2f}. \nThank you for using the online store!".format(totalCostHarmonized))
        elif province.upper() == "NEW BRUNSWICK":
            totalCostHarmonized = cost * harmonizedTax
            print("Your total will be ${0:.2f}. \nThank you for using the online store!".format(totalCostHarmonized))
        elif province.upper() == "ONTARIO":
            totalCostHarmonized = cost * harmonizedTax
            print("Your total will be ${0:.2f}. \nThank you for using the online store!".format(totalCostHarmonized))
        else:
            totalCostOther = cost * otherTax
            print("Your total will be ${0:.2f}. \nThank you for using the online store!".format(totalCostOther))
    else:
        print("\nThere's no charge because you're outside of Canada! \nThank you for using the online store!")
        
    
    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()