class Father:
    def displayFather(self,name,age):
        self.fatherName=name
        self.fatherAge=age
        print("Name=",self.fatherName)
        print("Age=",self.fatherAge)
class Child(Father):
    def displySon(self,nm,ag):
        self.SonName=nm
        self.SonAge=ag
        print("Name=",self.SonName,self.fatherName)
        print("Age=",self.SonAge)
class Result(Child):
    def displayResult(self):
        print("Age difference=",self.fatherAge-self.SonAge)
obj=Result()
obj.displayFather("Balaso Patil",54)
obj.displySon("Sakshi",21)
obj.displayResult()
