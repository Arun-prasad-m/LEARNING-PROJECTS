days=int(input("enter the days :"))
if days==0:
    print("good no fine ")
elif days>=1 and days<=5:
    print("fine amount :",days*0.5)
elif days>=5 and days<=10:
    print("fine amount :",days*1)
elif days>=10 and days<=30:
    print("fine amount :",days*5)
else:
    print("membership cancel " )
    