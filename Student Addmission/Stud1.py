import sqlite3
import logging

logging.basicConfig(filename= 'login.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')
class Student:

    def __init__(self):
        pass

    def addinfo(self):
        try:
            s = sqlite3.connect("Student")
            cursor = s.cursor()
            logging.debug("Database creation")

            cursor.execute("create table Student (sno int, name  text, age int, address text, phno int);")

            while True:
                sno = int(input("Enter Student Number: "))
                name = input("Enter Student name: ")
                age = int(input("Enter Student age: "))
                address = input("Enter address: ")
                phno = int(input("Enter Phone number: "))

                sql="insert into Student values( %d, '%s', %d ,'%s', %d )"

                cursor.execute(sql % (sno, name, age, address, phno))

                print("Record Inserted Successfully")
                option = input("Do you want to insert one more record[Yes|No] :")
                if option == "No":
                    s.commit()
                    break
        except  :
            logging.warning("please Enter correct input")
            print("please Enter correct"
                  "1 input")


    def display(self):
        try:
            s = sqlite3.connect("Student")
            cursor = s.cursor()
            cursor.execute("select * from Student")
            data = cursor.fetchall()
            for row in data:
                print("Student Number:", row[0])
                print("Student Name:", row[1])
                print("Student Age:", row[2])
                print("Student Address:", row[3])
                print("Student Phone No.:", row[4])
        except :
            print("There is a problem with sql :")

    def updateinfo(self):
        try:
            s = sqlite3.connect("Student")
            cursor = s.cursor()
            cno=int(input("Select Student number for updation"))
            sadd=input("Enter new address:")
            sql="Update Student set address='%s' where sno=%d "
            cursor.execute(sql %(sadd, cno))
            print("Records Updated Successfully")

            s.commit()

        except :
            print("There is a problem with sql :")
        finally:
            if s:
                s.close()
            if cursor:
                s.close()



    def deleteinfo(self):
        try:
            s = sqlite3.connect("Student")
            cursor = s.cursor()
            cno = int(input("Select Student number for deleting student information: "))
            sql="delete from Student where sno=%d"
            cursor.execute(sql % (cno))
            print("Record is Deleted.")
            s.commit()
            s.close()
        except:
            print("There is a problem with sql :")

soj = Student()
for i in range (1,5):
    print(" 1. Add Student Information. \n 2. Display Student Information. \n 3. Update Student Information. \n 4. Delete Student Information.")
    i = int(input("Select your choice: "))
    if i==1:
        soj.addinfo()
    elif i==2:
        soj.display()
    elif i==3:
        soj.updateinfo()
    elif i==4:
        soj.deleteinfo()
    else:
        print("exit")