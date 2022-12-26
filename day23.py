from aoc import *
import time
import tkinter as tk

def printScreen(mem):
  root = tk.Tk()
  canvas = tk.Canvas(root, width=1000, height=1000)
  canvas.pack()
  for i in mem:
    canvas.create_rectangle(i[0]*10, i[1]*10, i[0]*10+10, i[1]*10+10, fill="black")
  root.update()
  root.mainloop()
  # root.after(1000)
  # root.destroy()

def elfMove(x, y, grid):
  for i in range(x-1, x+2):
    for j in range(y-1, y+2):
      if (i, j) in grid:
        for k in range(x-1, x+2):
          if (x+k, y-1) in grid:
            return (x, y - 1)
          elif (x+k, y+1) in grid:
            return (x, y + 1)
        for l in range(y-1, y+2):
          if (x-1, y+l) in grid:
            return (x - 1, y)
          elif (x+1, y+l) in grid:
            return (x + 1, y)
  return (x, y)


class DayTwentyThree:

  mem = []

  def __init__(self, mem):
    for y in range(len(mem)):
      for x in range(len(mem[0])):
        if mem[y][x] == '#':
          self.mem.append((x, y))

  def partOne(self):
    propMoves = []
    for _ in range(2):
      printScreen(self.mem)
      for i in self.mem:
        propMoves.append(elfMove(i[0], i[1], self.mem))
      self.mem.clear()
      for i in set(propMoves):
        if propMoves.count(i) == 1:
          self.mem.append(i)
      propMoves.clear()
    maxX = max([x[0] for x in self.mem])
    minX = min([x[0] for x in self.mem])
    maxY = max([x[1] for x in self.mem])
    minY = min([x[1] for x in self.mem])
    return ((maxX - minX) * (maxY - minY)) - len(self.mem)

  def partTwo(self):
    pass

if __name__ == "__main__":
  y = fileOpenLines(23, 't')
  dayTwentyThree = DayTwentyThree(y)
  startTime = time.time()
  print("Part 1: ", dayTwentyThree.partOne(), " in ", round(time.time() - startTime, 2), "s")
  startTime = time.time()
  print("Part 2: ", dayTwentyThree.partTwo(), " in ", round(time.time() - startTime, 2), "s")