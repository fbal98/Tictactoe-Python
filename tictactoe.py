initBoard = [["_", "_", "_"],
             ["_", "_", "_"],
             ["_", "_", "_"]]

xTurn = True

# print game instruction
print("\nHello and Welcome to Firas' tic tac toe ---------------#\n"
      "Please enter the row and column for each move ---------#\n"
      "The first player to complete three in a row wins the game\n"
      "Enter Q to quit")


def drawBoard(currentBoard):
    for i in currentBoard:
        print(i[0] + '|' + i[1] + '|' + i[2])
    print("+---------+")


def isFull(board):
    for i in board:
        if i[0] or i[1] or i[2] == "_":
            return False
        else:
            return True


def isOccupied(board, r, c):
    if board[r][c] == "_":
        return False
    else:
        return True


def drawx(board, r, c):
    if isFull(board):
        print("The board is Full baby")
    elif isOccupied(board, r, c):
        print("ahh baby too much for one space")
    else:
        board[r][c] = "X"
        global xTurn
        xTurn = False
        # drawBoard(board)


def drawy(board, r, c):
    if isFull(board):
        print("The board is Full baby")
    elif isOccupied(board, r, c):
        print("ahh baby too much for one space")
    else:
        board[r][c] = "O"
        global xTurn
        xTurn = True
        # drawBoard(board)


def isThereWinner(board):
    if horizontalWinner(board) or verticalWinner(board) or diagonalWinner(board):
        return True
    else:
        return False


def diagonalWinner(board):
    if (board[0][0] + board[1][1] + board[2][2] == "XXX") or \
            (board[0][2] + board[1][1] + board[2][0] == "XXX") or \
            (board[0][0] + board[1][1] + board[2][2] == "OOO") or \
            (board[0][2] + board[1][1] + board[2][0] == "OOO"):
        return True


def horizontalWinner(board):
    for i in board:
        if i[0] and i[1] and i[2] == "X":
            return True
        elif i[0] and i[1] and i[2] == "O":
            return True
        else:
            return False


def verticalWinner(board):
    if (board[0][0] + board[1][0] + board[2][0] == "XXX") or \
            (board[0][1] + board[1][1] + board[2][1] == "XXX") or \
            (board[0][2] + board[1][2] + board[2][2] == "XXX") or \
            (board[0][0] + board[1][0] + board[2][0] == "OOO") or \
            (board[0][1] + board[1][1] + board[2][1] == "OOO") or \
            (board[0][2] + board[1][2] + board[2][2] == "OOO"):
        return True

def resetBoard(board):
    board = [["_", "_", "_"],
             ["_", "_", "_"],
             ["_", "_", "_"]]
    return board

# ------ MAIN ------#
gameBoard = list(initBoard)
while True:
    # draws the first board
    drawBoard(gameBoard)
    # take input from user
    r = input("enter row: ")
    if r.lower() == "q":
        break
    c = input("enter column: ")
    if int(r) > 2 or int(c) > 2 or int(r) < 0 or int(c) < 0:
        print("Invalid entry!!")

    else:
        # check turns
        if xTurn:
            drawx(gameBoard, int(r), int(c))
        else:
            drawy(gameBoard, int(r), int(c))

        if isThereWinner(gameBoard):
            print("Game Over!")
            again = input("do you want to play again(Y or N)?")
            if again.lower() == "y":
                gameBoard = resetBoard(gameBoard)
                continue
            else:
                break
