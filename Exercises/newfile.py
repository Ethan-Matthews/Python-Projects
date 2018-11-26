def main():

    originalFile = "myFile.txt"

    accessMode = "a"

    myFile = open(originalFile, accessMode)

    accessMode = "r"

    filecontents = myFile.readline()
    print(filecontents)
    myFile.close()



main()