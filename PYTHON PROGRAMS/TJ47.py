class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printdetail(self):
        print("Name : ",self.name,"Age : ",self.age)
    @staticmethod
    def welcome():
        print("Welcome to our Institution ")
s1=student("joes",25)
s1.printdetail()
s1.welcome()
s1=student("raja",45)
s1.printdetail()
s1.welcome()

