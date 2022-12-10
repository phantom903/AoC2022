from aoc import *
from ElfCPU import ElfCPU

class DayTen:

  mem = []

  def __init__(self, mem):
    self.mem = mem.copy()
    self.elfCpu = ElfCPU(self.mem)

  def partOne(self):
    return self.elfCpu.run()

  def partTwo(self):
    self.elfCpu.printScreen()
    return input("What text is on the screen?")

if __name__ == "__main__":
  y = fileOpenLines(10)
  dayTen = DayTen(y)
  print('Day Ten part one : ', dayTen.partOne())
  print('Day Ten part two : ', dayTen.partTwo())