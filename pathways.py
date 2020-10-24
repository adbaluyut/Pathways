
from Node import Node
import copy

N = 5
# N = int(input("Enter the size of the game board:\n"))


def main():

    board = Node(N=N)
    board.resetGrid()
    board.insertMove(2, 0, 'H')
    board.insertMove(2, 2, 'H')
    board.insertMove(3, 3, 'H')
    board.insertMove(4, 4, 'H')
    board.insertMove(0, 4, 'H')
    # board.draw()
    # getHumanPlayerMove(board)
    # board.draw()
    # board.generateStates()
    board.draw()
    if (board.checkForAWin('H')):
        print('Win!')
    else:
        print('nah brah')


def getWhoMovesFirst():

    return input("Who moves first? (h/m)")


def getHumanPlayerMove(board):
    invalid_move = True
    while (invalid_move):
        x = int(input('\nEnter the x coordinate of your desired move:'))
        y = int(input('\nEnter the y coordinate of your desired move:'))

        if ((x < N and y < N) and board.state[x][y] == ' '):
            board.insertMove(x, y, 'H')
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
