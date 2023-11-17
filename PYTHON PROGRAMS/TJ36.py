
"""
# try block in Python
try:
    a=10/0
except Exception as e:
    print(e)
"""
"""
# Try Else
try:
    a=10/0
except Exception as e:
    print(e)
else:
    print(a)
"""
"""
# Try else finally
try:
    a=10/0
except Exception as e:
    print(e)
else:
    print(a)
finally:
    print("thank you")
"""
"""
# Type of Exceptions in Python
print(dir(locals()['__builtins__']))
print(len(dir(locals()['__builtins__'])))
# Nameerror Exception
try:
    print(a)
except NameError as e:
    print("A is not defined")
try:
    print(10/0)
except ZeroDivisionError as e:
    print("denominator not be zero")
try:
    a=int('joes')
except ValueError as e:
    print("please enter the number only")
try:
    a=[10,20,30,40,50]
    print(a[10])
except IndexError as e:
    print("invalid index")
try:
    f=open("tesot.text")
except FileNotFoundError as e:
    print("file is not found")
else:
    print(f.read())
"""
try:
    a=10/20
    print(a)
    b=[10,20,30,40]
    print(b[0])
    a=open('ramu.txt')
except ZeroDivisionError:
    print("denominator cant be zero")
except IndexError:
    print("Invalid Index")
except Exception as e:
    print(e)
