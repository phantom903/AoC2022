from aoc import *

class DayThree:
  mem = []

  def __init__(self, mem):
    self.mem = mem.copy()

  def partOne(self):
    total = 0
    for line in self.mem:
      grp1, grp2 = line.split(',')
      grp1 = [int(i) for i in grp1.split('-')]
      grp2 = [int(i) for i in grp2.split('-')]
      #full1 = [i for i in range(int(grp1[0]), int(grp1[1]))]
      #full2 = [i for i in range(int(grp2[0]), int(grp2[1]))]
      #if set(full1).issubset(set(full2)) or set(full2).issubset(set(full1)) and set(full1) != set(full2):
      if (grp1[0] <= grp2[0] and grp2[1] <= grp1[1]) or (grp2[0] <= grp1[0] and grp1[1] <= grp2[1]):
        total += 1
    return total

  def partTwo(self):
    total = 0
    for line in self.mem:
      grp1, grp2 = line.split(',')
      grp1 = [int(i) for i in grp1.split('-')]
      grp2 = [int(i) for i in grp2.split('-')]
      #if (grp1[0] <= grp2[1] and grp1[1] > grp2[0]) or (grp2[0] <= grp1[1] and grp2[1] > grp1[0]):
      if len(set(range(grp1[0], grp1[1]+1)).intersection(set(range(grp2[0], grp2[1]+1)))) > 0:     
        total += 1
    return total

if __name__ == "__main__":
  y = fileOpenLines(4)
  dayThree = DayThree(y)
  print('Day Three part one : ', dayThree.partOne())
  print('Day Three part two : ', dayThree.partTwo())