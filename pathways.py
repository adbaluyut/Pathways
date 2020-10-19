
from Node import Node
import copy

rows = columns = 5

def main():
    
    board = Node(rows=rows, cols=columns)
    board.resetGrid()
    # board.insertMove(2,0,'H')
    # board.insertMove(2,2,'H')
    # board.insertMove(3,3,'H')
    # board.insertMove(4,4,'H')
    board.draw()
    getHumanPlayerMove(board)
    board.draw()
    board.checkForAWin(2,2,'H')


def getWhoMovesFirst():
    
    return input("Who moves first? (h/m)")


def getHumanPlayerMove(board):
    invalid_move = True
    while (invalid_move):
        x = int(input('\nEnter the x coordinate of your desired move:'))
        y = int(input('\nEnter the y coordinate of your desired move:'))

        if ((x < rows and y < columns) and board.state[x][y] == ' '):
            board.insertMove(x,y,'H')
            invalid_move = False
        else: 
            print('\nInvalid move, please try new coordinates.')

def generateComputerPlayerMove():
    pass


def minimax(board):
    b = copy.deepcopy(board)


def alpha_beta(board):
    b = copy.deepcopy(board)


if __name__ == "__main__":
    main()