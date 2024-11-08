class vector () :
    def __init__(self,x,y) :
        self.x = x
        self.y = y
    def __str__(self) :
        return ("({}, {})".format(self.x, self.y))
    def __add__(self, other) :
        x = self.x + other.x
        y = self.y + other.y
        return (x,y)
    def __sub__(self, other) :
        x = self.x - other.x
        y = self.y - other.y
        return(x,y)
v1 = vector (2,3) 
v2 = vector (9,4)
v3 = v1 + v2 
v4 = v1 - v2
print(v1, v2, v3, v4)       
