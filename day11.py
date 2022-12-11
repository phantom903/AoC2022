from aoc import *
from math import prod

class Monkey:

  def __init__(self, monkey_data):
    self.id = ints(monkey_data[0])[0]
    self.items = ints(monkey_data[1])
    self.op = ' '.join(monkey_data[2].split()[3:])
    self.test = ints(monkey_data[3])[0]
    self.ifTrue = ints(monkey_data[4])[0]
    self.ifFalse = ints(monkey_data[5])[0]
    self.inspected = 0

  def __str__(self):
    return (
      "Monkey ID: " + str(self.id) +
      "\nItems: "+ ','.join([str(i) for i in self.items]) +
      "\nOperation: new = " + self.op +
      "\nTest: divisible by " + str(self.test) +
      "\n  If true: throw to monkey " + str(self.ifTrue) +
      "\n  If false: throw to monkey " + str(self.ifFalse) +
      "\nInspected " + str(self.inspected) + " items"
      )
  
  def inspect(self, partNo=1, modulo=0):
    for i in range(len(self.items)):
      if partNo == 1:
        self.items[i] = eval(self.op, {'old': self.items[i]}) // 3
      else:
        self.items[i] = eval(self.op, {'old': self.items[i]})
        self.items[i] %= modulo
      self.inspected += 1
      if self.items[i] % self.test == 0:
        yield (self.ifTrue, self.items[i])
      else:
        yield (self.ifFalse, self.items[i])
    self.items.clear()

  def takeItem(self, item):
    self.items.append(item)

class DayEleven:

  mem = []
  monkeys = []

  def __init__(self, mem):
    monkey = []
    for line in mem:
      if line in (None, '', '\n\n'):
        self.mem.append(monkey)
        monkey = []
      else:
        monkey.append(line)
    self.mem.append(monkey)

  def partOne(self):
    activity = []
    for i in self.mem:
      self.monkeys.append(Monkey(i))
    for _ in range(20):
      for monkey in self.monkeys:
        for thrown in monkey.inspect():
          self.monkeys[thrown[0]].takeItem(thrown[1])
    for monkey in self.monkeys:
      activity.append(monkey.inspected)
    activity = sorted(activity, reverse=True)
    return activity[0] * activity[1]
  
  def partTwo(self):
    activity = []
    tests = 0
    self.monkeys.clear()
    for i in self.mem:
      self.monkeys.append(Monkey(i))
    tests = prod(i.test for i in self.monkeys)
    for _ in range(10000):
      for monkey in self.monkeys:
        for thrown in monkey.inspect(2, tests):
          self.monkeys[thrown[0]].takeItem(thrown[1])
    for monkey in self.monkeys:
      activity.append(monkey.inspected)
    activity = sorted(activity, reverse=True)
    return activity[0] * activity[1]

if __name__ == "__main__":
  y = fileOpenLines(11)
  dayEleven = DayEleven(y)
  print('Day Eleven part one : ', dayEleven.partOne())
  print('Day Eleven part two : ', dayEleven.partTwo())