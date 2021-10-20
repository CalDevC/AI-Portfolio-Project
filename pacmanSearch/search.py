# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    #Initialize state
    currentState = problem.getStartState()
    visitedNodes = []
    visitedNodes.append(currentState)
    bestPath = []

    #Initialize frontier
    frontier = util.Stack()
    nextMoves = problem.getSuccessors(currentState)
    for elem in nextMoves:
        pathList = []
        temp = list(elem)
        pathList.append(elem[1])
        temp.append(pathList)
        elem = tuple(temp)
        frontier.push(elem)

    while not frontier.isEmpty():
        #Pop nodes until we find one that hasn't been visited
        currentNode = frontier.pop()
        while currentNode[0] in visitedNodes:
            if frontier.isEmpty():
                return bestPath
            currentNode = frontier.pop()

        #Check for goal
        if problem.isGoalState(currentNode[0]):
                bestPath = currentNode[-1]
                return bestPath

        visitedNodes.append(currentNode[0]) #Add to visited nodes list

        #Get current node's children
        nextMoves = problem.getSuccessors(currentNode[0])

        # For each child node
        for nextMove in nextMoves:
            # Add path to child node
            parentPath = currentNode[-1].copy()
            parentPath.append(nextMove[1])
            temp = list(nextMove)
            temp.append(parentPath)
            nextMove = tuple(temp)

            # make sure we don't add a visited node to our frontier
            if nextMove[0] not in visitedNodes:
                frontier.push(nextMove)

    return bestPath


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    #Initialize state
    currentState = problem.getStartState()
    visitedNodes = []
    visitedNodes.append(currentState)
    bestPath = []

    #Initialize the frontier and add path list to each node
    frontier = util.Queue()
    nextMoves = problem.getSuccessors(currentState)
    for elem in nextMoves:
        pathList = []
        temp = list(elem)
        pathList.append(elem[1])
        temp.append(pathList)
        elem = tuple(temp)
        frontier.push(elem)

    # While the frontier still has nodes
    while not frontier.isEmpty():

        #Pop nodes until we find one that hasn't been visited
        currentNode = frontier.pop()
        while currentNode[0] in visitedNodes:
            if frontier.isEmpty():
                return bestPath
            currentNode = frontier.pop()

        #Check for goal
        if problem.isGoalState(currentNode[0]):
            bestPath = currentNode[-1]
            # print("BEST PATH: ")
            # print(bestPath)
            return bestPath
        
        visitedNodes.append(currentNode[0]) #Add to visited nodes list

        #Get current node's children
        nextMoves = problem.getSuccessors(currentNode[0])

        # For each child node
        for nextMove in nextMoves:
            # Add path to child node
            parentPath = currentNode[-1].copy()
            parentPath.append(nextMove[1])
            temp = list(nextMove)
            temp.append(parentPath)
            nextMove = tuple(temp)

            # make sure we don't add a visited node to our frontier
            if nextMove[0] not in visitedNodes:
                frontier.push(nextMove)

    return bestPath


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    #Initialize state
    currentState = problem.getStartState()
    visitedNodes = []
    visitedNodes.append(currentState)
    cheapest = -1
    goalFound = False
    bestPath = []

    # initialize the frontier and add path list to each node
    frontier = util.PriorityQueue()
    nextMoves = problem.getSuccessors(currentState)
    for elem in nextMoves:
        pathList = []
        temp = list(elem)
        pathList.append(elem[1])
        temp.append(pathList)
        elem = tuple(temp)
        cost = problem.getCostOfActions(elem[-1]) #Calculate cost
        frontier.push(elem, cost)

    # While the frontier still has nodes
    while not frontier.isEmpty():

        #Pop nodes until we find one that hasn't been visited
        currentNode = frontier.pop()
        while currentNode[0] in visitedNodes or (goalFound and cheapest < problem.getCostOfActions(currentNode[-1])):
            if frontier.isEmpty():
                return bestPath
            currentNode = frontier.pop()

        #Check for goal
        if problem.isGoalState(currentNode[0]):
            goalFound = True
            if cheapest == -1 or cheapest > problem.getCostOfActions(currentNode[-1]):
                cheapest = problem.getCostOfActions(currentNode[-1])
                bestPath = currentNode[-1]
                visitedNodes.append(currentNode[0])
                continue
    
        visitedNodes.append(currentNode[0]) #Add to visited nodes list

        #Get current node's children
        nextMoves = problem.getSuccessors(currentNode[0])

        # For each child node
        for nextMove in nextMoves:
            # Add path to child node
            parentPath = currentNode[-1].copy()
            parentPath.append(nextMove[1])
            temp = list(nextMove)
            temp.append(parentPath)
            nextMove = tuple(temp)

            # make sure we don't add a visited node to our frontier
            if nextMove[0] not in visitedNodes:
                cost = problem.getCostOfActions(nextMove[-1])
                frontier.update(nextMove, cost)

    return bestPath


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    # Initialize state
    currentState = problem.getStartState()
    visitedNodes = []
    visitedNodes.append(currentState)
    cheapest = -1
    goalFound = False
    bestPath = []

    # Initialize the frontier and add path list to each node
    frontier = util.PriorityQueue()
    nextMoves = problem.getSuccessors(currentState)
    for elem in nextMoves:
        pathList = []
        temp = list(elem)
        pathList.append(elem[1])
        temp.append(pathList)
        elem = tuple(temp)
        cost = problem.getCostOfActions(elem[-1]) + heuristic(elem[0], problem) #Calculate cost + heuristic
        frontier.push(elem, cost)

    # While the frontier still has nodes
    while not frontier.isEmpty():

        #Pop nodes until we find one that hasn't been visited
        currentNode = frontier.pop()
        while currentNode[0] in visitedNodes or (goalFound and cheapest < (problem.getCostOfActions(currentNode[-1]) + heuristic(currentNode[0], problem))):
            if frontier.isEmpty():
                return bestPath
            currentNode = frontier.pop()

        #Check if goal
        if problem.isGoalState(currentNode[0]):
            goalFound = True
            if cheapest == -1 or cheapest > (problem.getCostOfActions(currentNode[-1]) + heuristic(currentNode[0], problem)):
                cheapest = problem.getCostOfActions(currentNode[-1]) + heuristic(currentNode[0], problem)
                bestPath = currentNode[-1]
                visitedNodes.append(currentNode[0])
                continue

        visitedNodes.append(currentNode[0])  # Add to visited nodes list

        # Get current node's children
        nextMoves = problem.getSuccessors(currentNode[0])

        # For each child node
        for nextMove in nextMoves:
            # Add path to child node
            parentPath = currentNode[-1].copy()
            parentPath.append(nextMove[1])
            temp = list(nextMove)
            temp.append(parentPath)
            nextMove = tuple(temp)

            # make sure we don't add a visited node to our frontier
            if nextMove[0] not in visitedNodes:
                cost = problem.getCostOfActions(nextMove[-1]) + heuristic(nextMove[0], problem)
                frontier.update(nextMove, cost)

    return bestPath  # If frontier is empty return empty path


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
