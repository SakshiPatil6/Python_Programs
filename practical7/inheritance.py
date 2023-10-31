class Person:
    def __init__(self,name,rollno):
        self.StudentName=name
        self.StudentRollno=rollno
    def display(self):
        print("Name=",self.StudentName)
        print("Rollno=",self.StudentRollno)
obj=Person("Sakshi Patil",71)
obj.display()
