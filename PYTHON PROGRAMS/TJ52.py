class employees:
    def workinghrs(self):
        self.hrs=50
    def printhrs(self):
        print("Total Working Hrs :",self.hrs)
class Trainee(employees):
    def workinghrs(self):
        self.hrs=60
    def resethrs(self):
        super().workinghrs()
employee=employees()
employee.workinghrs()
employee.printhrs()
trainee=Trainee()
trainee.workinghrs()
trainee.printhrs()
# Reset Trainee Hrs
trainee.resethrs()
trainee.printhrs()