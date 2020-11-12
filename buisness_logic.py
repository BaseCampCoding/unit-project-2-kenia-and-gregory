import bank_database as db
import json 
import sqlite3 
con= sqlite3.connect("bank.db")
cur= con.cursor()
with open("withdraw_activity.json") as file:
    reader = json.load(file)
    withdraws_j = list(reader)


class Account:
    def __init__(self): 
        self.name= str(None)
        self.savings = 0
        self.balance = float(0)
        self.budget= 0
        
    def if_acc(self):
        # db.cur.execute("SELECT Checkings FROM Account")
        # Money1 = db.cur.fetchall()
        # Money= []
        # for i in Money1:
        #     Money.append(i[0])
        # self.balance += float(Money[0])

        # db.cur.execute("SELECT Savings FROM Account")
        # Savings1 = db.cur.fetchall()
        # Savings = []
        # for i in Savings1:
        #     Savings.append(i[0])
        # self.savings += float(Savings[0])

        # db.cur.execute("SELECT Checkings FROM Account")
        # Budget1 = db.cur.fetchall()
        # Budget = []
        # for i in Budget1:
        #     Budget.append(i[0])
        # self.budget += float(Budget[0])

        while True:
            acc_option=input(
            """ Do you have an account?
        -Yes
        -No
        -Quit
        > """)
            if acc_option=="Yes".lower():
                name= input("Enter your USERNAME Name: ")
                cur.execute("""SELECT Name FROM Account""")
                con.commit()
                self.name = name
                acc_names= cur.fetchall()
                # print(names)
                if name == self.name:
                    entered_pin=input("Enter your pin: ")
                    cur.execute("""SELECT Pin FROM Account""")
                    con.commit()
                    pines= entered_pin
                    # print(pins)
                    if entered_pin == pines:
                        break
                    else:
                        print("Incorrrect Pin")

                else:
                    print("Incorrect Account Name! Please make account")
                    continue
                
            elif acc_option=="No".lower():
                name=input("Enter a USERNAME name: ")
                self.name = name
                amount=0 
                savings= 0
                budget=0 
                pin=str(input("Create a 4 digit pin: "))
                pins=[]
                for i in pines: 
                    pins.append(i[0])
                cur.execute("INSERT INTO Account Values(?, ?, ?, ?, ? )", (name, amount, savings, pin, budget))
                con.commit()
                print('Your Account is Created.')
                names=[]
                for i in acc_names:
                    names.append(i[0])
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
        if if_budget == "Yes".lower():
            budget_amount=input("What is your limit? ")   
            self.budget += float(budget_amount)
            print("Budget successfully set!")
            cur.execute("SELECT * FROM Account")
            cur.execute("UPDATE Account SET Budget = ? WHERE Name = ?", (self.budget, self.name))
            con.commit()

    def view_budget(self):
        print(f"Your Budget is $ {self.budget}")
        # print(f"The limit on your account is {things :.2f} ")

    def withdraw(self):
        num =input('Enter the amount to withdraw: $')
        reason=input("Reason for withdraw: ")
        entry={"Name": self.name, "Amount": num, "Reason": reason}
        withdraws_j.append(entry)
        while True:
            if(float(num) > self.balance):
                print('Insufficient Balance!')
                print(f"Your Balance = ${self.balance :.2f} ")
                num = input('Enter the amount to withdraw: ')
                break
            if self.budget > self.balance:
                answer_budget=input(
                    """You are going over your budget!
                    Do you still want to make the transaction?""")
                if answer_budget == "No".lower():
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

    def enquiry(self):
        name = self.name
        cur.execute('SELECT Checkings FROM Account WHERE Name = ?', (name,))
        self.balance = cur.fetchall()
        print(f"Your Balance = ${self.balance}")
 
    def Savings_enquiry(self):
        print(f"Your Balance = ${self.savings} ")

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
            print(f"Your New Savings Balance= ${self.savings :.2f}")

    def view_all(self):
        ALL_Data = (f"{self.name}, ${self.balance}, ${self.savings}, ${self.budget}")
        print(ALL_Data)

print(cur.fetchall())
account = Account()
