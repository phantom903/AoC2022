from aoc import *

class DayThree:

  mem = []

  def __init__(self, mem):
    self.mem = mem.copy()

  def partOne(self):
    pass

  def partTwo(self):
    pass

if __name__ == "__main__":
  y = fileOpenLines(3)
  dayThree = DayThree(y)
  print('Day Three part one : ', dayThree.partOne())
  print('Day Three part two : ', dayThree.partTwo())