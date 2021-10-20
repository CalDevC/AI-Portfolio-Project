# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent


class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)  # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """

        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        rows = newFood.width
        cols = newFood.height
        score = 0

        #Create a list with the positions of every ghost
        ghostList = []
        for ghostPos in newGhostStates:
            # Get ghost coords
            trimmedStr = str(ghostPos)[14:].split(',')
            x = float(trimmedStr[0])
            y = float(trimmedStr[1][1:].strip(')'))
            ghostList.append((x, y))

        #Search each grid square
        for i in range(0, rows):
            for j in range(0, cols):
                # Higher score for coords with food
                if newFood[i][j]:
                    score += 3.0 / (2.0 * manhattanDistance(newPos, (i, j)))
                # Higher score for going towards a scared ghost
                if newScaredTimes[0] > 0:
                    for ghost in ghostList:
                        score += 1.5 / manhattanDistance(newPos, ghost)
                else:  # Lower score for coords near a ghost
                    for ghost in ghostList:
                        if newPos != ghost:
                            score -= .1 / manhattanDistance(newPos, ghost)

        return successorGameState.getScore() + score


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        # Agent Indices
        pacman = 0
        finalAgent = gameState.getNumAgents() - 1

        # Constants
        INFINITY = float('inf')
        NEGATIVE_INFINITY = float('-inf')
        LOWEST_DEPTH = self.depth

        #Function checks if we are at a terminal state
        def isTerminal(state, depth):
            if depth == LOWEST_DEPTH or state.isWin() or state.isLose():
                return True
            return False

        def maxValue(state, currentDepth):
            # Increment our depth - Pacman's move starts a new ply
            currentDepth += 1

            # initialize v = -∞
            value = NEGATIVE_INFINITY

            # Check if we reach terminal state
            if isTerminal(state, currentDepth):
                return self.evaluationFunction(state)

            # for each successor of state
            for action in state.getLegalActions(pacman):
                successorState = state.generateSuccessor(pacman, action)

                # v = max(v, minValue(successor))
                value = max(value, minValue(successorState, currentDepth, 1))

            # return v
            return value

        def minValue(state, currentDepth, ghostNum):
            # initialize v = +∞
            value = INFINITY

            # Check if we reach terminal state
            if isTerminal(state, currentDepth):
                return self.evaluationFunction(state)

            # for each successor of state:
            for action in state.getLegalActions(ghostNum):
                successorState = state.generateSuccessor(ghostNum, action)

                if ghostNum != finalAgent:
                    # if the next agent is MIN: return min-value(state)
                    value = min(value, minValue(successorState, currentDepth, ghostNum + 1))
                elif ghostNum == finalAgent:
                    # if the next agent is MAX: return max-value(state)
                    value = min(value, maxValue(successorState, currentDepth))

            # return v
            return value

        # The best score achieved by Pacman and the action used to achieve it
        bestScore = None
        bestAction = None

        # For each of Pacman's possible actions
        for action in gameState.getLegalActions(pacman):
            # Get game state produced by the action
            newGameState = gameState.generateSuccessor(pacman, action)
            # Start recursion cycle off using:
            # game state produced by Pacman's action, starting depth, and first ghost
            actionScore = minValue(newGameState, 0, 1)

            #Update best score
            if not bestScore or actionScore > bestScore:
                bestScore = actionScore
                bestAction = action

        #Return action that produced best score
        return bestAction


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        # Agent Indices
        pacman = 0
        finalAgent = gameState.getNumAgents() - 1

        # Constants
        NEGATIVE_INFINITY = float('-inf')
        LOWEST_DEPTH = self.depth

        #Function checks if state is terminal
        def isTerminal(state, depth):
            if depth == LOWEST_DEPTH or state.isWin() or state.isLose():
                return True
            return False

        def maxValue(state, currentDepth):
            # Increment our depth - Pacman's move starts a new ply
            currentDepth += 1

            # initialize v = -∞
            value = NEGATIVE_INFINITY

            # Check if we reach terminal state
            if isTerminal(state, currentDepth):
                return self.evaluationFunction(state)

            # for each successor of state
            for action in state.getLegalActions(pacman):
                successorState = state.generateSuccessor(pacman, action)

                # v = max(v, expValue(successor))
                value = max(value, expValue(successorState, currentDepth, 1))

            # return v
            return value

        def expValue(state, currentDepth, ghostNum):
            # initialize v = 0
            value = 0
            valueSum = 0

            # Check if we reach terminal state
            if isTerminal(state, currentDepth):
                return self.evaluationFunction(state)

            # for each successor of state:
            for action in state.getLegalActions(ghostNum):
                successorState = state.generateSuccessor(ghostNum, action)

                # Calc probability
                prob = 1 / len(state.getLegalActions(ghostNum))

                if ghostNum != finalAgent:
                    # if the next agent is CHANCE: return exp-value(state)
                    value = prob * expValue(successorState, currentDepth, ghostNum + 1)
                elif ghostNum == finalAgent:
                    # if the next agent is MAX: return max-value(state)
                    value = maxValue(successorState, currentDepth)
                valueSum += value
            return valueSum

        # The best score achieved by Pacman and the action used to achieve it
        bestScore = None
        bestAction = None

        # For each of Pacman's possible actions
        for action in gameState.getLegalActions(pacman):
            # Get game state produced by the action
            newGameState = gameState.generateSuccessor(pacman, action)
            # Start recursion cycle off using:
            # game state produced by Pacman's action, starting depth, and first ghost
            actionScore = expValue(newGameState, 0, 1)

            #Update best score
            if not bestScore or actionScore > bestScore:
                bestScore = actionScore
                bestAction = action

        #Return action that produced best score
        return bestAction


def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION:
        First we took the manhattan distance to every piece of food and added (1 / the closest distance) to the score.
        Next we found the ghost positions and subtracted the manhattan distance to each ghost from the score.
        Then we subtracted the number of remaining pieces of food from the score.
        Finally we added half of the game state's score to our score.

        The coefficients we used and numbers we divided with were some what arbitrary and we just changed them around
        to see what gave us better results.
    """

    #Initialize variables
    score = 0
    position = currentGameState.getPacmanPosition()
    foodGrid = currentGameState.getFood().asList()
    closest = -1

    #Find the closest piece of food
    for foodPos in foodGrid:
        dist = manhattanDistance(position, foodPos)
        if dist < closest or closest == -1:
            closest = dist

    #Add inverse of closest distance to score
    score += 1/closest

    #Create a list of ghost positions
    newGhostStates = currentGameState.getGhostStates()
    ghostList = []
    for ghostPos in newGhostStates:
        # Get ghost coords
        trimmedStr = str(ghostPos)[14:].split(',')
        x = float(trimmedStr[0])
        y = float(trimmedStr[1][1:].strip(')'))
        ghostList.append((x, y))

    #For every ghost subtract it's manhattan distance (to pacman) from the score
    for ghost in ghostList:
        if position != ghost:
            score -= manhattanDistance(position, ghost)

    #Subtract the number of remaining pieces of food from the score
    score - currentGameState.getNumFood()
    #Add half of the gamestate's  score
    score += 0.5 * currentGameState.getScore()

    return score

# Abbreviation
better = betterEvaluationFunction
