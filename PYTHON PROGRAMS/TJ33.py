"""
# No Return Type Without Argument Function in Python
def add():
    a=(int(input("enter the number of A : ")))
    b=(int(input("enter the number of B : ")))
    c=a+b
    print("total", c)
add()
"""
"""
# No Return Type With Argument Function in Python
def sub(a, b):
    c = a - b
    print("Difference : ", c)
"""
"""
# Return Type Without Argument Function in Python
def mul():
    a = int(input("Enter The Value of A : "))
    b = int(input("Enter The Value of B : "))
    c = a * b
    return c
x=mul()
print("Mul ",x)
"""
# Return Type With Argument Function in Python
"""
def div(a, b):
    c = a / b
    return c
 
 
x = div(25, 2)
print("Division ", x)
"""
"""
# Arbitrary Arguments Function in Python (*)
def class_10(*students):
    print (students)
    for user in students:
        print(user)
class_10("ram","arun","devi")
"""
"""
# Keyword Arguments Function in Python
def message(name,age):
    print(name,"age is ",age)
message(age=35,name="arun")
"""
"""
# Arbitrary Keyword Arguments in Python(**)
def biodata(**data):
    print(data)
biodata(name="arun",age=35,gender="male")
"""
"""
# Default Parameter Function in Python
def biodata(name,gender="male"):
    print(name,"gender is",gender)
biodata("arun","female")
biodata("arun")
"""
"""
# Passing a List as an Argument in Function Python
def Total(marks):
    return sum(marks)
print(Total([1,2,3,4,5]))
"""
"""
# recursive function
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
print(factorial(5))
"""
c=lambda a,b:a+b
print(c(1,2))
