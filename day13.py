from aoc import *
from ast import literal_eval

def compare(left, right):
  if left == None and right != None:
    return True
  elif type(left) == int and type(right) == int:
    return int(left) < int(right)
  elif type(left) == int and type(right) == list:
    return compare([left], right)
  elif type(left) == list and type(right) == int:
    return compare(left, [right])
  else:
    for (l, r) in zip(left, right):
      if compare(l, r):
        return True
      elif compare(r, l):
        return False
  if len(left) < len(right):
    return True
  return False

class DayThirteen:

  mem = []

  def __init__(self, mem):
    blocks = mem.split('\n\n')
    for i in range(len(blocks)):
      pair = []
      block = blocks[i].splitlines()
      pair.append(literal_eval(block[0]))
      pair.append(literal_eval(block[1]))
      self.mem.append(pair)

  def partOne(self):
    total = 0
    for i in range(len(self.mem)):
      if compare(self.mem[i][0], self.mem[i][1]):
        total += i + 1
    return total

  def partTwo(self):
    toSort = []
    self.mem.append([[[2]], [[6]]])
    for i in self.mem:
      toSort.append(i[0])
      toSort.append(i[1])
    sortedList = bubblesort(toSort, compare)
    return (sortedList.index([[2]]) + 1) * (sortedList.index([[6]]) + 1)

if __name__ == "__main__":
  y = fileOpenRaw(13)
  dayThirteen = DayThirteen(y)
  print('Day Thirteen part one : ', dayThirteen.partOne())
  print('Day Thirteen part two : ', dayThirteen.partTwo())