#create an empty list
myList = []

myList.append(["P", "Q", "R", "S"])
myList.append(["A", "B", "C", "D"])
myList.append(["K", "L", "M", "N"])


#print in raw format
# print(myList)
# print(myList[2][2])

# myList[1][2] = "z"

for row in myList:
    for column in row:
        print(column, end=" ")
    print() #print line break \n.  \n is at the end of every print statement.

# for rowIndex in range(len(myList)):
#     for colIndex in range(len(myList[rowIndex])):
#         print(myList[rowIndex][colIndex])

# print("Geoff", end="")
# print("Colby", end="")
# print("Whatever")


