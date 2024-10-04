class cl:
    def __init__(self):
        self.contry = ''
        self.state = ''
        
    def put(self):
        print(f"I live at {self.contry} in {self.state}")
        
        
obj = cl()
obj.contry = 'india'
obj.state = 'maharashtra'

obj.put()