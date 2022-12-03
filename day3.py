from aoc import *

TESTDATA = [
  "vJrwpWtwJgWrhcsFMMfFFhFp",
  "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
  "PmmdzqPrVvPwwTWBwg",
  "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
  "ttgJtRGJQctTZtZT",
  "CrZsJsPPZsGzwwsLwLmpwMDw"
]

def findCommon(str1, str2, str3=''):
  for letter in str1:
    if letter in str2:
      if str3 != '':
        if letter in str3:
          return letter
      else:
        return letter
  return ''

class DayThree:
  mem = []
  lookup = dict()

  def __init__(self, mem):
    self.mem = mem.copy()
    # self.mem = TESTDATA
    for i in range(26):
      self.lookup.update({chr(i+97):i+1})
      self.lookup.update({chr(i+65):i+27})

  def partOne(self):
    total = 0
    for i in range(len(self.mem)):
      h1, h2 = self.mem[i][:len(self.mem[i])//2], self.mem[i][len(self.mem[i])//2:]
      total += self.lookup[findCommon(h1,h2)]
      # print("Letter: ", letter, "Value: ", self.lookup[letter], "Total: ", total)
    return total

  def partTwo(self):
    total = 0
    for i in range(0, len(self.mem), 3):
      total += self.lookup[findCommon(self.mem[i], self.mem[i+1], self.mem[i+2])]
    return total

if __name__ == "__main__":
  y = fileOpenLines(3)
  dayThree = DayThree(y)
  print('Day Three part one : ', dayThree.partOne())
  print('Day Three part two : ', dayThree.partTwo())