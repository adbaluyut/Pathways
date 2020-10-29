
from Node import Node
import copy
import random
from datetime import date, datetime


# N = 5
N = int(input("Enter the size(N) of the game board (N x N):\n"))


def main():

    # our board is initially on a maximizing layer
    board = Node(N=N)
    board.resetGrid()

    # test = createEvalTable(board.state)
    # for i in test:
    #     print(i)

    playGame(board)


def playGame(board):
    
    board.draw()

    depth = 3
    currentPlayer, maximizingPlayer = getWhoMovesFirst()

    while True:

        if board.isFull():
            print("It's a draw!")
            break

        if currentPlayer == 'H':

            getHumanPlayerMove(board)
            currentPlayer = 'M'
        
        else:

            print("Computer making it's move")
            temp = generateComputerPlayerMove(board, board, depth, -1000, +1000, maximizingPlayer, 'M')[0]
            if temp is not None:
                board = temp

            # print("printing the returned board")
            # board.draw()
            # print("________________________")
            # this returns the state to the next move we can make
            
            if board.parent is not None:
                while board.parent.parent:
                    # print(board.parent)
                    board = board.parent
            board.parent = None

            currentPlayer = 'H'
    
        board.draw()
        # break

        if board.checkForAWin('H' if currentPlayer == 'M' else 'M')[0]:
            print(f"{'Human' if currentPlayer == 'M' else 'Computer'} Player wins!")                        
            break


# if computer moves first computer is a maximizing player
def getWhoMovesFirst():

    maximizing = True
    first = input("Who moves first? (h/m)").upper()

    # if first == 'H':
    #     maximizing = True
    
    return first, maximizing


def getHumanPlayerMove(board):

    invalid_move = True
    while (invalid_move):
        x = int(input('\nEnter the row of your desired move:'))
        y = int(input('\nEnter the column of your desired move:'))

        if ((x < N and y < N) and board.state[x][y] == ' '):
            board.insertMove(x, y, 'H')
            invalid_move = False
        else:
            print('\nInvalid move, please try new coordinates.')


def generateComputerPlayerMove(board, staticBoard, depth, alpha, beta, maximizingPlayer, playerType):

    curState = copy.deepcopy(board)
    state = None
    children = curState.generateStates(playerType)
    opponent = 'M' if (playerType == 'H') else 'H'

    # for s in children:
    #     s.draw()

    if (depth == 0 or curState.checkForAWin('M')[0] or len(children) == 0):
        # print(f"cur: {curState}")
        if curState is None:
            return
        return curState, staticEvaluation(curState, staticBoard, playerType)

    if maximizingPlayer:
        maxEvaluation = -1000
        
        # curState is the generated States
        for child in children:
            newState, evaluation = generateComputerPlayerMove(child, staticBoard, depth -1, alpha, beta, False, opponent)
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
            newState, evaluation = generateComputerPlayerMove(child, staticBoard, depth - 1, alpha, beta, True, opponent)
            if evaluation < minEvaluation:
                state = newState
            minEvaluation = min(minEvaluation, evaluation)
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        # print("minimizing")
        # state.draw()
        return state, minEvaluation
    

def staticEvaluation(curState, staticBoard, playerType): #curState is a node and this assigns a value to it
    
    value = 0
    table = createEvalTable(staticBoard.state)
    isWin = curState.checkForAWin(playerType)
    opponentWin = curState.checkForAWin('H' if playerType == 'M' else 'M')

    # can have a for loop here and compare curState.State[i][j] and table[i][j]
    # for i in table:
    #     print(i)

    for i in range(N):
        for j in range(N):
            if curState.state[i][j] != staticBoard.state[i][j]:
                # print(f"\n{i}{j}")
                # print(f"cur: {curState.state[i][j]}")                
                # print(f"static: {staticBoard.state[i][j]}")
                # print(f"table: {table[i][j]}")
                value += table[i][j]
    
    # if this is a winning state give it a high value
    if isWin[0]:
        value += 100
    # if this is a losing state give it a low value
    if opponentWin[0]:
        value -= 100
    
    
    # depending on path length add a value

    # depending on opponents path length subtract a value

    # if we place it in a column with no playerType give add to value else + 0?

    # random.seed(datetime.now())
    # curState.heuristic = random.randint(1, 50)
    # # print(f"heuristic value = {curState.heuristic}")
    # return curState.heuristic

    # if all up, down, left, right is other player or out of bounds

    return value

# def createEvalTable(board):
    
#     b = copy.deepcopy(board)
#     topoMap = copy.deepcopy(board)

#     maxValue = 10000
#     minValue = -10000
#     lt_score = 200
#     gt_score = 200

#     for i in range(N):
#         for j in range(N):
            
#             if i == 0:
#                 b[i][j] = minValue
#             elif i == N - 1:
#                 b[i][j] = minValue
#             if j == 0:
#                 b[i][j] = minValue
#             elif j == N - 1:
#                 b[i][j] = minValue      

#             if j == (N - 1) // 2:
#                 topoMap[i][j] = maxValue - 100
            
#             if i == (N - 1) // 2 and j == (N - 1) // 2:
#                 topoMap[i][j] = maxValue

#             if  j < (N - 1) // 2:
#                 topoMap[i][j] = minValue + lt_score
#                 lt_score = lt_score + 200

#             if j > (N - 1) // 2:
#                 topoMap[i][j] = maxValue - gt_score
#                 gt_score = gt_score + 200
    
#     # for i in topoMap:
#     #     print(i)
    
#     for i in range(N):
#         for j in range(N):
#             if board[i][j] == ' ':

#                 b[i][j] = topoMap[i][j]
#     # for i in b:
#     #     print(i)
                
#     return b

def createEvalTable(board):
    
    b = copy.deepcopy(board)
    maxValue = 1000
    minValue = -1000
    count = 0

    
    for i in range(N):
        for j in range(N):
            if board[i][j] == ' ':

                b[i][j] = 500

                if i == 0:
                    b[i][j] = minValue
                elif i == N - 1:
                    b[i][j] = minValue
                if j == 0:
                    b[i][j] = minValue
                elif j == N - 1:
                    b[i][j] = minValue               
                # if the board is in the middle
                if i == (N - 1) // 2 and j == (N - 1) // 2:
                    b[i][j] = maxValue

                # if (j < (N - 1) // 2) and (j > 0):
                #     b[i][j] = b[i][j+2] - 100
                # else:
                #     b[i][j] = b[i][j-2] - 100
                
                

    return b


if __name__ == "__main__":
    main()
