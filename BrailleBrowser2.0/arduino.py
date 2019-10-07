from pyfirmata import Arduino,util
import time

from Arduino import Arduino


board = Arduino("COM5")

for x in range(5):
  board.digital[13].write(1)
  time.sleep(0.2)
  board.digital[13].write(0)
  time.sleep(0.2)