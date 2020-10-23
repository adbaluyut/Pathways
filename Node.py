
from collections import defaultdict
import copy


class Node:

    def __init__(self, state=None, N=None, parent=None):
        self.state = state
        self.N = N
        self.parent = parent

    def resetGrid(self):

        self.state = []

        for i in range(self.N):
            self.state.append([])
            for j in range(self.N):

                if (i % 2) == 0 and (j % 2) == 1:
                    self.state[i].append('H')
                elif (i % 2) == 1 and (j % 2) == 0:
                    self.state[i].append('M')
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

    def checkMoves(self):
        index = self.findEmpty()
        neighbors = []
        neighbors.append(self.up(index))
        neighbors.append(self.down(index))
        neighbors.append(self.left(index))
        neighbors.append(self.right(index))

        return [i for i in neighbors if i]

    def generateStates(self):
        stateList = []

        for i in range(self.N):
            for j in range(self.N):
                if self.state[i][j] == ' ':
                    self.state[i][j] = 'M'
                    self.state[i][j] = ' '
                    # New Node will have a copy of board.state
                    stateOption = Node(N=self.N, state=copy.deepcopy(self.state), parent=self)
                    # New Node.state[i][j] = 'M'
                    stateOption.state[i][j] = 'M'
                    # store the state
                    stateList.append(stateOption)

        for state in stateList:
            state.draw()

        print(len(stateList))

    def createGraph(self):
        return defaultdict(list)

    def addEdge(self, graph, u, v):
        graph[u].append(v)

    # BFS function to find path from source to sink
    def BFS(self, graph, start, finish):
        # Base case
        if start == finish:
            return True
             
        # Mark all the vertices as not visited
        visited = [False]*(len(graph) + 1)
        print("len",len(visited))
        
        # Create a queue for BFS
        queue = []
        queue.append(start)
 
        # Mark the current node as visited and
        # enqueue it
        visited[start] = True
        while(queue):
 
            # Dequeue a vertex from queue
            start = queue.pop(0)
 
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent has
            # not been visited, then mark it visited
            # and enqueue it
            for i in graph[start]:
                print(i)
                # If this adjacent node is the destination
                # node, then return true
                if i == finish:
                    return True

                # Else, continue to do BFS
                if visited[i] is False and i <= self.N:
                    queue.append(i)
                    visited[i] = True

        # If BFS is complete without visiting d
        return False

    def boundaryCheck(self, i, j, state):
        if i >= 0 and i <= len(state) and j >= 0 and j <= len(state[0]):
            return True
        else:
            return False

    # Returns true if there is a path from a source (a 
    # cell with value 1) to a destination (a cell with 
    # value 2)
    def checkForAWin(self, M, source, destination, playerType):
        s, d = None, None # source and destination 
        N = len(M)
        print(N)
        g = self.createGraph()
    
        # create graph with n * n node 
        # each cell consider as node 
        k = 1 # Number of current vertex
        for i in range(N):
            for j in range(N):
                if (M[i][j] != ' ' or M[i][j] != playerType):
    
                    # connect all 4 adjacent cell to 
                    # current cell 
                    if (self.boundaryCheck(i, j + 1, M)):
                        self.addEdge(g, k, k + 1)
                    if (self.boundaryCheck(i, j - 1, M)):
                        self.addEdge(g, k, k - 1)
                    if (self.boundaryCheck(i + 1, j, M)):
                        self.addEdge(g, k, k + N)
                    if (self.boundaryCheck(i - 1, j, M)):
                        self.addEdge(g, k, k - N)
                
                # if (M[i][j] == source):
                if ((i,j) == source):
                    s = k
    
                # destination index     
                if ((i,j) == destination):
                    d = k
                k += 1
        
        print(f"s is {s}")
        print(f"d is {d}")
    
        # find path Using BFS 
        return self.BFS(g, s, d)





















































    # def checkForAWin(self, playerType):

    #     # Defining visited array to keep
    #     # track of already visited indexes
    #     visited = [[False for x in range(self.N)]for y in range(self.N)]
        
    #     # Flag to indicate whether the
    #     # path exists or not
    #     flag = False
    
    #     for i in range(self.N):
    #         for j in range(self.N):
            
    #             # If state[i][j] is source
    #             # and it is not visited
    #             if (self.state[i][j] == 1 and not
    #                 visited[i][j]):
    
    #                 # Starting from i, j and
    #                 # then finding the path
    #                 if (self.checkPath(self.state, i, j, visited, playerType)):
                    
    #                     # If path exists
    #                     flag = True
    #                     break
    #     if (flag):
    #         print("YES")
    #     else:
    #         print("NO")
    #     pass

    # # Method for checking boundries
    # def isSafe(self, i, j, state):

    #     if (i >= 0 and i < len(state) and
    #         j >= 0 and j < len(state[0])):
    #         return True
    #     return False
    
    # # Returns true if there is a
    # # path from a source(a
    # # cell with value 1) to a
    # # destination(a cell with
    # # value 2)
    # def checkPath(self, state, i, j, visited, playerType):
    
    #     # Checking the boundries, walls and
    #     # whether the cell is unvisited
    #     if (self.isSafe(i, j, state) and
    #         state[i][j] != 0 and not
    #         visited[i][j]):
        
    #         # Make the cell visited
    #         visited[i][j] = True
    
    #         # If the cell is the required
    #         # destination then return true
    #         if (state[i][j] == 2):
    #             return True
    
    #         # traverse up
    #         up = self.checkPath(state, i - 1, j, visited)
    
    #         # If path is found in up
    #         # direction return true
    #         if (up):
    #             return True
    
    #         # Traverse left
    #         left = self.checkPath(state, i, j - 1, visited)
    
    #         # If path is found in left
    #         # direction return true
    #         if (left):
    #             return True

    #         # Traverse down
    #         down = self.checkPath(state, i + 1, j, visited)

    #         # If path is found in down
    #         # direction return true
    #         if (down):
    #             return True

    #         # Traverse right
    #         right = self.checkPath(state, i, j + 1, visited)

    #         # If path is found in right
    #         # direction return true
    #         if (right):
    #             return True

    #     # No path has been found
    #     return False
