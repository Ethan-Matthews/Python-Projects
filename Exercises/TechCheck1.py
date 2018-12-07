def main():
    billAmount = input("Input your bill amount: $")
    tax = int(billAmount) * 0.15
    tip = int(billAmount) * 0.20
    totalAmount = (int(billAmount) + tip + tax)
    print("Your tax amount is: $" + str(tax))
    print("Your tip amount is: $" + str(tip))
    print("Your bill total with taxes and tips is: $" + str(totalAmount)) 

main()