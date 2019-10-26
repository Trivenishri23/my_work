import sqlite3
from abc import ABC , abstractmethod

class Bank(ABC):
    def __init__(self):
        pass

    def addinfo(self):
        pass

    def inerest(self):
        pass

    def withdraw(self):
        pass

    def deposit(self):
        pass

class Sbi(Bank):
    try:
        def addinfo(self):
            b = sqlite3.connect("Bank")
            cursor = b.cursor()

            #cursor.execute("create table Sbi (cid int primary key, cname text, bname text, acno int unique, balance double )")
            while True:
                cid = int(input("Enter Customer ID:  "))
                cname = input("Enter Customer Name: ")
                bname = input("Enter Bank Name: ")
                acno = int(input("Enter Customer Account Number: "))
                balance = float(input("Enter Balance: "))

                sql = "Insert into Sbi values(%d, '%s', '%s', %d, %f )"
                cursor.execute(sql % (cid, cname, bname, acno, balance))

                print("Record is successfully Created")
                option=input("Do you want to insert one more record[Yes|No] :")
                if option=="No" or option=="no":
                    b.commit()
                    break
    except:
        print("Please Enter valid input.")

    def interest(self):
        try:
            b = sqlite3.connect("Bank")
            cursor = b.cursor()

            n = int(input("Select Customer Account Number: "))
            q = "Select balance from Sbi where acno=%d"

            t = float(input("Enter Time limit : "))
            print("Rate of Interest of SBI Bank is 8%.")

            j = cursor.execute(q % (n))
            j = cursor.fetchone()
            r = j[0] * 8 * t / 100
            print(f"Rate of interest is:{r}")
        except:
            print("Please Enter valid input")

    def display(self):
        b = sqlite3.connect("Bank")
        cursor = b.cursor()

        cursor.execute("select * from Sbi")
        data = cursor.fetchall()
        for row in data:
            print("Customer ID", row[0])
            print("Customer Name:", row[1])
            print("Bank Name:", row[2])
            print("Account Number:", row[3])
            print("Balance:", row[4])

    def deposit(self):
        try:
            b = sqlite3.connect("Bank")
            cursor = b.cursor()

            n = int(input("Select Customer Account Number: "))
            q = "Select balance from Sbi where acno=%d"
            w = float(input("Enter deposit Amount: "))

            j = cursor.execute(q % (n))
            j = cursor.fetchone()
            wmon = j[0] + w
            sql = "update Sbi set balance=%f where acno=%d"
            cursor.execute(sql % (wmon, n))
            b.commit()
        except:
            print("Please enter valid input.")

    def withdraw(self):
        try:
            b = sqlite3.connect("Bank")
            cursor = b.cursor()

            n = int(input("Select Customer Account Number: "))
            q = "Select balance from Sbi where acno=%d"
            w=float(input("Enter withdraw money: "))

            j = cursor.execute(q % (n))
            j = cursor.fetchone()
            wmon=j[0]-w
            sql="update Sbi set balance=%f where acno=%d"
            cursor.execute(sql %(wmon, n))
            b.commit()
        except:
            print("Please Enter valid input")

class Hdfc(Bank):
    try:
        def addinfo(self):
            b = sqlite3.connect("Bank")
            cursor = b.cursor()
            cursor.execute("create table Hdfc (cid int primary key, cname text, bname text, acno int unique, balance double )")
            while True:
                cid = int(input("Enter Customer ID:  "))
                cname = input("Enter Customer Name: ")
                bname = input("Enter Bank Name: ")
                acno = int(input("Enter Customer Account Number: "))
                balance = float(input("Enter Balance: "))

                sql = "Insert into Hdfc values(%d, '%s', '%s', %d, %f )"
                cursor.execute(sql % (cid, cname, bname, acno, balance))

                print("Record is successfully Created")
                option = input("Do you want to insert one more record[Yes|No] :")
                if option == "No" or option == "no":
                    b.commit()
                    break
    except:
        print("Please Enter valid input")

    def interest(self):
        try:
            b = sqlite3.connect("Bank")
            cursor = b.cursor()

            n = int(input("Select Customer Account Number: "))
            q = "Select balance from Hdfc where acno=%d"

            t = float(input("Enter Time limit : "))
            print("Rate of Interest of HDFC Bank is 8%.")

            j = cursor.execute(q %(n))
            j = cursor.fetchone()
            r = j[0 ] * 8 * t / 100
            print(f"Rate of interest is:{r}")
        except:
            print("Please Enter valid input")

    def withdraw(self):
        try:
            b = sqlite3.connect("Bank")
            cursor = b.cursor()

            n = int(input("Select Customer Account Number: "))
            q = "Select balance from Hdfc where acno=%d"
            w=float(input("Enter withdraw money: "))

            j = cursor.execute(q % (n))
            j = cursor.fetchone()
            wmon=j[0]-w
            sql="update Hdfc set balance=%f where acno=%d"
            cursor.execute(sql %(wmon, n))
            b.commit()
        except:
            print("Please Enter valid input")

    def display(self):
        b = sqlite3.connect("Bank")
        cursor = b.cursor()

        cursor.execute("select * from Hdfc")
        data = cursor.fetchall()
        for row in data:
            print("Customer ID", row[0])
            print("Customer Name:", row[1])
            print("Bank Name:", row[2])
            print("Account Number:", row[3])
            print("Balance:", row[4])

    def deposit(self):
        try:
            b = sqlite3.connect("Bank")
            cursor = b.cursor()

            n = int(input("Select Customer Account Number: "))
            q = "Select balance from Hdfc where acno=%d"
            w = float(input("Enter deposit Amount: "))

            j = cursor.execute(q % (n))
            j = cursor.fetchone()
            wmon = j[0] + w
            sql = "update Hdfc set balance=%f where acno=%d"
            cursor.execute(sql % (wmon, n))
            b.commit()
        except:
            print("Please enter valid input.")

