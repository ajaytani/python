def getPossibleCandidates(board, row,col):
    legal_numbers = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

    numbersUsedInRow = set()
    numbersUsedInColumn = set()

    for i in range(0,9):
        numbersUsedInRow.add(board[row][i])
        numbersUsedInColumn.add(board[i][col])

    subBoardTopLeftRow = row - (row % 3)
    subBoardTopLeftColumn = col - (col % 3)
    numbersUsedInSubBoard = set()

    for i in range(0,3):
        for j in range(0,3):
            numUsedInSubBoard = board[subBoardTopLeftRow + i][subBoardTopLeftColumn + j]
            numbersUsedInSubBoard.add(numUsedInSubBoard)

    disqualified = set()
    validNumbersForCurrentSquare = legal_numbers.difference(set([]).union(numbersUsedInSubBoard, numbersUsedInRow, numbersUsedInColumn))
    return validNumbersForCurrentSquare

def getLeastNumofCandidatesIndex(board):

    minIndex = None
    minNumofCandidates = float('inf')

    for i in range(0,9):
        for j in range(0,9):

            numOfCurrentCandidates = len(getPossibleCandidates(i,j))
            if board[i][j] ==0 and numOfCurrentCandidates < minNumofCandidates:
                minIndex = [i,j]
                numOfMinCandidates = numOfCurrentCandidates

    return minIndex


def getFirstEmptySquare(board):
    for i in range(0,9):
        for j in range(0,9):
            if board[i][j] == 0:  # i.e. the square is empty
                return [i, j]

    return None


def rowContains(board, row, num):

    for col in range(0,9):
        if (board[row][col] == num):
            return True

    return False

def colContains(board, col, num):

    for row in range(0,9):
        if (board[row][col] == num):
            return True

    return False

def subBoardContains(board, subBoardIndex, num):

    topLeftPositionRow = subBoardIndex - (subBoardIndex % 3)

    # the column of the top left position in the index-th square of the sub-board
    topLeftPositionCol = 3 * (subBoardIndex % 3)

    for i in range(0,3):
        for j in range(0,3):
            if (board[topLeftPositionRow + i][topLeftPositionCol + j] == num):
                return True
    return False


def isComplete(board):

    nextEmptySquare = getFirstEmptySquare(board)
    if nextEmptySquare:
        return False

    for index in range(0,9):
        for num in range(1,10):
            isNumberMissing =  not rowContains(board, index, num) or not colContains(board, index, num) or not subBoardContains(board, index, num)

        if isNumberMissing:
            return False

    # all numbers appear exactly once in each row, column and sub-board
    return True


def sudokuSolve(board):
    # Input: board - a sudoku board as described in the question
    # Output: True if the board is solvable

    if isComplete(board):
        return True  # base case for the recursion

    # get a pair: the row and column of the first empty square in board
    currentSquareIndex = getFirstEmptySquare(board)

    # If the board is full but not completed, it"s invalid
    if not currentSquareIndex:
        return False

    row = currentSquareIndex[0]
    col = currentSquareIndex[1]
    candidatesForCurrentSquare = getPossibleCandidates(board, row, col)

    for candidate in candidatesForCurrentSquare:
        # Assume the current candidate is a good match, and keep solving
        board[row][col] = candidate
        if sudokuSolve(board):
            return True

        board[row][col] = 0

    return False
board = [[9,1,0,0,7,0,0,0,8],
[3,0,0,0,0,9,0,1,0],
[0,7,0,8,0,5,0,9,4],
[2,0,7,0,0,4,0,0,0],
[0,0,0,0,0,7,8,0,2],
[0,0,4,9,0,0,0,7,0],
[7,0,6,5,9,0,0,0,0],
[0,5,9,0,0,0,2,0,7],
[0,0,0,0,2,0,9,0,1]]


print(sudokuSolve(board))