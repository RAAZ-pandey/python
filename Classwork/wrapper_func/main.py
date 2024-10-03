#write a fuction to count n and evaluate  a =a = 10 for all values from 0 to n'

import time

def count(n):
    for i in range(0,n):
        a=n*10

ns = [100000 ,234234, 34356, 345, 344, 345]
#n = 100000

def wrapper(func,n):
  
  # code to start  evaluate run time of function call count(n)
  start = time.time() * 1000000
  #print(start_time)
  #count(1000000)   #timming this function call/execution
  func(n)
  end = time.time() *1000000
  #print(end_time)
  print(f"\n n = {n}time to execute is {end- start} micro second")

for n in ns:
   wrapper(count,n)
