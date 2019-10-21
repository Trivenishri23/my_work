import openpyxl

class Bus:

    def __init__(self):
        pass

    def reserv(self):
        option=input("Do you want to book bus ticket? :")
        if option == 'n' or option=='N' or option== 'No' or option =='no:' :
            print("Thanks for visiting.")
        elif option == 'y' or option=='Y' or option== 'Yes' or option =='yes':
            print("Welcome")
            b=int(input("pealse selct seat: \n 1. AcSleeper. \n 2. Acseater. \n 3.NonAcsleeper. \n 4.NonAcseater. \n"))
            if b == 1:
                print("Available seats are: ")
                book = openpyxl.Workbook()  # creating Excel sheet
                acsl = book.active

                for l in "ABCDE":
                    for i in range(1,4):
                        l1=f'{l}{i}'
                        print(l1)
                        for k in range(1, (len(l1) + 1)):
                            for j in range(1, (len(l1) + 2)):
                                acsl(row=k, column=j).value = l1[k - 1][j - 1]




b=Bus()
b.reserv()