class Point () :
    def __init__(self,x,y) :
        self.x = x
        self.y = y
    def __str__(self) :
        return ("({}, {})".format(self.x, self.y))
p1 = Point(2,3)
print(p1)               
