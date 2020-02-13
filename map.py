import random as r
from searches import bfs
from searches import dfs
from searches import bi_bfs
from searches import astar
import time


def main(): 
  inputDim = input("Enter dimension of map: ")
  inputP = input("Enter probability 0<p<1: ")
  map=generateMap(int(inputDim),float(inputP))
  printMap(map)
  search = input("Choose search option: dfs, bfs, a*, bi-bfs \n")
  if (search == "dfs"):
    dfs(map)
  elif (search == "bfs"):
    bfs(map)
  elif (search == "a*" or search == "a" ):
    
    # Setting up map
    map[0][0]=0
    map[len(map)-1][len(map)-1] = 0

    flag = input("Enter number: (0) Manhattan (1) Euclidean \n")
    # 1 for Euclidean
    # 0 for Manhattan
    start_time = time.time()
    path = astar(map,int(flag))
    if path is None:
      print("path does not exist")
    else:
      print(path)
    print("--- %s seconds ---" % (time.time() - start_time)) 
    
  elif (search == "bi-bfs"):
    bi_bfs(map)
  '''
  else:
    print("DFS:")
    dfs(map)
    print("BFS:")
    bfs(map)
    print("BI-BFS:")
    bi_bfs(map)
  '''



def printMap(a):
  print("map:")
  print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in a]))
  print()

def generateMap(dim,p):
  map = [[0 for x in range(dim)] for y in range(dim)]
  v = [0,1]
  weights = [1-p,p]
  for row in range(len(map)):
    for col in range(len(map)):
      value = r.choices(v,weights)
      map[row][col] = value[0]
  map[0][0] = "S"
  map[dim-1][dim-1] = "G"
  return map


def calculateSolvability():
 
  i = 10
  i2 = i
  solvable = 0
  unsolvable = 0
  while (i > 0):
    map = None
    map = generateMap(int(10),0.9)
    printMap(map)
    map[0][0] = 0
    map[9][9] = 0
    path = astar(map,int(1))
    print(path)
    if path is None:
     unsolvable = unsolvable + 1
    else:
      solvable = solvable + 1
    i=i-1

  print("Generated: "+ str(i2) +" and # Solvable: " + str(solvable))
  print("Success Percent: "+ str((solvable/i2)*100))


main()
