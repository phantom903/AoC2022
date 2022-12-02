from aoc import *

class DayOne:

  mem = []

  def __init__(self, mem):
    self.mem = mem.copy()
    self.tots = []

  def partOne(self):
    tot = 0
    tots = []
    for i in range(len(self.mem)):
      if self.mem[i] != '':
        tot += int(self.mem[i])
      else:
        tots.append(tot)
        tot = 0
    self.tots = tots.copy()
    return max(tots)
  
  def partTwo(self):
    self.tots.sort()
    return sum(self.tots[-3:])

if __name__ == "__main__":
  y = fileOpenLines(1)
  dayOne = DayOne(y)
  print('Day One part one : ', dayOne.partOne())
  print('Day One part two : ', dayOne.partTwo())