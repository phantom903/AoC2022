
from aoc import fileOpenLines, fileOpenNewLines, ints
import sys
import time
from day1 import DayOne

if len(sys.argv) > 1:
  dayChoice = sys.argv[1]
else:
  dayChoice = input("Which day?: ")
if dayChoice == "1":
  y = fileOpenLines(1, "i")
  dayOne = DayOne()
  startTime = time.time()
  print("Part 1: ", dayOne.partOne(), " in ", round(time.time() - startTime, 2), "s")
  startTime = time.time()
  print("Part 2: ", dayOne.partTwo(), " in ", round(time.time() - startTime, 2), "s")