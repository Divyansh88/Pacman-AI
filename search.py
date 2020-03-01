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
from util import Queue
from util import Stack
from util import PriorityQueue


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
    return [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    "Open list contains all nodes which are going to be visited and closed list contains all visited nodes. " \
    "First we push starting position and empty list(path to that node) in Stack(open_list) then we check if it is starting is goal then return nothing." \
    "Until open list is empty pop element (LIFO) so it will go to depth. If that element is goal then return path." \
    "If that element is not in closed list add it to closed list then get all children of that node by getSuccessors." \
    "Check for all children if it is already in closed list or not if not then add path to that node by adding parents path + node's path." \
    "Then push it to the stack and check again."
    open_list = Stack()
    open_list.push((problem.getStartState(), []))
    closed_list = set()

    if problem.isGoalState(problem.getStartState()):
        return []

    while not open_list.isEmpty():
        x = open_list.pop()
        if problem.isGoalState(x[0]):
            return x[1]
        if x[0] not in closed_list:
            closed_list.add(x[0])
            children = problem.getSuccessors(x[0])
            for child in children:
                if child[0] not in closed_list:
                    new_path = x[1] + [child[1]]
                    open_list.push((child[0], new_path))

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    "Open list contains all nodes which are going to be visited and closed list contains all visited nodes. " \
    "First we push starting position and empty list(path to that node) in Stack(open_list) then we check if it is starting is goal then return nothing." \
    "Until open list is empty pop element (FIFO) so it will go to level. If that element is goal then return path." \
    "If that element is not in closed list add it to closed list then get all children of that node by getSuccessors." \
    "Check for each child if it is already in closed list or not if not then add path to that node by adding parents path + node's path." \
    "Then push it to the queue and check again."
    open_list = Queue()
    open_list.push((problem.getStartState(), []))
    closed_list = set()

    if problem.isGoalState(problem.getStartState()):
        return []

    while not open_list.isEmpty():
        x = open_list.pop()
        if problem.isGoalState(x[0]):
            return x[1]
        if x[0] not in closed_list:
            closed_list.add(x[0])
            children = problem.getSuccessors(x[0])
            for child in children:
                if child[0] not in closed_list:
                    new_path = x[1] + [child[1]]
                    open_list.push((child[0], new_path))
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    "Open list contains all nodes which are going to be visited and closed list contains all visited nodes. " \
    "First we push starting position and empty list(path to that node) in Stack(open_list) then we check if it is starting is goal then return nothing." \
    "Until open list is empty pop element (cost) so it will go by priority. If that element is goal then return path." \
    "If that element is not in closed list add it to closed list then get all children of that node by getSuccessors." \
    "Check for all children if it is already in closed list or not if not then add path to that node by adding parents path + node's path." \
    "Also add cost to that node by adding parents cost + node's cost." \
    "Then push it to the priority queue and check again."
    open_list = PriorityQueue()
    open_list.push((problem.getStartState(), [], 0), 0)
    closed_list = set()

    if problem.isGoalState(problem.getStartState()):
        return []

    while not open_list.isEmpty():
        x = open_list.pop()
        if problem.isGoalState(x[0]):
            return x[1]
        if x[0] not in closed_list:
            closed_list.add(x[0])
            children = problem.getSuccessors(x[0])
            for child in children:
                if child[0] not in closed_list:
                    new_path = x[1] + [child[1]]
                    new_cost = x[2] + child[2]
                    open_list.push((child[0], new_path, new_cost), new_cost)
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    "Open list contains all nodes which are going to be visited and closed list contains all visited nodes. " \
    "First we push starting position and empty list(path to that node) in Stack(open_list) then we check if it is starting is goal then return nothing." \
    "Until open list is empty pop element (lowest combined cost) so it will go by priority. If that element is goal then return path." \
    "If that element is not in closed list add it to closed list then get all children of that node by getSuccessors." \
    "Check for all children if it is already in closed list or not if not then add path to that node by adding parents path + node's path." \
    "Also add cost to that node by adding parents cost + node's cost." \
    "Also add combined cost by adding actual cost + heuristic." \
    "Then push it to the priority queue and check again."
    open_list = PriorityQueue()
    open_list.push((problem.getStartState(), [], 0), 0)
    closed_list = set()

    if problem.isGoalState(problem.getStartState()):
        return []

    while not open_list.isEmpty():
        x = open_list.pop()
        if problem.isGoalState(x[0]):
            return x[1]
        if x[0] not in closed_list:
            closed_list.add(x[0])
            children = problem.getSuccessors(x[0])
            for child in children:
                if child[0] not in closed_list:
                    new_path = x[1] + [child[1]]
                    actual_cost = x[2] + child[2]
                    combined_cost = actual_cost + heuristic(child[0], problem)
                    open_list.push((child[0], new_path, actual_cost), combined_cost)
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
