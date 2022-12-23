from aoc import *
import time
from copy import deepcopy

class DayTwenty:

  mem = []

  def __init__(self, mem):
    self.mem = mem.copy()

  def partOne(self):
    print(self.mem)
         
  def partTwo(self):
    pass

if __name__ == "__main__":
  y = fileOpenLines(20, 't')
  dayTwenty = DayTwenty(y)
  startTime = time.time()
  print("Part 1: ", dayTwenty.partOne(), " in ", round(time.time() - startTime, 2), "s")
  startTime = time.time()
  print("Part 2: ", dayTwenty.partTwo(), " in ", round(time.time() - startTime, 2), "s")