class Icici(Bank):
    def addinfo(self):
        b = sqlite3.connect("Bank")
        cursor = b.cursor()

        cursor.execute("create table Icici (cid int primary key, cname text, bname text, acno int unique, balance double )")

        while True:
            cid = int(input("Enter Customer ID:  "))
            cname = input("Enter Customer Name: ")
            bname = input("Enter Bank Name: ")
            acno = int(input("Enter Customer Account Number: "))
            balance = float(input("Enter Balance: "))

            sql = "Insert into Icici values(%d, '%s', '%s', %d, %f )"
            cursor.execute(sql % (cid, cname, bname, acno, balance))

            print("Record is successfully Created")
            option = input("Do you want to insert one more record[Yes|No] :")
            if option == "No" or option == "no":
                b.commit()
                break

    def interest(self):
        try:
            b = sqlite3.connect("Bank")
            cursor = b.cursor()

            n = int(input("Select Customer Account Number: "))
            q = "Select balance from Icici where acno=%d"

            t = float(input("Enter Time limit : "))
            print("Rate of Interest of SBI Bank is 8%.")

            j = cursor.execute(q % (n))
            j = cursor.fetchone()
            r = j[0] * 8 * t / 100
            print(f"Rate of interest is:{r}")
        except:
            print("Please Enter valid input")

    def display(self):
        b = sqlite3.connect("Bank")
        cursor = b.cursor()

        cursor.execute("select * from Icici")
        data = cursor.fetchall()
        for row in data:
            print("Customer ID", row[0])
            print("Customer Name:", row[1])
            print("Bank Name:", row[2])
            print("Account Number:", row[3])
            print("Balance:", row[4])

    def deposit(self):
        try:
            b = sqlite3.connect("Bank")
            cursor = b.cursor()

            n = int(input("Select Customer Account Number: "))
            q = "Select balance from Icici where acno=%d"
            w = float(input("Enter deposit Amount: "))

            j = cursor.execute(q % (n))
            j = cursor.fetchone()
            wmon = j[0] + w
            sql = "update Icici set balance=%f where acno=%d"
            cursor.execute(sql % (wmon, n))
            b.commit()
        except:
            print("Please enter valid input.")

    def withdraw(self):
        try:
            b = sqlite3.connect("Bank")
            cursor = b.cursor()

            n = int(input("Select Customer Account Number: "))
            q = "Select balance from Icici where acno=%d"
            w=float(input("Enter withdraw money: "))

            j = cursor.execute(q % (n))
            j = cursor.fetchone()
            wmon=j[0]-w
            sql="update Icici set balance=%f where acno=%d"
            cursor.execute(sql %(wmon, n))
            b.commit()
        except:
            print("Please Enter valid input")

for bnk in range(1,5):
    print(" 1. SBI. \n 2. HDFC. \n 3. ICICI. \n 4. EXIT.")
    bnk=int(input("please select your bank: "))

    if bnk==1:
        sobj=Sbi()
        for i in range(1,7):
            print(" 1. Add Customer \n 2. Calculate interest. \n 3. Withdraw Amount. \n 4. Deposite Amount ")
            i=int(input("Select your transaction type: "))
            if i==1:
                sobj.addinfo()
            elif i==2:
                sobj.display()
                sobj.interest()
            elif i==3:
                sobj.display()
                sobj.withdraw()
                sobj.display()
            elif i==4:
                sobj.display()
                sobj.deposit()
                sobj.display()
            else:
                print("Sorry ! Wrong choice.")
    elif bnk==2:
        hobj=Hdfc()
        for i in range(1, 7):
            print(" 1. Add Customer \n 2. Calculate interest. \n 3. Withdraw Amount. \n 4. Deposite Amount")
            i = int(input("Select your transaction type: "))

            if i == 1:
                hobj.addinfo()
            elif i == 2:
                hobj.display()
                hobj.interest()
            elif i == 3:
                hobj.display()
                hobj.withdraw()
                hobj.display()
            elif i == 4:
                hobj.display()
                hobj.deposit()
                hobj.display()
            else:
                print("Sorry ! Wrong choice.")

    elif bnk==3:
        iobj=Icici()
        for i in range(1, 7):
            print(" 1. Add Customer \n 2. Calculate interest. \n 3. Withdraw Amount. \n 4. Deposite Amount")
            i = int(input("Select your transaction type: "))

            if i == 1:

                iobj.addinfo()
            elif i == 2:
                iobj.display()
                iobj.interest()
            elif i == 3:
                iobj.display()
                iobj.withdraw()
                iobj.display()
            elif i == 4:
                iobj.display()
                iobj.deposit()
                iobj.display()
            else:
                print("Sorry ! Wrong choice.")
    elif bnk==4:
        exit()
    else:
        print("wrong choice")