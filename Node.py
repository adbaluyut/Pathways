
from collections import defaultdict, deque
import copy


class Node:

    # Initiates an N x N grid
    def __init__(self, state=None, N=None, parent=None, heuristic=None):

        self.state = state
        self.N = N
        self.parent = parent
        # self.alpha = -1000000
        # self.beta = 1000000
        self.heuristic = heuristic
        self.value = None

    def resetGrid(self):

        self.state = []

        for i in range(self.N):
            self.state.append([])
            for j in range(self.N):

                if (i % 2) == 0 and (j % 2) == 1:
                    self.state[i].append('H')
                elif (i % 2) == 1 and (j % 2) == 0:
                    self.state[i].append('M')
                    # self.state[i].append(' ')
                else:
                    self.state[i].append(' ')

    def draw(self):

        for i in range(self.N - 1, -1, -1):
            for j in range(self.N):
                print(f'{self.state[i][j]}', end=' ')
            print()
        print()

    def insertMove(self, r, c, playerType):

        self.state[r][c] = playerType

    def isFull(self):

        full = True

        for i in range(self.N):
            if ' ' in self.state[i]:
                full = False

        return full

    def checkMoves(self):

        index = self.findEmpty()
        neighbors = []
        neighbors.append(self.up(index))
        neighbors.append(self.down(index))
        neighbors.append(self.left(index))
        neighbors.append(self.right(index))

        return [i for i in neighbors if i]

    def generateStates(self, playerType):

        stateList = []

        for i in range(self.N):
            for j in range(self.N):
                if self.state[i][j] == ' ':
                    self.state[i][j] = playerType
                    self.state[i][j] = ' '
                    # New Node will have a copy of board.state
                    stateOption = Node(N=self.N, state=copy.deepcopy(self.state), parent=self)
                    # New Node.state[i][j] = 'M'
                    stateOption.state[i][j] = playerType
                    # store the state
                    stateList.append(stateOption)

        # for state in stateList:
        #     state.draw()

        # print(len(stateList))
        return stateList

    def checkForAWin(self, playerType):

        start = deque()
        end = deque()

        for i in range(self.N):
            if self.state[i][0] == playerType:
                start.append((i, 0))
            if self.state[i][self.N - 1] == playerType:
                end.append((i, self.N - 1))
        
        if len(start) != 0 and len(end) != 0:
            while start:

                s = start.popleft()

                while end:

                    e = end.popleft()
                    #search
                    if self.checkPath(s, e, playerType):

                        print(f"{'Human' if playerType == 'H' else 'Computer'} Player  wins!")
                        return True
                    # print(f"{s},{e}")

        return False

    def checkPath(self, source, destination, playerType):

        current = source
        fringe = deque()
        fringe.append(current)
        closed = []

        while fringe:

            next = fringe.popleft()
            closed.append(next)

            if next == destination:

                return True

            for neighbor in self.checkMoves(next[0], next[1], playerType):

                if neighbor not in closed:

                    fringe.append(neighbor)
                    closed.append(neighbor)
        
        return False

    def checkMoves(self, r, c, playerType):

        neighbors = []
        neighbors.append(self.up(r, c, playerType))
        neighbors.append(self.down(r, c, playerType))
        neighbors.append(self.left(r, c, playerType))
        neighbors.append(self.right(r, c, playerType))        

        return [i for i in neighbors if i]

    # region up, down, left, right
    def up(self, r, c, playerType):
        
        if r < self.N - 1 and self.state[r + 1][c] == playerType:
            return (r + 1, c)
        else:
            return None
    
    def down(self, r, c, playerType):
        
        if r > 0 and self.state[r - 1][c] == playerType:
            return (r - 1, c)
        else:
            return None

    def left(self, r, c, playerType):
        
        if c > 0 and self.state[r][c - 1] == playerType:
            return (r, c - 1)
        else:
            return None

    def right(self, r, c, playerType):
        
        if c < self.N - 1 and self.state[r][c + 1] == playerType:
            return (r, c + 1)
        else:
            return None
    #endregion
