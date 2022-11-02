from day1 import DayOne
from aoc import fileOpenLines, fileOpenNewLines, ints
import sys
import time

if len(sys.argv) > 1:
  dayChoice = sys.argv[1]
else:
  dayChoice = input("Which day?: ")
# fileName = 'day' + dayChoice
# className = 'Day' + num2words[int(dayChoice)]
# module = importlib.import_module(fileName, className)
if dayChoice == "1":
  y = fileOpenLines(1, "i")
  dayOne = DayOne()
  print("Part 1: " , dayOne.partOne(y))
  print("Part 2: " , dayOne.partTwo(y))
# elif dayChoice == "2":
#   y = fileOpenLines(2, "s")
#   dayTwo = DayTwo(y)
#   print("Part 1: " , dayTwo.partOne())
#   print("Part 2: " , dayTwo.partTwo())
# elif dayChoice == "3":
#   y = fileOpenLines(3, "s")
#   dayThree = DayThree(y)
#   print("Part 1: " , dayThree.partOne())
#   print("Part 2: " , dayThree.partTwo())
# elif dayChoice == "4":
#   y = fileOpenLines(4, "s")
#   dayFour = DayFour(y)
#   print("Part 1: ", dayFour.partOne())
#   print("Part 2: ", dayFour.partTwo())
# elif dayChoice == "5":
#   y = fileOpenLines(5, "s")
#   dayFive = DayFive(y)
#   print("Part 1: ", dayFive.partOne())
#   print("Part 2: ", dayFive.partTwo())
# elif dayChoice == "6":
#   y = fileOpenLines(6, "s")
#   daySix = DaySix(y)
#   print("Part 1: ", daySix.simFish(80))
#   print("Part 2: ", daySix.simFish(256))
# elif dayChoice == "7":
#   y = fileOpenLines(7,"s")
#   daySeven = DaySeven(y)
#   print("Part 1: ", daySeven.partOne())
#   print("Part 2: ", daySeven.partTwo())
# elif dayChoice == "8":
#   y = fileOpenLines(8,"s")
#   dayEight = DayEight(y)
#   print("Part 1: ", dayEight.partOne())
#   print("Part 2: ", dayEight.partTwo())
# elif dayChoice == "9":
#   y = fileOpenLines(9,"s")
#   dayNine = DayNine(y)
#   print("Part 1: ", dayNine.partOne())
#   print("Part 2: ", dayNine.partTwo())
# elif dayChoice == "10":
#   y = fileOpenLines(10,"s")
#   dayTen = DayTen(y)
#   print("Part 1: ", dayTen.partOne())
#   print("Part 2: ", dayTen.partTwo())
# elif dayChoice == "11":
#   y = fileOpenLines('11',"s")
#   dayEleven = DayEleven(y)
#   startTime = time.time()
#   print("Part 1: ", dayEleven.partOne(100), " in ", round(time.time() - startTime,2), "s")
#   startTime = time.time()
#   print("Part 2: ", dayEleven.partTwo(), " in ", round(time.time() - startTime, 2), "s")
# elif dayChoice == "12":
#   y = fileOpenLines(12,"s")
#   dayTwelve = DayTwelve(y)
#   startTime = time.time()
#   print("Part 1: ", dayTwelve.partOne(), " in ", round(time.time() - startTime, 2), "s")
#   startTime = time.time()
#   print("Part 2: ", dayTwelve.partTwo(), " in ", round(time.time() - startTime, 2), "s")
# elif dayChoice == "13":
#   y = fileOpenLines(13,"s")
#   dayThirteen = DayThirteen(y)
#   startTime = time.time()
#   print("Part 1: ", dayThirteen.partOne(), " in ", round(time.time() - startTime, 2), "s")
#   startTime = time.time()
#   print("Part 2: ", dayThirteen.partTwo(), " in ", round(time.time() - startTime, 2), "s")
# elif dayChoice == "14":
#   y = fileOpenLines(14,"s")
#   dayFourteen = DayFourteen(y)
#   startTime = time.time()
#   print("Part 1: ", dayFourteen.simPolymer(10), " in ", round(time.time() - startTime, 2), "s")
#   startTime = time.time()
#   print("Part 2: ", dayFourteen.simPolymer(40), " in ", round(time.time() - startTime, 2), "s")
# elif dayChoice == "15":
#   y = fileOpenLines(15, "s")
#   dayFifteen = DayFifteen(y)
#   startTime = time.time()
#   print("Part 1: ", dayFifteen.partOne(), " in ", round(time.time() - startTime, 2), "s")
#   startTime = time.time()
#   print("Part 2: ", dayFifteen.partTwo(), " in ", round(time.time() - startTime, 2), "s")
# elif dayChoice == "16":
#   y = fileOpenLines(16, "s")
#   daySixteen = DaySixteen(y)
#   startTime = time.time()
#   print("Part 1: ", daySixteen.partOne(), " in ", round(time.time() - startTime, 2), "s")
#   startTime = time.time()
#   print("Part 2: ", daySixteen.partTwo(), " in ", round(time.time() - startTime, 2), "s")
# elif dayChoice == "17":
#   y = fileOpenLines(17,"s")
#   daySeventeen = DaySeventeen(y)
#   startTime = time.time()
#   print("Part 1: ", daySeventeen.partOne(), " in ", round(time.time() - startTime, 2), "s")
#   startTime = time.time()
#   print("Part 2: ", daySeventeen.partTwo(), " in ", round(time.time() - startTime, 2), "s")
# elif dayChoice == "20":
#   from day20 import DayTwenty
#   y = fileOpenLines(20,"s")
#   dayTwenty = DayTwenty(y)
#   startTime = time.time()
#   print("Part 1: ", dayTwenty.partOne(), " in ", round(time.time() - startTime, 2), "s")
#   startTime = time.time()
#   print("Part 2: ", dayTwenty.partTwo(), " in ", round(time.time() - startTime, 2), "s")