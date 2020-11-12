import colorama
from colorama import Fore, Style, Back 
colorama.init()
import bank_database as db
import json 
import sqlite3 
con= sqlite3.connect("bank.db")
cur= con.cursor()
with open("withdraw_activity.json") as file:
    reader = json.load(file)
    withdraws_j = list(reader)

with open("savings.json") as file:
    reader = json.load(file)
    savings_j = list(reader)



class Account:
    def __init__(self): 
        self.name= str(None)
        self.savings = 0
        self.balance = float(0)
        self.budget= 0
        
    def if_acc(self):
        while True:
            acc_option=input(Fore.LIGHTMAGENTA_EX+
            """ Do you have an account?
        -Yes
        -No
        -Quit
        > """ +Style.RESET_ALL)
            if acc_option=="Yes".lower():
                name= input("Enter your USERNAME: ")
                cur.execute("""SELECT Name FROM Account""")
                con.commit()
                self.name = name
                acc_names= cur.fetchall()
                names=[]
                for i in acc_names:
                    names.append(i[0])
                # print(names)
                if name in names:
                    entered_pin=input("Enter your pin: ")
                    cur.execute("""SELECT Pin FROM Account""")
                    con.commit()
                    pines= cur.fetchall()
                    pins=[]
                    for i in pines: 
                        pins.append(i[0])
                    # print(pins)
                    if entered_pin in pins:
                        break
                    else:
                        print("Incorrrect Pin")

                else:
                    print("Incorrect Account Name! Please make account")
                    continue
                
            elif acc_option=="No".lower():
                name=input("Enter a USERNAME: ")
                self.name = name
                amount=0 
                savings= 0
                budget=0 
                pin=str(input("Create a 4 digit pin: "))
                cur.execute("INSERT INTO Account Values(?, ?, ?, ?, ? )", (name, amount, savings, pin, budget))
                con.commit()
                print('Your Account is Created.')
                break
            elif acc_option == "Quit".lower():
                "GOODBYE"
                quit()

    def deposit(self):
        deposits = input('Enter the amount to deposit: $')
        while True:
            try:
                self.balance += float(deposits)
                cur.execute("SELECT * FROM Account")
                cur.execute("UPDATE Account SET Checkings = ? WHERE Name = ?", (self.balance, self.name))
                print(f"Your New Balance = ${self.balance :.2f} ")
                con.commit()
                break
            except ValueError:
                print ("Please input a number")
                deposits = input('Enter the amount to deposit: ')

    def budgets(self):
        if_budget= input("Do you want to set up a budget for your Checkings account? ")
        while True:
            if if_budget == "Yes".lower():
                budget_amount=input("What is your limit? ")   
                self.budget += float(budget_amount)
                print("Budget successfully set!")
                cur.execute("SELECT * FROM Account")
                cur.execute("UPDATE Account SET Budget = ? WHERE Name = ?", (self.budget, self.name))
                con.commit()
                break
            elif if_budget == "No".lower():
                break
            else: 
                print("Please insert a valid answer!")
                if_budget= input("Do you want to set up a budget for your Checkings account? ")


    def view_budget(self):
        print(f"Your Budget is $ {self.budget}")


    def withdraw(self):
        num =input('Enter the amount to withdraw: $')
        reason=input("Reason for withdraw: ")
        entry={"Name": self.name, "Amount": num, "Reason": reason}
        withdraws_j.append(entry)
        while True:
            if(float(num) > self.balance):
                print(Fore.RED +'Insufficient Balance!'+ Style.RESET_ALL)
                print(f"Your Balance = ${self.balance :.2f} ")
                num = input('Enter the amount to withdraw: ')
                self.balance -= float(num)
                break
            elif self.budget <= self.balance:
                print("You are going over your budget!")
                answer_budget=input("Do you still want to make the transaction? ")
                if answer_budget == "Yes".lower():
                    self.balance -= float(num)
                    cur.execute("SELECT * FROM Account")
                    cur.execute("UPDATE Account SET Checkings = ? WHERE Name = ?", (self.balance, self.name))
                    con.commit()
                    with open("withdraw_activity.json", "w", newline='') as file:
                        json.dump(withdraws_j, file)
                    print(f"Your Balance = ${self.balance:.2f} ")
                    break
                elif answer_budget == "No".lower():
                    self.balance += float(num)
                    break

            else:
                self.balance -= float(num)
                cur.execute("SELECT * FROM Account")
                cur.execute("UPDATE Account SET Checkings = ? WHERE Name = ?", (self.balance, self.name))
                con.commit()
                with open("withdraw_activity.json", "w", newline='') as file:
                    json.dump(withdraws_j, file)
                print(f"Your Balance = ${self.balance:.2f} ")
                break

    def view_withdraws(self):
        for key in withdraws_j:
            if key["Name"] == self.name:
                print(Fore.RED+ "AMOUNT $", key["Amount"]+"- Purpose for Withdrawal: " +key["Reason"]+Style.RESET_ALL)

    def enquiry(self):
        cur.execute('SELECT Checkings FROM Account WHERE Name = ?', (self.name,))
        print(f"Your Balance = ${cur.fetchall()}")
 
    def Savings_enquiry(self):
        cur.execute('SELECT Savings FROM Account WHERE Name = ?', (self.name,))
        print(f"Your Balance = ${cur.fetchall()} ")

    def add_to_savings(self):
        number=(input("How much do you want to transfer to Savings Account? "))
        if(float(number)>self.balance):
            print('Insufficient Balance!')
        else:
            self.balance -= float(number)
            self.savings += float(number)
            cur.execute("SELECT * FROM Account")
            cur.execute("UPDATE Account SET Checkings = ? WHERE Name = ?", (self.balance, self.name))
            con.commit()
            cur.execute("UPDATE Account SET Savings = ? WHERE Name = ?", (self.savings, self.name))
            con.commit()
            savings={"Name": self.name, "Amount": number}
            savings_j.append(savings)
            print(f"Your New Savings Balance= ${self.savings :.2f}")
            with open("savings.json", "w", newline='') as file:
                    json.dump(savings_j, file)

    def view_all(self):
        ALL_Data = (f"{self.name}, ${self.balance}, ${self.savings}, ${self.budget}")
        print(ALL_Data)

account = Account()
