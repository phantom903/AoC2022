from aoc import *
import time
import pygame

colors = [
  (0, 0, 0),
  (120, 37, 179),
  (100, 179, 179),
  (80, 34, 22),
  (80, 134, 22),
  (180, 34, 22),
  (180, 34, 122)
]

class Rock:

  #  0,  1,  2,  3
  #  4,  5,  6,  7
  #  8,  9, 10, 11
  # 12, 13, 14, 15
  rocks = [
    [12, 13, 14, 15],
    [5, 8, 9, 10, 13],
    [6, 10, 12, 13, 14],
    [0, 4, 8, 12],
    [8, 9, 12, 13]
  ]

  def __init__(self, x, y, type):
    self.x = x
    self.y = y
    self.type = type
    self.color = random.randint(1, len(colors) - 1)

  def image(self):
    return self.figures[self.type]

class Tetris:
    
    score = 0
    state = "start"
    field = []
    height = 0
    width = 0
    x = 100
    y = 60
    zoom = 20
    figure = None

    def __init__(self, height, width):
      self.height = height
      self.width = width
      for i in range(height):
        new_line = []
        for j in range(width):
          new_line.append(0)
        self.field.append(new_line)
    
    def new_figure(self, y, type):
      self.figure = Rock(3, y, type)
    
    def intersects(self):
      intersection = False
      for i in range(4):
        for j in range(4):
          if i * 4 + j in self.figure.image():
            if i + self.figure.y > self.height - 1 or \
              j + self.figure.x > self.width - 1 or \
              j + self.figure.x < 0 or \
              self.field[i + self.figure.y][j + self.figure.x] > 0:
                intersection = True
      return intersection

    def freeze(self):
      for i in range(4):
        for j in range(4):
          if i * 4 + j in self.figure.image():
            self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
      self.new_figure()
      if self.intersects():
        game.state = "gameover"
   
    def go_down(self):
      self.figure.y += 1
      if self.intersects():
        self.figure.y -= 1
        self.freeze()

    def go_side(self, dx):
      old_x = self.figure.x
      self.figure.x += dx
      if self.intersects():
        self.figure.x = old_x
        
class DaySeventeen:

  mem = []

  def __init__(self, mem):
    self.mem = mem.copy()

  def partOne(self):
    pygame.init()

  def partTwo(self):
    pass

if __name__ == "__main__":
  y = fileOpenLines(17)
  daySeventeen = DaySeventeen(y)
  startTime = time.time()
  print("Part 1: ", daySeventeen.partOne(), " in ", round(time.time() - startTime, 2), "s")
  startTime = time.time()
  print("Part 2: ", daySeventeen.partTwo(), " in ", round(time.time() - startTime, 2), "s")