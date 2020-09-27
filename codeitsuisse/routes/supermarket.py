import logging
import json
import random
import operator as op
from functools import reduce


from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/supermarket', methods=['POST'])
def evaluateSuper():
    data = request.get_json();
    result={}
    logging.info("data sent for evaluation {}".format(data))
    i =  0
    for case in data["tests"]:
        maze = data["tests"][case]["maze"]
        start = data["tests"][case]["start"]
        end = data["tests"][case]["end"]
        st=solveMaze(maze,start,end)
        result[case]= st
        i = i + 1
    fr = { "answers": result }
    logging.info("My result :{}".format(fr))
    return json.dumps(fr);

  

  
# A utility function to check if x, y is valid 
# index for N * N Maze 
def isSafe( maze, x, y, row, col ): 
      
    if x >= 0 and x < row and y >= 0 and y < col and maze[x][y] == 1: 
        return True
      
    return False
  
def stepsdfg(maze,row,col):
    logging.info("My result :{}".format(maze))
    ans = 0
    for i in range(0,row):
        for j in range(0,col):
            if maze[i][j]==1:
                ans = ans + 1
    return ans

def solveMaze(maze,start,end ): 
      
    row = len(maze)
    col = len(maze[0])
    sol = [ [ 0 for j in range(col) ] for i in range(row) ] 
    for i in range(0,row):
        for j in range(0,col):
            maze[i][j] = 1 - maze[i][j]
    logging.info("maze:{}".format(maze))
    steps = 0
    if solveMazeUtil(maze, start[1],start[0], end,row,col, sol) == False: 
        logging.info("Solution doesn't exist"); 
        return -1
      
    return stepsdfg(sol,row,col)
      
# A recursive utility function to solve Maze problem 
def solveMazeUtil(maze, x,y,end,row,col,sol): 
    logging.info("x:{}".format(x))
    logging.info("y :{}".format(y))
    # if (x, y is goal) return True 
    if x == end[1] and y == end[0] and maze[x][y]== 1: 
        sol[x][y] = 1
        return True
          
    # Check if maze[x][y] is valid 
    if isSafe(maze, x, y,row,col) == True: 
        if sol[x][y] == 1:
            return False
        # mark x, y as part of solution path 
        sol[x][y] = 1

        hor = end[1]-x
        ver = end[0]-y
        if hor > 0:
            # Move forward in x direction 
            if solveMazeUtil(maze, x + 1, y,end,row,col,sol) == True: 
                return True
        else: 
            if solveMazeUtil(maze, x - 1, y,end,row,col,sol) == True: 
                return True    
        # If moving in x direction doesn't give solution  
        # then Move down in y direction 
        if ver > 0:
            if solveMazeUtil(maze, x, y + 1,end,row,col, sol) == True: 
                return True
        else:
            if solveMazeUtil(maze, x, y - 1,end,row,col, sol) == True: 
                return True
        if hor > 0:
            # Move forward in x direction 
            if solveMazeUtil(maze, x - 1, y,end,row,col,sol) == True: 
                return True
        else: 
            if solveMazeUtil(maze, x + 1, y,end,row,col,sol) == True: 
                return True   
        if ver > 0:
            if solveMazeUtil(maze, x, y - 1,end,row,col, sol) == True: 
                return True
        else:
            if solveMazeUtil(maze, x, y + 1,end,row,col, sol) == True: 
                return True
        # If none of the above movements work then  
        # BACKTRACK: unmark x, y as part of solution path 
        sol[x][y] = 0
        return False
  
