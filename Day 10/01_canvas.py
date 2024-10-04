import turtle

# Set up the turtle
t = turtle.Turtle()
t.width(5)

# Function to draw the letter A
def draw_A():
    t.left(60)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.backward(50)
    t.right(120)
    t.forward(50)
    t.backward(50)
    t.left(120)
    t.backward(50)
    t.left(60)

# Function to draw the letter B
def draw_B():
    t.forward(100)
    t.right(90)
    t.circle(-25, 180)
    t.left(180)
    t.circle(-25, 180)
    t.left(90)
    t.forward(100)
    t.left(90)

# Function to draw the letter C
def draw_C():
    t.penup()
    t.forward(50)
    t.pendown()
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.penup()
    t.forward(50)
    t.pendown()

# Function to draw the letter D
def draw_D():
    t.forward(100)
    t.right(90)
    t.circle(-50, 180)
    t.right(90)
    t.forward(100)
    t.left(90)

# Draw the letters with spacing
draw_A()
t.penup()
t.forward(60)
t.pendown()
draw_B()
t.penup()
t.forward(60)
t.pendown()
draw_C()
t.penup()
t.forward(60)
t.pendown()
draw_D()

# Hide the turtle and display the window
t.hideturtle()
turtle.done()
