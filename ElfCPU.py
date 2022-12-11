class ElfCPU:

  def __init__(self, mem, xReg=1):
    self.mem = mem.copy()
    self.xReg = xReg
    self.ptr = 0
    self.cycles = 0
    self.cycleBreaks = [20,60,100,140,180,220]
    self.signal = 0
    self.screen = [' ' for _ in range(240)] 
  
  def cycle(self, runs = 1):
    for _ in range(runs):
      xPos = (self.xReg + 1 % 40 ) 
      if (self.cycles + 1) % 40 in [xPos - 1, xPos, xPos + 1]:
        self.screen[self.cycles] = chr(9608)
      self.cycles += 1
      if self.cycles in self.cycleBreaks:
        self.signal += (self.xReg * self.cycles)
    return

  def execute(self):
    op = self.mem[self.ptr].split(' ')
    if op[0] == 'noop':
      self.ptr += 1
      self.cycle()
    elif op[0] == 'addx':
      self.cycle(2)
      self.xReg += int(op[1])
      self.ptr += 1
    return    
  
  def run(self):
    while True:
      self.execute()
      if self.ptr >=len(self.mem):
        break
    return self.signal
  
  def printScreen(self):
    output = ''
    for i in range(len(self.screen)):
      output += self.screen[i]
      if (i + 1) % 40 == 0:
        output += '\n'
    print(output)
    return