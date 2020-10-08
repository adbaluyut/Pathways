
import copy

rows = columns = 5

def main():
    
    board = initBoard();
    drawBoard(board)


# Change to ResetGrid?
def initBoard():

    board = []

    for i in range(rows): 
        board.append([])
        for j in range(columns):
            board[i].append('o')

    return board


def getWhoMovesFirst():
    
    return = input("Who moves first? (h/m)")


def getHumanPlayerMove():
    pass


def generateComputerPlayerMove():
    pass


def checkForAWin(board):
    pass


def minimax(board):
    b = copy.deepcopy(board)


def alpha-beta(board):
    b = copy.deepcopy(board)


def drawBoard(b):

    for i in range(rows):
        for j in range(columns):
            print(f'{b[i][j]}', end=' ')
        print()        
    print()


if __name__ == "__main__":
    main()