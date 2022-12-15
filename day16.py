from aoc import *
import time

class DaySixteen:

  mem = []

  def __init__(self, mem):
    self.mem = mem.copy()

  def partOne(self):
    pass

  def partTwo(self):
    pass

if __name__ == "__main__":
  y = fileOpenLines(16)
  daySixteen = DaySixteen(y)
  startTime = time.time()
  print("Part 1: ", daySixteen.partOne(), " in ", round(time.time() - startTime, 2), "s")
  startTime = time.time()
  print("Part 2: ", daySixteen.partTwo(), " in ", round(time.time() - startTime, 2), "s")