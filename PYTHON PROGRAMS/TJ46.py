class student:
    count=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        student.count+=1
    def printdetail(self):
        print("Name : ",self.name," Age : ",self.age)
    @classmethod
    def total(cls):
        return cls.count
o=student("joes",25)
o.printdetail()
a=student("raja",245)
o.printdetail()
print("Total Admission : ",student.total())
print("Total Admission : ",o.total())
