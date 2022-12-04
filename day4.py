from aoc import *

class DayThree:
  mem = []

  def __init__(self, mem):
    self.mem = mem.copy()

  def partOne(self):
    total = 0
    for line in self.mem:
      print(line)
      grp1, grp2 = line.split(',')
      grp1 = grp1.split('-')
      grp2 = grp2.split('-')
      full1 = [i for i in range(int(grp1[0]), int(grp1[1]))]
      full2 = [i for i in range(int(grp2[0]), int(grp2[1]))]
      if full1 in full2 or full2 in full1:
        total += 1
    return total

  def partTwo(self):
    total = 0
    return total

if __name__ == "__main__":
  y = fileOpenLines(4)
  dayThree = DayThree(y)
  print('Day Three part one : ', dayThree.partOne())
  print('Day Three part two : ', dayThree.partTwo())