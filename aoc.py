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
  f = open("input/day" + str(dayNum) + ".txt")
  x = f.read().splitlines()
  f.close()
  if rtnType == "i":
   return [int(val) for val in x]
  else:
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

def manhattan(a, b):
  return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def printBoard(mem):
  for line in mem:
    print(''.join([str(i) for i in line]))
  print('============')
  return

def memoize(func):
  cache = dict()

  def memoized_func(*args):
      if args in cache:
          return cache[args]
      result = func(*args)
      cache[args] = result
      return result

  return memoized_func