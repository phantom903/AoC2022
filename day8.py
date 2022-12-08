from aoc import *

TESTDATA = [
  [3,0,3,7,3],
  [2,5,5,1,2],
  [6,5,3,3,2],
  [3,3,5,4,9],
  [3,5,3,9,0]
]

def isVisible(mem, j, i):
  up = [mem[x][i] for x in range(0, j)]
  down = [mem[x][i] for x in range(j + 1, len(mem))]
  left = [mem[j][x] for x in range(0, i)]
  right = [mem[j][x] for x in range(i + 1, len(mem[0]))]
  if all(mem[j][i] > x for x in up) or all(mem[j][i] > x for x in down) or all(mem[j][i] > x for x in left) or all(mem[j][i] > x for x in right):
    return True
  return False

def scenic(mem, j, i):
  upScore, downScore, leftScore, rightScore, loc = 0, 0, 0, 0, 0
  up = reversed([mem[x][i] for x in range(0, j)])
  down = [mem[x][i] for x in range(j + 1, len(mem))]
  left = reversed([mem[j][x] for x in range(0, i)])
  right = [mem[j][x] for x in range(i + 1, len(mem[0]))]
  loc = mem[j][i]
  for x in up:
    upScore += 1
    if x >= loc:
      break
  for x in down:
    downScore += 1
    if x >= loc:
      break
  for x in left:
    leftScore += 1
    if x >= loc:
      break
  for x in right:
    rightScore += 1
    if x >= loc:
      break
  return (upScore * downScore * leftScore * rightScore)

class DayEight:

  mem = []
  visible = []

  def __init__(self, mem):
    self.mem = mem.copy()
    # self.mem = TESTDATA
    
  def partOne(self):
    total = 0
    for i in range(len(self.mem[0])):
      for j in range(len(self.mem)):
        if isVisible(self.mem, j, i):
          total += 1
    return total

  def partTwo(self):
    totals = []
    for i in range(len(self.mem[0])):
      for j in range(len(self.mem)):
        totals.append(scenic(self.mem, j, i))
    return max(totals)

if __name__ == "__main__":
  y = fileOpenIntGrid(8)
  dayEight = DayEight(y)
  print('Day Eight part one : ', dayEight.partOne())
  print('Day Eight part two : ', dayEight.partTwo())