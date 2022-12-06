from aoc import *

class DaySix:

  mem = []

  def __init__(self, mem):
    self.mem = mem.copy()

  def signalParse(self, num):
    buffer = self.mem[0]
    for i in range(num-1, len(buffer)):
      if len(set([i for i in buffer[i-num:i]])) == num:
        return i

if __name__ == "__main__":
  y = fileOpenLines(6)
  daySix = DaySix(y)
  print('Day Six part one : ', daySix.signalParse(4))
  print('Day Six part two : ', daySix.signalParse(14))