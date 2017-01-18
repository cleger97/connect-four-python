# File: proj1.py
# Author: Alex Leger
# Date: Started 11/7/2016
# Section: 4
# E-mail: cleger1@umbc.edu
# Description:
# Plays a connect 4 game.
# Collaboration:
# Collaboration was not allowed on this assignment.

# Connect 4
# This program has a sequence of tasks that must be done.
# First, it will load the game. (It will either load from a file or create a new game.)
# Then, it will ask for continual input. There are many options that can happen:
# You can either input a value (to play the game) or input "s" to save the game.
# Check the game every time you put a number to see the potential victory conditions.
# THen, you'll need to print the current board and/or victors.
# At the end, allow user to play again or exit.

# Note to anyone reading the source: Rows are referred to as "lines"
# and columns as "length" because that seems to make more sense
# for arrays. Each "row" is a line of array values and the "columns" 
# determine the length of each line.

# Global Constants

PLAYER1 = 1
PLAYER2 = 2
MIN_COUNT = 5
NOT_OCCUPIED = "_"
PIECE_LIST = { 1 : "X",
               2 : "O" }

# Second, we define generic functions.

# gameInput(minn, maxx): Gets either a string or numeric input. If the value entered is numeric, it
# will not allow you to return a value larger than max or smaller than minimum.
# input: a minimum (int) and maximum (int)
# output: a value (str or int) and a boolean (False if string return, True if int return)

def gameInput(minn, maxx):
    numOut = -1
    validData = False;

    
    while (not validData):
        inLine = input("Enter a value: ")
        # Special Exception - Will return string immediately if input is a string
        try:
            numOut = int(inLine)
        except (ValueError):
            return inLine, False
    
        if (not(numOut < minn or numOut > maxx)):
            return numOut, True
        print("Invalid input!")


# saveFile(name): Saves the game to a file.
# input: file name (str), lines (int), length (int), and the current player (int). 
# Sends a shallow copy of gameBoard as well (list).
# output: confirmation that the save worked

def saveFile(name, lines, length, currentPlayer, gameBoard):
    saveName = name
    fOut = open(saveName, "w")
    
    for line in gameBoard:
        currentLine = ""
        for value in line:
            # Appends the current element + a space
            # For example, 0 turns into 0 1 and 0 1 turns into 0 1 2 
            currentLine = currentLine + value + " "
        # Strip *all* leading and ending whitespace
        # This is super important for loading the file
        currentLine = currentLine.strip()
        # Then we add a newLine to split at when we read in the file
        fOut.write(currentLine + "\n")
        
    # We've now written the entire gameboard. Lastly, we should write the player who's playing and
    # the lines/length.
    
    # Write the player, row, and column.
    current = str(currentPlayer) + " " + str(lines) + " " + str(length)
    fOut.write(current)

    # The file format should now be something like this.
    # 1 2 1 2 0
    # 2 1 2 1 0
    # 1 2 1 1 0
    # 1 2 1 1 0
    # 2 5 4

    # Saves the data to the file.
    fOut.close()

    # Confirm that the function worked - and that the data is saved.
    print("Save to file " + name + " complete!")

# loadFile(name): The inverse of the last function. Reads in the file and proceeds to create
# the game board and sets the player.
# input: file name (string). 
# Sends a shallow copy of gameBoard (list).
# output: line count, length of each line, and currentPlayer.
def loadFile(name, gameBoard):
    fIn = open(name, "r")
    inData = fIn.readlines()
    lines = 0;
    length = 0;
    currentPlayer = 0;

    # Now we have the same data as we left above, but in an array. Seeing as to how the array above
    # did lines by length, we should do the same. But, first, we should handle the last line.
    finalLine = inData[len(inData) - 1].split(" ")
    currentPlayer = int(finalLine[0])
    lines = int(finalLine[1])
    length = int(finalLine[2])
    
    # Now delete the last line so we can iterate over the rest.
    inData.pop(-1)
    
    # Now we handle the rest of the file - by reading it in and re-parsing it as integers.
    for index in range(len(inData)):

        line = inData[index].strip().split(" ")
        # Now we have one of the many lines. We add a new array to the game board - just to
        # replace it later. This is just important so we can write something to that line without
        # throwing an index out of bounds error.

        gameBoard.append([])
        
        # Now write the line to the board space we just created.
        gameBoard[index] = line;
        
    # Saves the file.
    fIn.close()

    return lines, length, currentPlayer

# iNewBoard(lines, length): Creates a new board. Fills with 0 values to avoid errors.
# input: (int) lines and (int) length of each line to be filled. 
# Sends a shallow copy of gameBoard as well (list).
# output: nothing

