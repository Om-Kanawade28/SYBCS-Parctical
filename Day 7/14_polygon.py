def polygon():
    t = Turtle()
    sides = int(input("Number of sides="))
    side_length = int(input("Length of each side="))
    for i in range(sides):
        t.fd(side_length)
        t.right(360/sides)

        
polygon()

# Number of sides=5
# Length of each side=200