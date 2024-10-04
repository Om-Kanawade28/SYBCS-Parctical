class rectangle:
    def __init__(self):
        self.length = 0.0
        self.breath = 0.0
        self.height = 0.0
        
    def volume(self):
        print("volume of rectangle:-",self.length*self.breath*self.height)
        
    def area(self):
        print("Area of rectangle:-",self.length*self.breath)
        
        
obj = rectangle()
obj.length = int(input("Enter the leanth:-"))
obj.breath = int(input("Enter the breath:-"))
obj.height = int(input("Enteer the height:-"))

obj.volume()
obj.area()
