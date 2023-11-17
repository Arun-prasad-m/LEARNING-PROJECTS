class student():
    name="ram kumar"
    age=25
''' This is Class Attributes '''
# getattr method
print(getattr(student,'name'))
print(getattr(student,'age'))
print(getattr(student,'gender','no such attributre found'))
# Dot Notation
print(student.name)
print(student.age)
print("-------------------------")
# setattr
setattr(student,'name','tutor joes')
print(student.name)
setattr(student,'gender','male')
print(student.gender)
student.city="selam"
print(student.city)
print(student.__dict__)
delattr(student,"city")
print(student.__dict__)
del student.gender
print(student.__dict__)