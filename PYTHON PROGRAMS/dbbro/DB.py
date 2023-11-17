import sqlite3
con=sqlite3.connect('users.db')
def insertdata(name,age,city):
    qry="insert into users (NAME,AGE,CITY) values (?,?,?);"
    con.execute(qry,(name,age,city))
    con.commit()
    print("user details added")

def updatedata(name,age,city,id):
    qry="update users set NAME=?,AGE=?,CITY=? where id=?;"
    con.execute(qry,(name,age,city,id))
    con.commit()
    print("user details updated")

def deletedata(id):
    qry="delete from users where id=?;"
    con.execute(qry,(id))
    con.commit()
    print("user details deleted")

def selectdata():
    qry="select * from users"
    result=con.execute(qry)
    for row in result:
        print(row)

print("""
1.insert
2.update
3.delete
4.select
""")
ch=1
while ch==1:
    c=int(input("select your choice : "))
    if(c==1):
        print("add new record")
        name=input("enter the name : ")
        age=input("enter the age : ")
        city=input("enter the city : ")
        insertdata(name,age,city)
    elif(c==2):
        print("edit the record")
        id=input("enter the id : ")
        name=input("enter the name : ")
        age=input("enter the age : ")
        city=input("enter the city : ")
        updatedata(name,age,city,id)

    elif(c==3):
        print("delete the record")
        id=input("enter the id : ")
        deletedata(id)
    elif(c==4):
        print("print all record")
        selectdata()
    else:
        print("invalid selection")
    ch=int(input("enter 1 to continue : "))
print("thank you")
    
   
    