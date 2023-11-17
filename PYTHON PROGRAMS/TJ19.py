m1=int(input('enter the marks 1 :'))
m2=int(input('enter the marks 2 :'))
m3=int(input('enter the marks 1 :'))
total=m1+m2+m3
average=total/3.0
print("total :",total)
print("average :",average)
if m1>=35 and m2>=35 and m3>=35:
    print("result : pass ")
    if average>=90 and average<=100:
        print("grade : A")
    if average>=80 and average<=90:
        print("grade : B")
    if average>=70 and average<=80:
        print("grade : C")
    else:
        print("grade : D")
else:
    print("result : fail")
    print("grade : no grade")
            
         