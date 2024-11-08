class point () :
    def __init__(self,x,y) :
        self.x = x
        self.y = y
    def __str__(self) :
        return ("({}, {})".format(self.x, self.y))
    def __lt__(self,other ): #self đối tượng hiện tại, other đối tượng cânf so sánh vs đối tượng hiện tại
        hien_tai = (self.x**2) + (self.y**2)
        the_others = (other.x**2) + (other.y**2)
        return hien_tai < the_others
p1 = point (1,2)
p2 = point (3,4)
p3 = point (2,3)
print(p1<p2), print(p2<p3), print(p1<p3)    
