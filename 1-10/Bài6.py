class animal :
    def __init__ (self,ten):
        self.ten = ten
    def tieng_keu(self) :
        print("Some sound !")
    def getName(self) :
        print("Ten cua no la: %s" %(self.ten))    
class dog(animal) :
    def __init__(self, ten):
        super(dog,self).__init__(ten)
    def tieng_keu(self) :
        print("No sua: Gâu :))") 
con1 = dog("Alaska")
con1.getName()
con1.tieng_keu()

