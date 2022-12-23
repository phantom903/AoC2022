from aoc import *
import time

class DayTwentyOne:

  def __init__(self, mem):
    self.rules = dict()
    for line in mem:
      line = line.split(' ')
      self.rules.update({line[0].strip(':') : ' '.join(i for i in line[1:])})

  def calc(self, start):
    line = self.rules[start].split(' ')
    if len(line) == 1:
      return int(float(line[0]))
    else:
      if line[1] == '+':
        return int(self.calc(line[0]) + self.calc(line[2]))
      elif line[1] == '*':
        return int(self.calc(line[0]) * self.calc(line[2]))
      elif line[1] == '/':
        return int(self.calc(line[0]) / self.calc(line[2]))
      elif line[1] == '-':
        return int(self.calc(line[0]) - self.calc(line[2]))

  def partOne(self):
    return int(self.calc('root'))

  def partTwo(self):
    l, r = self.rules['root'].split(' ')[0], self.rules['root'].split(' ')[2]
    rVal, lVal = self.calc(r), self.calc(l)
    while rVal != lVal:
      if abs(rVal - lVal) > 100:
        self.rules['humn'] = str(int(float(self.rules['humn']) + abs(rVal - lVal)/10))
      else:
        self.rules['humn'] = str(int(self.rules['humn']) + 1)
      rVal, lVal = self.calc(r), self.calc(l)
    return(self.rules['humn'])


if __name__ == "__main__":
  y = fileOpenLines(21)
  dayTwentyOne = DayTwentyOne(y)
  startTime = time.time()
  print("Part 1: ", dayTwentyOne.partOne(), " in ", round(time.time() - startTime, 2), "s")
  startTime = time.time()
  print("Part 2: ", dayTwentyOne.partTwo(), " in ", round(time.time() - startTime, 2), "s")