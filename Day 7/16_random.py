from turtle import *
import random
def randonWalk(turns,distance):
    t = Turtle()
    for x in range(turns):
        if x % 2 == 0:
            t.left(random.randint(0,270))
        else:
            t.right(random.randint(0,270))
        t.forward(distance)
        
randonWalk(40,30)