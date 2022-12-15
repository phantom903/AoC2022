from aoc import *

class DayFifteen:

  sensors = []
  row = set()

  def populate(self, sensor, checkRow=2000000):
    x1, y1, x2, y2 = sensor
    dist = manhattan((x1, y1), (x2, y2))
    if y1 > checkRow and (y1 - dist) <= checkRow:
      over = abs(y1 - checkRow - dist)
      for x in range(x1 - over, x1 + over + 1):
        self.row.add((x, checkRow))
    elif y1 < checkRow and y1 + dist >= checkRow:
      over = abs((y1 + dist) - checkRow)
      for x in range(x1 - over, x1 + over + 1):
        self.row.add((x, checkRow))

  def __init__(self, mem):
    for line in mem:
      self.sensors.append(ints(line))
      
  def partOne(self, checkRow=2000000):
    for sensor in self.sensors:
      self.populate(sensor, checkRow=checkRow)
    for sensor in self.sensors:
      if sensor[3] == checkRow and tuple(sensor[2:4]) in self.row:
        self.row.remove(tuple(sensor[2:4]))
    return len(self.row)
      

  def partTwo(self):
    pairs = []
    for sensor in self.sensors:
      x1, y1, x2, y2 = sensor
      dist = manhattan((x1, y1), (x2, y2))
      for sensor2 in self.sensors[1:]:
        x3, y3, x4, y4 = sensor2
        dist2 = manhattan((x3, y3), (x4, y4))
        dist3 = manhattan((x1, y1), (x3, y3))
        if dist3 == dist + dist2 + 2:
          pairs.append((sensor, sensor2))
    print(pairs)

if __name__ == "__main__":
  y = fileOpenLines(15)
  # y = fileOpenLines(15, 't')
  dayFifteen = DayFifteen(y)
  print('Day Fifteen part one : ', dayFifteen.partOne())
  # print('Day Fifteen part one : ', dayFifteen.partOne(10))
  print('Day Fifteen part two : ', dayFifteen.partTwo())