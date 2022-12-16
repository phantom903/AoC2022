import collections
import time

from aoc import *

class DaySixteen:

  valves = dict()

  def __init__(self, mem):
    for line in mem:
      flow = ints(line)[0]
      ident = line.split(" ")[1]
      connections = [conn.strip(',') for conn in line.split(" ")[9:]]
      self.valves[ident] = (flow, connections)

  def solve(self, start, ticks):
    runs = []
    Q = collections.deque()
    Q.append((start, self.valves[start][0], 0))
    visited = set((i) for i, _, _ in Q)
  
    def push(i, j, d):
      for conn in self.valves[i][1]:
        if self.valves[i][0] > 0 and not conn in visited:
          d += 1
        Q.append((conn, j + ((self.valves[i][0]) * (ticks-d)), d + 1))
      visited.add(i)

    while len(Q):
      (i, j, d) = Q.popleft()
      if d >= ticks:  
        runs.append(j)
      else:
        push(i, j, d)
    
    return runs

  def partOne(self):
    return max(self.solve('AA', 30))

  def partTwo(self):
    pass

if __name__ == "__main__":
  y = fileOpenLines(16)
  daySixteen = DaySixteen(y)
  startTime = time.time()
  print("Part 1: ", daySixteen.partOne(), " in ", round(time.time() - startTime, 2), "s")
  startTime = time.time()
  print("Part 2: ", daySixteen.partTwo(), " in ", round(time.time() - startTime, 2), "s")