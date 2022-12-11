from aoc import *

TESTDATA = [
  'R 5',
  'U 8',
  'L 8',
  'D 3',
  'R 17',
  'D 10',
  'L 25',
  'U 20'
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
    tLocs = [(0,0)]
    for i in range(len(self.mem)):
      for _ in range(self.mem[i][1]):
        knots[0] = doMove(knots[0], self.mem[i][0])
        for j in range(1, 10):
          if not isAdjacent(knots[j], knots[j-1]):
            knots[j] = moveTowards(knots[j-1], knots[j])          
        tLocs.append(knots[9])
    return len(set(tLocs))

if __name__ == "__main__":
  y = fileOpenLines(9)
  dayNine = DayNine(y)
  print('Day Nine part one : ', dayNine.partOne())
  print('Day Nine part two : ', dayNine.partTwo())