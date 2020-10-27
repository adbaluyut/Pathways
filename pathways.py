
from Node import Node
import copy
import random
from datetime import date, datetime


N = 5
# N = int(input("Enter the size of the game board:\n"))


def main():

    # our board is initially on a maximizing layer
    board = Node(N=N)
    board.resetGrid()

    playGame(board)


def playGame(board):
    
    board.draw()

    depth = 3
    currentPlayer, maximizingPlayer = getWhoMovesFirst()

    while not board.checkForAWin(currentPlayer):

        if currentPlayer == 'H':

            getHumanPlayerMove(board)
            currentPlayer = 'M'
        
        else:

            print("Computer making it's move")
            board = minimax(board, depth, -1000, +1000, maximizingPlayer, 'M')[0]

            print("printing the returned board")
            board.draw()
            print("________________________")
            # this returns the state to the next move we can make
            while board.parent.parent:
                # print(board.parent)
                board = board.parent
            board.parent = None

            currentPlayer = 'H'
    
        board.draw()
        break


def getWhoMovesFirst():

    maximizing = True
    first = input("Who moves first? (h/m)").upper()

    if first == 'H':
        maximizing = False
    
    return first, maximizing


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


# right now minimax returns a state in the highest position every time
def minimax(board, depth, alpha, beta, maximizingPlayer, playerType):

    curState = copy.deepcopy(board)
    state = None
    children = curState.generateStates(playerType)
    opponent = 'M' if (playerType == 'H') else 'H'

    # for s in children:
    #     s.draw()

    if (depth == 0 or curState.checkForAWin('M')):
        return curState, staticEvaluation(curState)

    if maximizingPlayer:
        maxEvaluation = -1000
        
        # curState is the generated States
        for child in children:
            newState, evaluation = minimax(child, depth -1, alpha, beta, False, opponent)
            if evaluation > maxEvaluation:
                state = newState
            maxEvaluation = max(maxEvaluation, evaluation)
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
        # print("maximizing")
        # state.draw()
        return state, maxEvaluation
      
    else:
        minEvaluation = 1000
        for child in children:
            newState, evaluation = minimax(child, depth - 1, alpha, beta, True, opponent)
            if evaluation > minEvaluation:
                state = newState
            minEvaluation = min(minEvaluation, evaluation)
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        # print("minimizing")
        # state.draw()
        return state, minEvaluation
    

def staticEvaluation(curState): #curState is a node and this assigns a value to it
    random.seed(datetime.now())
    curState.heuristic = random.randint(1, 50)
    # print(f"heuristic value = {curState.heuristic}")
    return curState.heuristic

  
def alpha_beta(board):
    b = copy.deepcopy(board)


if __name__ == "__main__":
    main()
