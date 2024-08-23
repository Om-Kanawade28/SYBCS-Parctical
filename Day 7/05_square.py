from turtle import *
def square(side):
    t = Turtle()
    for i in range(4):
        t.forward(side)
        t.left(90)

        
square(150)