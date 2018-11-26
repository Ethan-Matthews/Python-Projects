import csv


def main():

    quitSwitch = False

    while quitSwitch == False:

        fileName = "CVSguestList.txt"
        accessMode = "a"
        #Open a file object, if one doesn't exist than it creats one.
        myFile = open(fileName, accessMode)

        name = input("Please enter name (or 'end' to exit): ").lower()
        if name == "end":
            print("Goodbye")
            quitSwitch = True
            break
        age = input("Please enter age: ")

        myFile.write("{0}, {1}\n".format(name, age))

        print("Do you want a list of you guests so far?")
        listPrint = input("('yes' to print, 'end' to exit): ").lower()
        if listPrint == "end":
            print("Goodbye")
            quitSwitch = True
            break

        myFile.close()

        fileName = "CVSguestList.txt"
        accessMode = "r"

        with open(fileName, accessMode) as myCSVReader:
            CVSguestList = csv.reader(myCSVReader)
            for row in CVSguestList:
                print("Name: {0:10s}Age: {1}".format(row[0], row[1]))

    
        try:
            myFile = open(fileName, accessMode)
        except FileNotFoundError:
            print("That is an invalid folder directory.")
        except PermissionError:
            print("You don't have permission to accesss that folder.")
        except OSError:
            print("Invalid file name.")
        except:
            print("An unknown error has occured.")

main()