# Is there a plus and minus (-/+) symbol in python?
#


n = 100 #int(input("Enter a number: "))

counter = 0
while counter <= n:
    if counter * counter <= n:
        print("Square = {0}".format(counter * counter))
        print("*" * 20)
    if counter % 10 == 0:
        print("Evenly Divisible by 10?: {0}".format(counter))
        print("*" * 20)
    if 2 ** counter <= n:
        print("Powers of two: {0}".format(2 ** counter))
        print("*" * 20)
    counter += 1



