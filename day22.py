from aoc import *
import time
from enum import Enum

def tokenise(line):
  num = ""
  dir = ''
  directions = []
  for i in range(len(line)):
    if line[i].isnumeric():
      if dir != '': directions.append(dir)
      dir = ''
      num += line[i]
    else:
      if num != '': directions.append(int(num))
      num = ''
      dir += line[i]
  return directions

class DayTwentyTwo:

  mem = []

  def __init__(self, mem):
    self.directions = tokenise(mem.pop(-1))
    mem.pop(-1)
    self.map = mem.copy()

  def partOne(self):
    dir = ['R', 'D', 'L', 'U']
    facing = dir.index('R')
    pos = (self.map[0].find('.'), 0)
    for i in self.directions:
      if type(i) == int:
        print(i)
        for _ in range(i):
          nextPos = doMove(pos, dir[facing])
          print(pos, nextPos)
          xBound = min(len(self.map[nextPos[1]]), ((len(self.map[nextPos[1]]) - len(self.map[nextPos[1]].rstrip()) - 1)))
          yBound = len(self.map)
          if nextPos[0] >= xBound:
            nextPos = (len(self.map[nextPos[1]]) - len(self.map[nextPos[1]].lstrip()), nextPos[1])
          elif nextPos[0] < 0:
            nextPos = (len(self.map[nextPos[1]]) - len(self.map[nextPos[1]].rstrip()) - 1, nextPos[1])
          while nextPos[1] >= yBound or (self.map[nextPos[1]][nextPos[0]] == ' ' and dir[facing] == 'D'):
            nextPos = doMove((nextPos[0], yBound - 1), dir[facing])
          while nextPos[1] < 0 or (self.map[nextPos[1]][nextPos[0]] == ' ' and dir[facing] == 'U'):
            nextPos = doMove((nextPos[0], 0), dir[facing])
          if self.map[nextPos[1]][nextPos[0]] != '#':
            pos = nextPos
          print(pos[0], pos[1], facing)
      else:
        facing = (dir.index(dir[dir.index(i) + 1]) % 4)
      
    return ((1000 * (pos[0] - 1) + (4 * (pos[1] - 1))) + facing)
    

  def partTwo(self):
    pass

if __name__ == "__main__":
  y = fileOpenLines(22, 't')
  dayTwentyTwo = DayTwentyTwo(y)
  startTime = time.time()
  print("Part 1: ", dayTwentyTwo.partOne(), " in ", round(time.time() - startTime, 2), "s")
  startTime = time.time()
  print("Part 2: ", dayTwentyTwo.partTwo(), " in ", round(time.time() - startTime, 2), "s")