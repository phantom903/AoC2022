import os 
import sys

def console_frame(output):
	os.system('clear' if os.name == 'posix' else 'CLS')
	sys.stdout.write(output + "\n")
	sys.stdout.flush()


import time
import math

for t in range(100):
	console_frame("\n".join(["*" * (30 + int(30 * math.sin(.1 * x + .1 * t))) for x in range(30)])) # time-varying sine wave
	time.sleep(.04)