from aoc import *

class DaySeven:

  mem = []

  def __init__(self, mem):
    self.mem = mem.copy()
    self.tree = []
    self.pwd = ''
    self.folders = []
    self.fldrlist = []
    for entry in self.mem:
      self.cmdParse(entry)

  def cmdParse(self, entry):
    entry = entry.split(' ')
    if entry[0] == '$': # Command, ls can be ignored
      if entry[1] == 'cd':
        if entry[2] == '/':
          self.pwd = '/'
        elif entry[2] == '..':
          self.pwd = '/'.join(self.pwd.split('/')[:-1])
        else:
          self.pwd += '/' + entry[2]
    else: # entry is a file or folder
      if entry[0] == 'dir':
        self.folders.append(self.pwd + '/' + entry[1])
      else:
        self.tree.append([self.pwd + '/' + entry[1], int(entry[0])])

  def partOne(self):
    total = 0
    for fldr in self.folders:
      self.fldrlist.append((fldr, sum([i[1] for i in self.tree if fldr in i[0]])))
    total = sum([i[1] for i in self.fldrlist if i[1] <= 100000])
    return total

  def partTwo(self):
    delList = []
    spaceNeeded = 30000000 - (70000000 - sum([i[1] for i in self.tree]))
    delList = [i for i in self.fldrlist if i[1] > spaceNeeded]
    return min([i[1] for i in delList])

if __name__ == "__main__":
  y = fileOpenLines(7)
  daySeven = DaySeven(y)
  print('Day Seven part one : ', daySeven.partOne())
  print('Day Seven part two : ', daySeven.partTwo())