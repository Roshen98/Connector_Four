# importing required libraries
import random

# global declarations
ROWS = 6
rowList = [1, 2, 3, 4, 5, 6]
COLUMNS = 7
colList = [1, 2, 3, 4, 5, 6, 7]
computerWinMessage = "Computer won!"
playerWinMessage = "You won!"
drawMessage = "It is a draw!"


def menu():
    # game menu that starts the game or quit
    print('Welcome to connect four it is probably better to just buy it tho')
    while True:
        board = initializeBoard()
        print()
        print('1. Player vs Computer')
        print('2. Quit')
        try:
            option = int(input('Pick a number:'))
            if option == 1:
                vsComputer(board)
            elif option == 2:
                break
            else:
                print('PICK 1, 2, or 3 ONLY')
        except ValueError:
            print('Numbers only!')


def pickSymbolStyle():
    # returns the symbol choices of the game
    while True:
        print('1. X and O ')
        print('2. Blue dot and Red dot')
        try:
            option = int(input('Pick number 1-2: '))
            if option == 1:
                return "X/O"
            elif option == 2:
                return "B/R"
            else:
                print('Numbers 1-2 only')
        except ValueError:
            print('Numbers only!')


def pickXorO():
    # returns the player's choice of X or O
    while True:
        print('1. O')
        print('2. X')
        try:
            option = int(input('pick a symbol: '))
            if option == 1:
                return "O"
            elif option == 2:
                return "X"

            else:
                print('pick a number 1 or 2')
        except ValueError:
            print('enter a number')


def pickBorR():
    # returns the player's choice of R or B
    while True:
        print('1. B')
        print('2. R')
        try:
            option = int(input('pick a symbol: '))
            if option == 1:
                return "B"
            elif option == 2:
                return "R"

            else:
                print('pick a number 1 or 2')
        except ValueError:
            print('enter a number')


def whoGoingFirst():
    # returns whoever is going first
    while True:
        first = input('Who is going first:[bot/player] ')
        if first == 'bot' or first == 'player':
            return first
        else:
            print('Enter bot/player only!')


def getComputerSymbolXO(symbol):
    # returns X if the player choice O earlier and vice versa
    if symbol == "X":
        return "O"
    else:
        return "X"


def getComputerSymbolBR(symbol):
    # returns B if the player choice R earlier and vice versa
    if symbol == "B":
        return "R"
    else:
        return "B"


def vsComputer(b):
    # start the game with the chosen symbol
    printBoard(b)
    SymbolType = pickSymbolStyle()
    if SymbolType == "X/O":
        yourSymbol = pickXorO()
        computerSymbol = getComputerSymbolXO(yourSymbol)
    else:
        yourSymbol = pickBorR()
        computerSymbol = getComputerSymbolBR(yourSymbol)

    first = whoGoingFirst()

    # while the game did not end, if computer is going first, it makes a choice and vice versa
    while True:
        if first == 'bot':
            computerTurn(b, computerSymbol)
        else:
            playerTurn(b, yourSymbol)

        printBoard(b)
        print()
        if gameEnd(b, first, yourSymbol, computerSymbol):
            break

        first = changeTurn(first)


def gameEnd(b, goesFirst, playerSymbol, AISymbol):
    # returns true if the game ended as a win, lose or draw and also prints the result messages
    if winResult(b, goesFirst, playerSymbol, AISymbol) == computerWinMessage:
        print(computerWinMessage)
        return True
    elif winResult(b, goesFirst, playerSymbol, AISymbol) == playerWinMessage:
        print(playerWinMessage)
        return True
    elif draw(b):
        print(drawMessage)
        return True
    else:
        return False


def draw(b):
    # returns false if the board still has empty tiles, otherwise return true
    for row in range(ROWS):
        for col in range(COLUMNS):
            if b[row][col] == "-":
                return False

    return True


def resultDisplay(current_turn):
    # returns the result message given the current turn
    if current_turn == "bot":
        return computerWinMessage
    else:
        return playerWinMessage


def turnMade(current_turn, playerSymbol, AISymbol):
    # returns the symbol based on the current turn
    if current_turn == "bot":
        return AISymbol
    else:
        return playerSymbol


def winResult(b, goesFirst, playerSymbol, AISymbol):
    # returns the result message if the game ended, otherwise return nothing
    turn = turnMade(goesFirst, playerSymbol, AISymbol)
    for row in range(ROWS):
        for col in range(COLUMNS):
            if col == COLUMNS - 3:
                break

            elif b[row][col] == turn and \
                    b[row][col + 1] == turn and \
                    b[row][col + 2] == turn and \
                    b[row][col + 3] == turn:
                return resultDisplay(goesFirst)

    for col in range(COLUMNS):
        for row in range(ROWS):
            if row == ROWS - 3:
                break

            elif b[row][col] == turn and \
                    b[row + 1][col] == turn and \
                    b[row + 2][col] == turn and \
                    b[row + 3][col] == turn:
                return resultDisplay(goesFirst)

    if diagonal(b, turn):
        return resultDisplay(goesFirst)

    return


