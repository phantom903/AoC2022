from aoc import *

TESTDATA = [
  'R 4',
  'U 4',
  'L 3',
  'D 1',
  'R 4',
  'D 1',
  'L 5',
  'R 2'
]

class DayNine:

  mem = []

  def __init__(self, mem):
    for line in mem:
    # for line in TESTDATA:
      x, y = line.split(' ')
      self.mem.append([x, int(y)])
    
  def partOne(self):
    hLoc = (0, 0)
    tLoc = (0, 0)
    oldLoc = (0, 0)
    tLocs = [(0,0)]
    for i in range(len(self.mem)):
      for _ in range(self.mem[i][1]):
        oldLoc = hLoc
        hLoc = doMove(hLoc, self.mem[i][0])
        if manhattan(tLoc, hLoc) >= 2 and not isAdjacent(tLoc, hLoc):
          tLoc = oldLoc
          tLocs.append(tLoc)
    return len(set(tLocs))

  def partTwo(self):
    knots = [(0,0) for _ in range(10)]
    oldknots = [(0,0) for _ in range(10)]
    tLocs = [(0,0)]
    for i in range(len(self.mem)):
      for _ in range(self.mem[i][1]):
        oldknots[0] = knots[0]
        knots[0] = doMove(knots[0], self.mem[i][0])
        for j in range(0, 10):
          if manhattan(knots[j-1], knots[j]) >= 2 and not isAdjacent(knots[j-1], knots[j]):
            knots[j] = oldknots[j-1]
        tLocs.append(knots[9])
          
    return len(set(tLocs))

if __name__ == "__main__":
  y = fileOpenLines(9)
  dayNine = DayNine(y)
  print('Day Nine part one : ', dayNine.partOne())
  print('Day Nine part two : ', dayNine.partTwo())