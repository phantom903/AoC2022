import re

## 
## Remove all duplicate items from list x
##
def stripDups(x):
  return list(dict.fromkeys(x))

##
## Take a list of strings x, return a list of all 
## duplicate chars between those strings
##
def showDups(x):
  return list(set(x[0]).intersection(*x))

##
## Convert text representation of a binary string
## where binChars is a list []  of chars representing 1
##
def binaryPass(binChars, data):
  return int("".join(["1" if i in binChars else "0" for i in data]), 2)


##
## Read input file for Day dayNum and split input into
## a list of lines - converted to ints if rtnType "i"
##
def fileOpenLines(dayNum, rtnType="s"):
  if rtnType == "t":
    f = open("input/day" + str(dayNum) + "test.txt")
  else:
    f = open("input/day" + str(dayNum) + ".txt")
  x = f.read().splitlines()
  f.close()
  if rtnType == "i":
   return [int(val) for val in x]
  else:
    return x

##
## Read input file for Day dayNum and return a string
## of the entire file
##
def fileOpenRaw(dayNum):
  f = open("input/day" + str(dayNum) + ".txt")
  x = f.read()
  f.close()
  return x

##
## Bubble sort a list depending on compare function
## which must return True if left is less than right
## if no compare function is passed, use generic compare
##
def bubblesort(toSort, compareFn=lambda left, right: left < right):
  for i in range(len(toSort)):
    for j in range(len(toSort) - 1):
      if compareFn(toSort[j+ 1], toSort[j]):
        temp = toSort[j]
        toSort[j] = toSort[j + 1]
        toSort[j + 1] = temp
  return toSort

##
## Read input file for Day dayNum and split input into
## a list of lists of ints
##
def fileOpenIntGrid(dayNum):
  f = open("input/day" + str(dayNum) + ".txt")
  x = f.read().splitlines()
  f.close()
  for i in range(len(x)):
    x[i] = [int(val) for val in x[i]]
  return x
  
##
## Return a list of ints in a string, other chars
## are ignored
##
def ints(mixedStr):
  strippedInts = re.findall(r'\d+', mixedStr)
  strippedInts = [int(val) for val in strippedInts]
  return strippedInts

##
## Read input file for Day dayNum, return a list of entries
## separated by empty lines in input file
##
def fileOpenNewLines(dayNum):
  f = open("input/day" + str(dayNum) + ".txt")
  x = f.read().splitlines()
  f.close()
  entry = ""
  entries = []
  for line in x:
    if not line in (None, '', '\n\n'):
      entry += (line + " ")
    else:
      entries.append(entry.strip())
      entry = ""
  entries.append(entry.strip())
  return entries

##
## Returns all neighbours of current location in mem
## looking diagonally if diag is True
##
def neighbours(current, mem, diag=False):
  res = []
  if diag:
    checks = 8
  else:
    checks = 4
  locX = [1, 0, -1, 0, -1, 1, -1, 1]
  locY = [0, 1, 0, -1, 1, -1, -1, 1]
  lowPoint = True
  for i in range(checks):
    row, col = current[0] + locX[i], current[1] + locY[i]
    if row >= 0 and row < len(mem[0]) and col >= 0 and col < len(mem):
      res.append((row,col))
  return res

##
## Returns the manhattan distance between two points
##
def manhattan(a, b):
  return sum(abs(val1-val2) for val1, val2 in zip(a,b))

##
## Returns true if a and b are diagonal to each other
##
def isDiagonal(a, b):
  return (a[0] != b[0]) and (a[1] != b[1]) and (manhattan(a, b) % 2 == 0)

##
## Returns a list of all adjacent locations to loc
##
def adjacents(loc):
  return [
    (loc[0]+1, loc[1]), (loc[0]-1, loc[1]), (loc[0], loc[1]+1), (loc[0], loc[1]-1),
    (loc[0]+1, loc[1]+1), (loc[0]-1, loc[1]-1), (loc[0]+1, loc[1]-1), (loc[0]-1, loc[1]+1)
  ]

##
## Performs a move in the direction specified
## and returns the new location
##
def doMove(loc, direction):
  if direction == 'N':
    return (loc[0], loc[1]-1)
  elif direction == 'S':
    return (loc[0], loc[1]+1)
  elif direction == 'E':
    return (loc[0]+1, loc[1])
  elif direction == 'W':
    return (loc[0]-1, loc[1])
  elif direction == 'D':
    return (loc[0], loc[1]+1)
  elif direction == 'U':
    return (loc[0], loc[1]-1)
  elif direction == 'R':
    return (loc[0]+1, loc[1])
  elif direction == 'L':
    return (loc[0]-1, loc[1])

##
## Returns true if a and b are adjacent
##
def isAdjacent(a, b):
  return b in adjacents(a)

##
## Prints a 2D array
##
def printBoard(mem):
  for line in mem:
    print(''.join([str(i) for i in line]))
  print('============')
  return

##
## Returns a cached version of a function
##
def memoize(func):
  cache = dict()

  def memoized_func(*args):
      if args in cache:
          return cache[args]
      result = func(*args)
      cache[args] = result
      return result

  return memoized_func

##
## Returns an (x, y) tuple of fromLoc moved towards tgtLoc
## according to the rules of AoC 2022 Day 9
##
def moveTowards(tgtLoc, fromLoc):
  x,y = fromLoc[0], fromLoc[1]
  dx = tgtLoc[0] - fromLoc[0]
  dy = tgtLoc[1] - fromLoc[1]
  if abs(dx) == 2 and not dy:
    x += 1 if dx > 0 else -1
  elif abs(dy) == 2 and not dx:
    y += 1 if dy > 0 else -1
  elif (abs(dy) == 2 and abs(dx) in (1,2)) or (abs(dx) == 2 and abs(dy) in (1,2)):
    x += 1 if dx > 0 else -1
    y += 1 if dy > 0 else -1
  return (x,y)