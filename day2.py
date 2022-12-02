from aoc import *

TESTDATA = ["A Y", "B X", "C Z"]

def score(handOne, handTwo):
  if handTwo == 3 and handOne == 1:
    return 0
  elif handTwo > handOne:
    return 6
  elif handTwo == handOne:
    return 3
  elif handTwo == 1 and handOne == 3:
    return 6
  else:
    return 0

def parseRound(opp, plr):
  handOne = ord(opp) - 64
  handTwo = ord(plr) - 87
  return handTwo + score(handOne, handTwo)

class DayTwo:

  mem = []

  def __init__(self, mem):
    self.mem = mem.copy()
    # self.mem = TESTDATA

  def partOne(self):
    total = 0
    for i in range(len(self.mem)):
      handOne, handTwo = self.mem[i].split(' ')
      total += parseRound(handOne, handTwo)
    return total

  def partTwo(self):
    total = 0
    for i in range(len(self.mem)):
      handOne, outcome = self.mem[i].split(' ')
      if outcome == 'X': #Lose
        total += ((ord(handOne)-66) % 3) + 1
      elif outcome == 'Y': #Draw
        total += (ord(handOne) - 64) + 3
      else: #Win
        total += ((ord(handOne) - 64) % 3) + 7
    return total

if __name__ == "__main__":
  y = fileOpenLines(2, "s")
  dayTwo = DayTwo(y)
  print('Day Two part one : ', dayTwo.partOne())
  print('Day Two part two : ', dayTwo.partTwo())