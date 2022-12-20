from aoc import *
import time
from copy import deepcopy

class DayTwenty:

  mem = []

  def __init__(self, mem):
    self.mem = mem.copy()

  def partOne(self):
    moves = deepcopy(self.mem)
    idxList = list((i, j) for i, j in enumerate(self.mem))
    for move in moves:
      if move == '0': zeroLoc = (moves.index(move), move)
      moveLoc = idxList.index((moves.index(move), move))
      del idxList[moveLoc]
      if int(move) < 0: moveLoc -= 1
      if moves.index(move) == len(idxList): moveLoc += 1
      idxList.insert((moveLoc + int(move)) % (len(idxList) + 1), (moves.index(move), move))
    return (int(idxList[(idxList.index(zeroLoc) + 1000) % len(idxList)][1]) + \
            int(idxList[(idxList.index(zeroLoc) + 3000) % len(idxList)][1]) + \
            int(idxList[(idxList.index(zeroLoc) + 2000) % len(idxList)][1]))
          

  def partTwo(self):
    pass

if __name__ == "__main__":
  y = fileOpenLines(20)
  dayTwenty = DayTwenty(y)
  startTime = time.time()
  print("Part 1: ", dayTwenty.partOne(), " in ", round(time.time() - startTime, 2), "s")
  startTime = time.time()
  print("Part 2: ", dayTwenty.partTwo(), " in ", round(time.time() - startTime, 2), "s")