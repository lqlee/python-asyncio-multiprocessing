
import os

# pi = 4(1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...)

def calculate_pi(start: int, end: int) -> float :
  res = 0.0
  positive = True if start % 2 == 0 else False
  for i in range(start, end) :
    tmp = 1.0 / (float(i * 2) + 1.0)
    if positive :
      res += tmp
    else :
      res -= tmp
    positive = not positive
  return res * 4.0
