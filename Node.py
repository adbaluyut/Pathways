
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

        pathLength = 0

        start = deque()
        end = deque()

        for i in range(self.N):
            if self.state[i][0] == playerType:
                start.append((i, 0))
            if self.state[i][self.N - 1] == playerType:
                end.append((i, self.N - 1))
        
        if len(start) != 0 and len(end) != 0:
            while start:

                pathLength += 1

                s = start.popleft()

                while end:

                    e = end.popleft()
                    #search
                    if self.checkPath(s, e, playerType):

                        return (True, pathLength)
                    # print(f"{s},{e}")

        return (False, pathLength)
    
    def checkPossiblePaths(self, playerType):

        arr = copy.deepcopy(self.state)
    
        # to find the path from  
        # top left to bottom right  

        start = deque()
        end = deque()

        for i in range(self.N):
            if arr[i][0] == playerType:
                start.append((i, 0))
            if arr[i][self.N - 1] == playerType:
                end.append((i, self.N - 1))

        # set arr[0][0] = 1 
        arr[0][0] = 1
    
        # Mark reachable (from top left)  
        # nodes in first row and first column.  
        for i in range(1, self.N): 
            if (arr[i][0] != 'H'): 
                arr[i][0] = arr[i-1][0] 
    
        for j in range(1, self.N): 
            if (arr[0][j] != 'H'): 
                arr[0][j] = arr[0][j-1] 
                
        # Mark reachable nodes in  
        # remaining matrix.  
        for i in range(1, self.N): 
            for j in range(1, self.N): 
                if (arr[i][j] != -1): 
                    arr[i][j] = max(self.state[i][j - 1],  
                                    arr[i - 1][j]) 
                                    
        # return yes if right  
        # bottom index is 1 
        return (arr[self.N - 1][self.N - 1] == 1) 
    
        # Driver Code  
        
        # Given array  
        arr = [[ 0, 0, 0, -1, 0 ],  
            [-1, 0, 0, -1, -1],  
            [ 0, 0, 0, -1, 0 ],  
            [-1, 0, -1, 0, -1],  
            [ 0, 0, -1, 0, 0 ]]  
        
        # path from arr[0][0] to arr[row][col]  
        if (isPath(arr)): 
            print("Yes")  
        else: 
            print("No") 

    def newPaths(self, source, destination, playerType):
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
                    if self.newPaths(s, e, playerType):

                        return True
                    # print(f"{s},{e}")

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

    def checkMovesPossible(self, r, c, playerType):

        neighbors = []
        neighbors.append(self.upPossiblePaths(r, c, playerType))
        neighbors.append(self.downPossiblePaths(r, c, playerType))
        neighbors.append(self.leftPossiblePaths(r, c, playerType))
        neighbors.append(self.rightPossiblePaths(r, c, playerType))      

        print(f"neighbors = {neighbors}")  

        return [i for i in neighbors if i]

    # region up, down, left, right
    def upPossiblePaths(self, r, c, playerType):
        
        if r < self.N - 1 and (self.state[r + 1][c] != ('H' if playerType == 'M' else 'M')):
            return [r + 1, c]
        else:
            return None
    
    def downPossiblePaths(self, r, c, playerType):
        
        if r > 0 and (self.state[r - 1][c] != ('H' if playerType == 'M' else 'M')):
            return [r - 1, c]
        else:
            return None

    def leftPossiblePaths(self, r, c, playerType):
        
        if c > 0 and (self.state[r][c - 1] != ('H' if playerType == 'M' else 'M')):
            return [r, c - 1]
        else:
            return None

    def rightPossiblePaths(self, r, c, playerType):
        
        if c < self.N - 1 and (self.state[r][c + 1] != ('H' if playerType == 'M' else 'M')):
            return [r, c + 1]
        else:
            return None
    #endregion