def diagonal(board, turn):
    # returns true if the diagonal tiles are four, otherwise return false
    for row in range(ROWS):
        for col in range(COLUMNS):
            if board[row][col] == turn:
                # bottom left to top right diagonal check

                # bottom left first input check
                # if there are three of the same symbol top right
                if row + 3 < ROWS and col - 3 > -1 and \
                        board[row + 1][col - 1] == turn and \
                        board[row + 2][col - 2] == turn and \
                        board[row + 3][col - 3] == turn:
                    return True

                # bottom left second input check
                # if there are two of the same symbol top right
                # and check if there is one of the same symbol left bottom
                if row + 2 < ROWS and row - 1 > -1 and \
                        col + 1 < COLUMNS and col - 2 > -1 and \
                        board[row - 1][col + 1] == turn and \
                        board[row + 1][col - 1] == turn and \
                        board[row + 2][col - 2] == turn:
                    return True

                # bottom left third input check
                # if there are two of the same symbol right bottom
                # and check if there is one of the same symbol top right
                if row - 2 > -1 and row + 1 < ROWS and \
                        col + 2 < COLUMNS and col - 1 > -1 and \
                        board[row - 1][col + 1] == turn and \
                        board[row - 2][col + 2] == turn and \
                        board[row + 1][col - 1] == turn:
                    return True

                # bottom left fourth input check
                # if there are three of the same symbol bottom left
                if row - 3 > -1 and col + 3 < COLUMNS and \
                        board[row - 1][col + 1] == turn and \
                        board[row - 2][col + 2] == turn and \
                        board[row - 3][col + 3] == turn:
                    return True

                ###################################################
                # top left to bottom right diagonal check

                # top left first input check
                # if there are three of the same symbol bottom right
                if row + 3 < ROWS and col + 3 < COLUMNS and \
                        board[row + 1][col + 1] == turn and \
                        board[row + 2][col + 2] == turn and \
                        board[row + 3][col + 3] == turn:
                    return True

                # top left second input check
                # if there are two of the same symbol bottom right
                # and there is of the same symbol top left
                if row + 2 < ROWS and col + 2 < COLUMNS and \
                        row - 1 > -1 and col - 1 > -1 and \
                        board[row - 1][col - 1] == turn and \
                        board[row + 1][col + 1] == turn and \
                        board[row + 2][col + 2] == turn:
                    return True

                # top left second input check
                # if there are two of the same symbol top left
                # and there is of the same symbol bottom right
                if row - 2 > -1 and col - 2 > -1 and \
                        row + 1 < ROWS and col + 1 < COLUMNS and \
                        board[row - 1][col - 1] == turn and \
                        board[row - 2][col - 2] == turn and \
                        board[row + 1][col + 1] == turn:
                    return True

                # top left fourth input check
                # if there are three of the same symbol top left
                if row - 3 > -1 and col - 3 > -1 and \
                        board[row - 1][col - 1] == turn and \
                        board[row - 2][col - 2] == turn and \
                        board[row - 3][col - 3] == turn:
                    return True

    return False


def changeTurn(goesFirst):
    # returns player turn if the current turn is the computer, otherwise return bot
    if goesFirst == 'bot':
        goesFirst = 'player'
    else:
        goesFirst = 'bot'
    return goesFirst


def pickRow():
    # returns the user input on picking a row number
    while True:
        try:
            row = int(input('Enter row: '))
            if row < 1 or row > ROWS:
                print('wrong row number ur bad')
            else:
                return row - 1
        except ValueError:
            print('Enter numbers only ur bad')


def pickCol():
    # returns the user input on picking a column number
    while True:
        try:
            col = int(input('Enter column: '))
            if col < 1 or col > COLUMNS:
                print('wrong row number ur bad')
            else:
                return col - 1
        except ValueError:
            print('Enter numbers only ur bad')


def computerTurn(b, AISymbol):
    # random column selection of the AI dropping a piece on the board
    randomCol = random.choice(colList) - 1
    if validCol(b, randomCol):
        row = lowestDrop(b, randomCol)
        b[row][randomCol] = AISymbol


def lowestDrop(b, col):
    # returns the index for the piece dropped in the given or chosen column
    for r in range(ROWS):
        if b[r][col] == '-':
            continue
        else:
            return r - 1
    return -1


def validCol(b, col):
    # returns true if there is still available spaces in the column, otherwise return false
    for r in range(ROWS):
        if b[r][col] == '-':
            return True
        else:
            continue
    return False


def playerTurn(b, playerSymbol):
    # make the player to choose a valid column
    while True:
        col = pickCol()
        if validCol(b, col):
            row = lowestDrop(b, col)
            b[row][col] = playerSymbol
            break
        else:
            print('not valid column')


def initializeBoard():
    # building the empty board in the form of two-dimensional array
    rowList = []
    for i in range(0, ROWS):
        columnList = []
        for j in range(0, COLUMNS):
            columnList.append('-')
        rowList.append(columnList)
    return rowList


def printBoard(board):
    # displays the board
    for r in range(ROWS):
        for c in range(COLUMNS):
            print(board[r][c], end=" ")
        print()


if __name__ == '__main__':
    # main function that implements the functions
    menu()
