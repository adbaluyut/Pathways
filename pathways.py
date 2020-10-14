
from Node import Node
import copy

rows = 5
columns = 5

def main():
    
    board = Node(rows=rows, cols=columns)
    board.resetGrid()
    board.insertMove(2,0,'H')
    board.insertMove(2,2,'H')
    board.insertMove(3,3,'H')
    board.insertMove(4,4,'H')
    board.draw()
    board.checkForAWin(2,2,'H')


def insertMove(r,c,b,location):
    b[r][c] = location


def getWhoMovesFirst():
    
    return input("Who moves first? (h/m)")


def getHumanPlayerMove():
    pass


def generateComputerPlayerMove():
    pass


def minimax(board):
    b = copy.deepcopy(board)


def alpha_beta(board):
    b = copy.deepcopy(board)


if __name__ == "__main__":
    main()