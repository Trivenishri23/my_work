import sqlite3

f=open("D:\example.txt","r")

d1=dict()
dlist=list()
key=['name', 'Age', 'CNAme', 'salary', 'Designation']
for i in f.readlines():
    d=i.strip()
    dlist.append(d.split(","))

db=sqlite3.connect("simple1")
cursor=db.cursor()

cursor.execute("create table Employee (name  text, age int, cname text, sal int, des text);")
print(dlist)
for j in dlist:
    q=f"insert into Employee values ('{j[0]}', '{j[1]}', '{j[2]}', '{j[3]}', '{j[4]}');"
    cursor.execute(q)

#cursor.execute("select * from User;")

db.commit()
db.close()
