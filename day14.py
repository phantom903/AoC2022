from aoc import *

class DayFourteen:

  rocks = [] 

  def __init__(self, mem):
    for line in mem:
      self.rocks.append(line)
    self.maxY = int(max([max([[int(x) for x in rock.split(',')][1] for rock in rocks.split(' -> ')]) for rocks in self.rocks]))
    self.cave = [['.' for x in range(0, 1000)] for y in range(0, self.maxY + 2)]
    self.p1 = 0
  
  def addPath(self, rock):
    rock = rock.split(' -> ')
    for i in range(len(rock) -1):
      startx, starty = [int(x) for x in rock[i].split(',')]
      endx, endy = [int(x) for x in rock[i+1].split(',')]
      if startx == endx:
        for y in range(min(starty, endy), max(starty, endy) + 1):
          self.cave[y][startx] = '#'
      else:
        for x in range(min(startx, endx), max(startx, endx) + 1):
          self.cave[starty][x] = '#'
  
  def dropSand(self, x, y):
    if 0 <= y <= self.maxY and 0 <= x <= len(self.cave[0]):
      if self.cave[y+1][x] == '.':
        return self.dropSand(x, y+1)
      elif self.cave[y+1][x-1] == '.':
        return self.dropSand(x-1, y+1)
      elif self.cave[y+1][x+1] == '.':
        return self.dropSand(x+1, y+1)
    self.cave[y][x] = 'o'
    return (x, y)

  def partOne(self):
    lastDropped = (0, 0)
    count = 0
    for rock in self.rocks:
      self.addPath(rock)
    while lastDropped[1] != self.maxY + 1:
      count += 1
      lastDropped = self.dropSand(500, 0)
    self.p1 = count -1
    return count - 1

  def partTwo(self):
    lastDropped = (0, 0)
    count = 0
    for rock in self.rocks:
      self.addPath(rock)
    while lastDropped != (500,0):
      count += 1
      lastDropped = self.dropSand(500, 0)
    return count + self.p1 + 1

if __name__ == "__main__":
  y = fileOpenLines(14)
  dayFourteen = DayFourteen(y)
  print('Day Fourteen: part one : ', dayFourteen.partOne())
  print('Day Fourteen: part two : ', dayFourteen.partTwo())