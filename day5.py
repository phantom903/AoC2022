from aoc import *
from collections import deque
from re import findall
from copy import deepcopy

class DayFive:

  mem = []
  stacks = [deque() for i in range(0,9)]
  instr = []

  def __init__(self, mem):
    self.mem = mem.copy()
    # Grim:
    for i in range(7,-1,-1):
      k = 0
      for j in range(1, 35, 4):
        if self.mem[i][j] != ' ':
          self.stacks[k].append(self.mem[i][j])
        k += 1
    for i in range(0,10):
      del self.mem[0]
    for line in self.mem:
      self.instr.append(findall(r'\d+', line))
     
  def partOne(self):
    result = ''
    stacks = deepcopy(self.stacks)
    instr = self.instr.copy()
    for line in instr:
      for i in range(int(line[0])):
        stacks[int(line[2])-1].append(stacks[int(line[1])-1].pop())
    for stack in stacks:
      result += stack.pop()
    return result

  def partTwo(self):
    result = ''
    stacks = deepcopy(self.stacks)
    instr = self.instr.copy()
    crane = deque()
    for line in instr:
      for i in range(int(line[0])):
        crane.append(stacks[int(line[1])-1].pop())
      for i in range(int(line[0])):  
        stacks[int(line[2])-1].append(crane.pop())
    for stack in stacks:
      result += stack.pop()
    return result

if __name__ == "__main__":
  y = fileOpenLines(5)
  dayFive = DayFive(y)
  print('Day Five part one : ', dayFive.partOne())
  print('Day Five part two : ', dayFive.partTwo())