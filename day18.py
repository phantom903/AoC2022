from aoc import *
import time
from collections import Counter

class DayEighteen:

  cubes = []

  def __init__(self, mem):
    for i in range(len(mem)):
      self.cubes.append([int(x) for x in mem[i].split(",")])

  def partOne(self):
    total = 0
    for cube in self.cubes:
      sides = 6
      xy = Counter([(x,y) for [x, y, z] in self.cubes if abs(z - cube[2]) == 1])
      sides -= xy[(cube[0], cube[1])]
      xz = Counter([(x,z) for [x, y, z] in self.cubes if abs(y - cube[1]) == 1])
      sides -= xz[(cube[0], cube[2])]
      yz = Counter([(y,z) for [x, y, z] in self.cubes if abs(x - cube[0]) == 1])
      sides -= yz[(cube[1], cube[2])]
      total += sides
    return total

  def partTwo(self):

    return sides


if __name__ == "__main__":
  y = fileOpenLines(18)
  dayEighteen = DayEighteen(y)
  startTime = time.time()
  print("Part 1: ", dayEighteen.partOne(), " in ", round(time.time() - startTime, 2), "s")
  startTime = time.time()
  print("Part 2: ", dayEighteen.partTwo(), " in ", round(time.time() - startTime, 2), "s")