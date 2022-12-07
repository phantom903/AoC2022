
from aoc import fileOpenLines, fileOpenNewLines, ints
import sys
import time
from day1 import DayOne

if len(sys.argv) > 1:
  dayChoice = sys.argv[1]
else:
  dayChoice = input("Which day?: ")
if dayChoice == "1":
  y = fileOpenLines(1)
  dayOne = DayOne(y)
  startTime = time.time()
  print("Part 1: ", dayOne.partOne(), " in ", round(time.time() - startTime, 2), "s")
  startTime = time.time()
  print("Part 2: ", dayOne.partTwo(), " in ", round(time.time() - startTime, 2), "s")
elif dayChoice == "2":
  from day2 import DayTwo
  y = fileOpenLines(2,"s")
  dayTwo = DayTwo(y)
  startTime = time.time()
  print("Part 1: ", dayTwo.partOne(), " in ", round(time.time() - startTime, 2), "s")
  startTime = time.time()
  print("Part 2: ", dayTwo.partTwo(), " in ", round(time.time() - startTime, 2), "s")
elif dayChoice == "3":
  from day3 import DayThree
  y = fileOpenLines(3,"s")
  dayThree = DayThree(y)
  startTime = time.time()
  print("Part 1: ", dayThree.partOne(), " in ", round(time.time() - startTime, 2), "s")
  startTime = time.time()
  print("Part 2: ", dayThree.partTwo(), " in ", round(time.time() - startTime, 2), "s")
elif dayChoice == "4":
  from day4 import DayFour
  y = fileOpenLines(4)
  dayFour = DayFour(y)
  startTime = time.time()
  print("Part 1: ", dayFour.partOne(), " in ", round(time.time() - startTime, 2), "s")
  startTime = time.time()
  print("Part 2: ", dayFour.partTwo(), " in ", round(time.time() - startTime, 2), "s")
elif dayChoice == "5":
  from day5 import DayFive
  y = fileOpenLines(5,"s")
  dayFive = DayFive(y)
  startTime = time.time()
  print("Part 1: ", dayFive.partOne(), " in ", round(time.time() - startTime, 2), "s")
  startTime = time.time()
  print("Part 2: ", dayFive.partTwo(), " in ", round(time.time() - startTime, 2), "s")
elif dayChoice == "6":
  from day6 import DaySix
  y = fileOpenLines(6,"s")
  daySix = DaySix(y)
  startTime = time.time()
  print("Part 1: ", daySix.signalParse(4), " in ", round(time.time() - startTime, 2), "s")
  startTime = time.time()
  print("Part 2: ", daySix.signalParse(14), " in ", round(time.time() - startTime, 2), "s")