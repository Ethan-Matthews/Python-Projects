"""
Student Name:   Ethan Matthews
Program Title:  Battleship
Description:    Design and develop a program that replicates the functionality of the provided
                sample application, a simple version of the game Battleship.
"""
"""
 1. Load external file into list.
 2. Copy list and replace characters with spaces to create the visible game board, so there will be two lists.
 3. Create a function for the players turn. Re-call function per turn.
 4. Function must contain input checks to account for input errors.
 5. Letter Co-ordinates will need to tranlated to integers so they can be used for index calls. (Maybe a loop to compare to a string of letters in sequence?)
 6. Will need to check user input against hidden list that contains map data.
 7. Append visible list with hidden list data (hits or misses). Probably need to do some string splitting and re-concatenation.
 8. Output updated visable list, repeat for every user turn.
 9. At the end will need to compare missile count or number of hits to end program appropriately.
10. While loop will be necessary to meet program ending conditions.
"""
# This function contains all the nesseary code to complete one turn.
# Input, input checks, co-ordinate splitting/translating and map output.
def playerTurn(p_hiddenMap, p_visibleMap, p_missileCount, p_hitCount):
    # Used to check letter co-ordinates in sequence to assign a numeric value to 'letterCoordinates'
    letterString = "ABCDEFGHIJ"
    # Switch will keep user in loop until proper input is recived.
    inputCheck = False
    while inputCheck == False:
        # user input for co-ordinates
        target = str(input("Choose your target(Ex. A1): ")).upper()
        # Checks if target is empty. Re-prompts user if True.
        if target == "":
            continue
        # letterCoodinate is assigned first letter in string.
        letterCoordinate = target[0]
        # Check if first letter of target string is an alphabet character. 
        if str(letterCoordinate).isalpha() == False:
            continue
        # Removes first letter from target string allowing the remaining to be assigned as the second numberCoordinate variable.
        for letter in letterString:
            if letter == letterCoordinate:
                numberCoordinate = target.replace(letter, "")
                break
        # Checks if numberCoordinate is a numeric character.
        if str(numberCoordinate).isnumeric() == False:
            continue
        # Casts numberCoordinate from a string to an integer. Checks if values are in viable range (A-J 1-10).
        # If IF statement is true, changes inputCheck to true and breaks loop.
        for letter in letterString:
            for counter in range(len(p_visibleMap)):
                numberCoordinate = int(numberCoordinate)
                if letter == letterCoordinate and counter == numberCoordinate:
                    inputCheck = True
                    break
            if inputCheck == True:
                break
    # Changes letterCoordinate to a the corresponding column index value.
    # Adds the CommaCounter to letterCoordinate to account for character spaces between columns.
    counter = 1
    commaCounter = 0
    for letter in letterString:
        commaCounter += 1
        if letter == letterCoordinate:
            letterCoordinate = counter
            break
        counter += 1
    letterCoordinate += commaCounter
    # If the target row is 10, will add one to letterCoordinate to account for second digit in '10'.
    if numberCoordinate == 10:
        letterCoordinate += 1
    # Checks the hiddenMap list with number/letterCoordinates for value at that index.
    stringReplace = []
    # If statement for value of 1(hit). Increasses hit counter and decreases missile count.
    if p_hiddenMap[numberCoordinate][letterCoordinate] == "1":
        print("HIT!!!!!")
        p_hitCount =+ 1
        p_missileCount -= 1
        print("You have {0} missiles remaining".format(p_missileCount))
        # Splits numberCoordinate row string into stringReplace list as individual elements.
        for row in p_visibleMap[numberCoordinate]:
            for column in row:
                stringReplace.append(column)
        # Replaces the value at the letterCoordinate column with x for hit.
        stringReplace[letterCoordinate] = "X"
        stringAmended = ""
        # joins all amended elements into single string again.
        stringAmended = ''.join(stringReplace)
        # replaces numberCoordinate row in visible map with ammended string.
        p_visibleMap[numberCoordinate] = stringAmended
        # Re-prints amended visible map.
        for counter in range(len(p_visibleMap)):
            print(p_visibleMap[counter], end="")
        print("\n")
    # If statement for value of 0(miss). Decreases missile count.
    elif p_hiddenMap[numberCoordinate][letterCoordinate] == "0":
        print("Miss")
        p_missileCount -= 1
        print("You have {0} missiles remaining".format(p_missileCount))
        # Splits numberCoordinate row string into stringReplace list as individual elements.
        for row in p_visibleMap[numberCoordinate]:
            for column in row:
                stringReplace.append(column)
        # Replaces the value at the letterCoordinate column with O for miss.
        stringReplace[letterCoordinate] = "O"
        stringAmended = ""
        # joins all amended elements into single string again.
        stringAmended = ''.join(stringReplace)
        # replaces numberCoordinate row in visible map with ammended string.
        p_visibleMap[numberCoordinate] = stringAmended
        # Re-prints amended visible map.
        for counter in range(len(p_visibleMap)):
            print(p_visibleMap[counter], end="")
        print("\n")
    # returns ammended visible map, missilecount and hit counter.
    return p_visibleMap, p_missileCount, p_hitCount

def main():
    # File name and access mode.
    battleshipFileName = "map.txt"
    accessMode = "r"
    #Open File.
    gameMap = open(battleshipFileName, accessMode)
    # Pre-initialized lists and letterlist for first row of game map.
    hiddenMap = []
    visibleMap = []
    letterList = "  A B C D E F G H I J\n"
    # Add letterList to first row of both lists.
    hiddenMap.append(letterList)
    visibleMap.append(letterList)
    # variable for singleline reading from file.
    singleLine = gameMap.readline()
    # Counter for adding row numbers.
    counter = 1
    # Appends singlelines from file to both lists. 
    while singleLine:
        hiddenMap.append("{0},".format(counter) + str(singleLine))
        # Replaces all grid chacters with spaces. Except row and column 0.
        singleLine = singleLine.replace(","," ")
        singleLine = singleLine.replace("0"," ")
        singleLine = singleLine.replace("1"," ")
        visibleMap.append("{0} ".format(counter) + str(singleLine))
        singleLine = gameMap.readline()
        counter += 1
    # Starting Message Banners.
    print("\nLet's play Battleship!")
    print("You have 30 missiles to fire to sink all five ships.")
    # Starting missile count and pre-initialized hit counter.
    missileCount = 30
    hitCount = 0
    # Prints visible map.
    for counter in range(len(visibleMap)):
        print(visibleMap[counter], end="")
    print("\n")
    # While loop controls winning/losing game.
    # When no missiles are left or hitcount is 17 the loop will terminate.
    while missileCount != 0 or hitCount < 17:
        #Function call for actions on every turn. Repeats every turn.
        visibleMap, missileCount, newHitCount = playerTurn(hiddenMap, visibleMap, missileCount, hitCount)
        # Updates hit counter every turn.
        hitCount += newHitCount
        # If hit counter is 17 you win. Breaks loop. Checked every turn.
        if hitCount == 17:
            print("YOU SANK MY ENTIRE FLEET!")
            print("You had 17 out of 17 hits, which sank all the ships.")
            print("You Won, congratulations!")
            break
        # If missile count is 0 you lose. Breaks loop. Checked every turn.
        elif missileCount == 0:
            print("GAME OVER.")
            print("You had {0} of 17 hits, but didn't sink all the ships.")
            print("Better luck next time.")
            break
    # Close accessed file.
    gameMap.close()

#Do not change any of the code below!
if __name__ == "__main__":
    main()