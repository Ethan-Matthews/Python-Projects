animalList = []
rangeofAnimals = 3

for counter in range(rangeofAnimals):
    animalList.append(input("Enter new animal types " + str(counter + 1) + ": "))

howBigislist = len(animalList)

for counter in range(howBigislist):
    print(animalList[counter])