def iNewBoard(lines, length, gameBoard):
    bLine = []
    # Adds a new 0 to the default line.    
    for i in range(0, length):
        bLine.append(NOT_OCCUPIED)
    # Now add default lines to the game board.
    # Note to future self: The lack of a cast here cost me about an hour of debugging.
    for i in range(0, lines):
        gameBoard.append(list(bLine))
    # Board is now initalized.


# Note for next two functions - always subtract one from the input because the user will attempt to input values into columns starting from 1 to the length.

# checkRow(value): Checks if a column is maxed out.
# input: column number (int).
# Sends a shallow copy of gameBoard as well (list).
# output: boolean (true if maxed or false otherwise)

def checkRow(column, gameBoard):
    if (gameBoard[0][column - 1] != NOT_OCCUPIED):
        return True;
    else:
        return False;

# inputRow(row): Adds a piece to the row.
# input: column (int) and current player (int). 
# Sends a shallow copy of gameBoard as well.
# output: nothing

def inputRow(column, currentPlayer, gameBoard):
    print(len(gameBoard[0]))
    
    for index in range(len(gameBoard) - 1, -1, -1):
        line = gameBoard[index]
        if (line[column - 1] == NOT_OCCUPIED):
            gameBoard[index][column - 1] = PIECE_LIST[currentPlayer]
            return None



# printBoard(): Prints out the current board.
# input: A shallow copy of gameBoard (list).
# output: nothing

def printBoard(gameBoard):
    for index in range(len(gameBoard)):
        line = gameBoard[index]
        currentLine = ""
        for value in line:
            currentLine = currentLine + " " + value
        currentLine = currentLine.strip()
        print(currentLine)


# debugPrint(): Print out a debug version of the board
# input: gameBoard
# output: the board

def debugPrint(gameBoard):
    for part in gameBoard:
        print(part, "\n")
    return None



# Determine Victory conditions

# checkVictory(currentPlayer, lines, length, gameBoard): Determines if a player can win.
# input: currentPlayer (int), lines (int), length (int). 
# Sends a shallow copy of gameBoard as well (list).
# output: a boolean (True if currentPlayer can win, false otherwise)

def checkVictory(currentPlayer, lines, length, gameBoard):
    piece = PIECE_LIST[currentPlayer]

    # debugPrint(gameBoard)
    # Subtracting from a line value brings it *up* one
    # Subtracting from a column brings it to the *left* one

    for line in range(lines):
        for col in range(length):

            # Debug
            # print(line, " ", col)

            # Condition 1 - Vertical Downwards
            # Requires - 3 potential pieces below
            if (line + 3 < lines):
                if (gameBoard[line][col] == piece and gameBoard[line+1][col] == piece and gameBoard[line+2][col] == piece and gameBoard[line+3][col] == piece):
                    return True;
            # Condition 2 - Vertical Upwards
            # Requires - 3 potential pieces above
            if (line - 3 >= 0):
                if (gameBoard[line][col] == piece and gameBoard[line-1][col] == piece and gameBoard[line-2][col] == piece and gameBoard[line-3][col] == piece):
                    return True;
            # Condition 3 - To the Left
            # Requires - 3 potential to the left
            if (col - 3 >= 0):
                if (gameBoard[line][col] == piece and gameBoard[line][col-1] == piece and gameBoard[line][col-2] == piece and gameBoard[line][col-3] == piece):
                    return True;
            # Condition 4 - To the right
            # Requires - 3 potential to the right
            if (col + 3 < length):
                if (gameBoard[line][col] == piece and gameBoard[line][col+1] == piece and gameBoard[line][col+2] == piece and gameBoard[line][col+3] == piece):
                    return True;
            # Condition 5 - Diagonally (BR)
            # Requires - 3 potential pieces below and to the right
            if (col + 3 < length and line + 3 < lines):
                if (gameBoard[line][col] == piece and gameBoard[line+1][col+1] == piece and gameBoard[line+2][col+2] == piece and gameBoard[line+3][col+3] == piece):
                    return True;
            # Condition 6 - Diagonally (BL)
            # Requires - 3 potential pieces below and to the left
            if (col - 3 >= 0 and line + 3 < lines):
                if (gameBoard[line][col] == piece and gameBoard[line+1][col-1] == piece and gameBoard[line+2][col-2] == piece and gameBoard[line+3][col-3] == piece):
                    return True;
            # Condition 7 - Diagonally (UR)
            # Requires: 3 potential pieces above and to the right
            if (col + 3 < length and line - 3 >= 0):
                if (gameBoard[line][col] == piece and gameBoard[line-1][col+1] == piece and gameBoard[line-2][col+2] == piece and gameBoard[line-3][col+3] == piece):
                    return True;
            # Condition 8 - Diagonally (UL)
            # Requires: 3 potential pieces above and to the left
            if (col - 3 >= 0 and line - 3 >= 0):
                if (gameBoard[line][col] == piece and gameBoard[line-1][col-1] == piece and gameBoard[line-2][col-2] == piece and gameBoard[line-3][col-3] == piece):
                    return True;
    # We've now iterated the entire list and found no victory. So, there's no victory.
    return False;

