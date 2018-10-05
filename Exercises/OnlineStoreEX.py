"""
Ask the user to input the cost of their order. Ask what country they're in. Ask what province they're in.
Calculate by using total plus the correct tax for the region. Output to the user.
Variables should be: albertaTax, harmonizedTax, otherTax, cost, country, province, totalCostAlberta, totalCostHarmonized, totalCostOther.
"""
#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:    Ethan Matthews.
Program Title:   Online Store.
Description:     Create an online store that sells to all provinces and outside the country.
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    albertaTax = 1.05       #Alberta sales tax.
    harmonizedTax = 1.15    #Ontario, New Brunswick and Nova Scotia sales tax.
    otherTax = 1.11         #Tax for all other provinces.

    print("Welcome to the Online Store! \n")                    #Welcome Banner.
    cost = float(input("Enter the cost of your perchase: "))    #Cost of perchase.
    country = input("Enter your country: ")                     #Country name.

    if country.upper() == "CANADA":                             #Country conditional statement.
        province = input("Enter your province: ")               #Name of province.
        if province.upper() == "ALBERTA":                                                                               #Alberta conditional statement.
            totalCostAlberta = cost * albertaTax                                                                        #Alberta cost calculation.
            print("Your total will be ${0:.2f}. \nThank you for using the online store!".format(totalCostAlberta))      #Output with Alberta sales tax.
        elif province.upper() == "NOVA SCOTIA":                                                                         #Nova Scotia conditional statement.
            totalCostHarmonized = cost * harmonizedTax                                                                  #Nova Scotia cost calculation.
            print("Your total will be ${0:.2f}. \nThank you for using the online store!".format(totalCostHarmonized))   #Output with harmonized tax.
        elif province.upper() == "NEW BRUNSWICK":                                                                       #New Brunswick conditional statement.
            totalCostHarmonized = cost * harmonizedTax                                                                  #New Brunswick cost calculation.
            print("Your total will be ${0:.2f}. \nThank you for using the online store!".format(totalCostHarmonized))   #Output with harmonized tax.
        elif province.upper() == "ONTARIO":                                                                             #Ontario conditional statement.
            totalCostHarmonized = cost * harmonizedTax                                                                  #Ontario cost calculation.
            print("Your total will be ${0:.2f}. \nThank you for using the online store!".format(totalCostHarmonized))   #Output with harmonized tax.
        else:                                                                                                           #Province else statement.
            totalCostOther = cost * otherTax                                                                            #Other province cost calculation.
            print("Your total will be ${0:.2f}. \nThank you for using the online store!".format(totalCostOther))        #Output with other sales tax.
    else:                                                                                                               #Country else statemnet.
        print("\nThere's no charge because you're outside of Canada! \nThank you for using the online store!")          #Output if country is else. No tax applied.
        
    
    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()