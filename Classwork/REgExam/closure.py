"""def outer_fun(massage):
    #value of massage is present here
     def inner_fun():
          print(massage)
     # inner_fun()
     return inner_fun

closure =outer_fun("Namste from Rajkumar")
closure()"""


def counter():
    #value of massage is present here
     count = 0
     def increament():
          nonlocal count
          count+=1
          print(count)
     # inner_fun()
     return increament

c1= counter()
c1()
c1()

c2 = counter()
c2()
c1()