# Check for draws
# You only need to check if every row is filled
# If so, and neither team has won, it's a draw

# checkDraw(lines, length, gameBoard): Checks the board for a draw
# Input: lines (int) and length (int)
# Sends a shallow copy of gameBoard (list) as well.
# Output: a boolean (True if draw, false otherwise):

def checkDraw(lines, length, gameBoard):
    isFilled = True
    for index in range(length):
        if (not checkRow(index, gameBoard)):
            return False;
    if (checkVictory(PLAYER1, lines, length, gameBoard) or checkVictory(PLAYER2, lines, length, gameBoard)):
        return False;

    return True;

# Main statement
# Runs the actual game...

def main():
    # Iterators related to the game itself
    isFinished = False;
    # CurrentIterator has a special function - if the game has ended at least once, they still *cannot* load a save. 
    currentIterator = 0;
    print("Connect 4: The Game")
    print("\n\nThis is a 2 player game.")
    newGame = input("\n\nWould you like to load a save file? (Enter y or n)").strip()

    while (not isFinished):
        # Now, we define the global variables that every function will use.
        gameBoard = []
        lines = 0
        length = 0
        # This will either be 1 for player1 or 2 for player2 at runtime!
        currentPlayer = 0


        # Asks for a save file if you're on the first load and/or cannot input correctly the first time.
        while ((newGame != "y" and newGame != "n") and (currentIterator == 0)):
            print("Invalid Choice!")
            newGame = input("Would you like to load a save file? (Enter y or n)")
        # If they start a new game, call iNewBoard() with the line count and length.
        if (newGame == "n" or currentIterator > 0):
            lines = int(input("Enter the number of rows: "))
            while (lines < MIN_COUNT):
                print("You require at least " + str(MIN_COUNT) + " rows.")
                lines = int(input("Enter the number of rows: "))
            length = int(input("Enter the number of columns: "))
            while (length < MIN_COUNT):
               print("You require at least " + str(MIN_COUNT) + " columns.")
               length = int(input("Enter the number of columns: "))
            iNewBoard(lines,length,gameBoard)
            currentPlayer = PLAYER1
    
        # If they choose to load a game, then ask for save then load the game.
        else: 
            fileName = input("Enter the name of your save file: ")
            lines, length, currentPlayer = loadFile(fileName, gameBoard)
    
        # Now we start the game...
        running = True;
        while (running):
            printBoard(gameBoard);
            print("It is Player " + str(currentPlayer)+ "\'s turn now.")

            finishedTurn = False;
            while (not finishedTurn):
                print("Enter a column - 1 to " + str(length) + " - to drop a piece into or enter s to save.")


                # inData is the value taken in; isGameInput is a boolean determining if the value is a number or string.
                # Send the length because the maximum entry is the length of the list.
                inData, isGameInput = gameInput(1, length)
                # If the value is a number, check the row. If it's invalid, then restart this process.
                if (isGameInput):
                    if (not checkRow(int(inData), gameBoard)):
                        # Inputs the piece, then checks for victory, draw, and then if neither are true, goes into the next player's turn.
                        inputRow(int(inData), currentPlayer, gameBoard)
                        if (checkVictory(currentPlayer, lines, length, gameBoard)):
                            printBoard(gameBoard);
                            print("Player " + str(currentPlayer) + " is victorious!")
                            running = False;
                            finishedTurn = True;
                            
                        elif (checkDraw(lines, length, gameBoard)):
                            printBoard(gameBoard);
                            print("The game is a draw.")
                            running = False;
                            finishedTurn = True;
                        else:
                            print("Player " + str(currentPlayer) + " has successfully dropped a piece into column " + str(inData))
                            # Switch players and end turn.
                            if (currentPlayer == PLAYER1):
                                currentPlayer = PLAYER2
                            else:
                                currentPlayer = PLAYER1
                            finishedTurn = True;
                    else:
                        print("This row is already full!")
                else:
                    # Allows for multiple different text options. For now, the only one necessary is save.
                    # Inputting s will prompt an ask for a file name to save to (which will be appended with .dat)
                    # Then the file will save.
                    if (inData == "s"):
                        fileChoice = input("Enter name of file to save to: ")
                        saveFile(fileChoice, lines, length, currentPlayer, gameBoard)
                        printBoard(gameBoard);
                    else:
                        print("Invalid input!")
        
        currentIterator += 1

        doContinue = "";
        while (not(doContinue == "y" or doContinue == "n")):
            doContinue = input("Would you like to play again? (y/n)")
        if (doContinue == "y"):
            pass;
        elif (doContinue == "n"):
            print("Thanks for playing Connect 4!")
            return None
            
main()

