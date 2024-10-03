import time


n = 100000

def wrapper(func,*args,**kwargs):
  def wrappeed(*args,**kwargs):
    # code to start  evaluate run time of function call count(n)
    start = time.time() * 1000000
    func(*args,**kwargs)   #timming this function call/execution
    end = time.time() *1000000
    print(f"\n n = {n}time to execute is {end- start} micro second")
  #wrappeed(*args,**kwargs)
  return wrappeed


@wrapper  #decorator
def count(n):
    for i in range(0,n):
        a=n*10
count(n)

@wrapper
def random():
   pass
random()

#wrapped_fuc = wrapper(count,n)
#wrapped_count = wrapper(count,n)
#wrapped_count(n)


