class studen:
    def __init__(self, name, Msv):
        self.name = name
        self.Msv = Msv 
    def getName(self) :
        print("Ten cua ban : %s" %(self.name))
    def getMsv(self) :
        print("Ma sinh vien cua ban: %s" %(self.Msv))
class Nam(studen) :
    def __init__(self, name, Msv) :
        super().__init__(name, Msv)
        self.sex = "Nam" 
    def getSex(self) :
        print("Gioi tinh cua ban là: %s" %(self.sex))    
studen1 = Nam("Nguyen Ngoc Duong", "B22DCVT112") 
studen1.getName()
studen1.getMsv()    
studen1.getSex()                  
