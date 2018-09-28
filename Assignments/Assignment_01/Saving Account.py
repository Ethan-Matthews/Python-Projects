"""THIS IS MY SAVINGS ACOUNT EXERCISE. Calculate the balance at the end of three years when $100 is deposited
at the beginning of each year in a savings account at 5 % interest compounded annually"""




def main():
    print("$100 deposited.")
    print("Intrest per year is 5%.")
    print("Time Elapsed since deposite: Three years.")
    Deposite = 100
    Intrest = 0.05
    Time = 3
    YearlyIntrest = (Deposite * Intrest)
    TotalIntrest = (YearlyIntrest * Time) + Deposite
    print("Your total to date is: $" + str(TotalIntrest))
    """Work in progress. Need compound calculations for eah year. also need to add $100 each year."""
main()