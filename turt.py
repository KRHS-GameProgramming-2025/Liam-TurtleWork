# ----Setup-----
from turtle import *
greg = Turtle()

# ----Code-----
greg.speed(0)

def square(size):
    count = 0
    while count < 1000:
        greg.fd(size)
        greg.lt(92)
        count = count + 1
        print(count)
 
square(100)
greg.fd(125)
square(50)

# ----End----
done()
