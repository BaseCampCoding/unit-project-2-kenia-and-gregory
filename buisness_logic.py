import bank_database as db
import json 
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
        while True:
            acc_option=input(
            """ Do you have an account?
        -Yes
        -No
        -Quit
        > """)
            if acc_option=="Yes".lower():
                name= input("Enter your USERNAME Name: ")
                db.cur.execute("""SELECT Name FROM Account""")
                db.con.commit()
                self.name = name
                acc_names= db.cur.fetchall()
                names=[]
                for i in acc_names:
                    names.append(i[0])
                # print(names)
                if name in names:
                    entered_pin=input("Enter your pin: ")
                    db.cur.execute("""SELECT Pin FROM Account""")
                    db.con.commit()
                    pines= db.cur.fetchall()
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
                name=input("Enter a USERNAME name: ")
                self.name = name
                amount=0 
                savings= 0
                budget=0 
                pin=str(input("Create a 4 digit pin: "))
                db.cur.execute("INSERT INTO Account Values(?, ?, ?, ?, ? )", (name, amount, savings, pin, budget))
                db.con.commit()
                print('Your Account is Created.')
                break
            elif acc_option == "Quit".lower():
                "GOODBYE"
                quit()
        # print('"""""""""""""""""""""""""""""')
    def deposit(self):
        deposits = input('Enter the amount to deposit: ')
        while True:
            try:
                self.balance += float(deposits)
                db.cur.execute("SELECT * FROM Account")
                db.cur.execute("UPDATE Account SET Checkings = ? WHERE Name = ?", (self.balance, self.name))
                print(f"Your New Balance = {self.balance :.2f} ")
                db.con.commit()
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
            db.cur.execute("SELECT * FROM Account")
            db.cur.execute("UPDATE Account SET Budget = ? WHERE Name = ?", (self.budget, self.name))
            db.con.commit()

    def view_budget(self):
        db.cur.execute("SELECT * FROM Account")
        db.cur.execute("""SELECT Budget FROM Account WHERE Name = ?""", (self.name))
        db.con.commit()
        print(f"The limit on your account is {db.cur.fetchall:.2f} ")

    def withdraw(self):
        num =input('Enter the amount to withdraw: ')
        reason=input("Reason for withdraw: ")
        entry={"Name": self.name, "Amount": num, "Reason": reason}
        withdraws_j.append(entry)
        while True:
            if(float(num) > self.balance):
                print('Insufficient Balance!')
                print(f"Your Balance = {self.balance :.2f} ")
                num = input('Enter the amount to withdraw: ')
                break
            elif self.budget > self.balance:
                answer_budget=input(
                    """You are going over your budget!
                    Do you still want to make the transaction?""")
                if answer_budget == "No".lower():
                    break
                        
            else:
                self.balance -= float(num)
                db.cur.execute("SELECT * FROM Account")
                db.cur.execute("UPDATE Account SET Checkings = ? WHERE Name = ?", (self.balance, self.name))
                db.con.commit()
                with open("withdraw_activity.json", "w") as file:
                    json.dump(withdraws_j, file)
                print(f"Your Balance = {self.balance:.2f} ")
                break
                        

    def enquiry(self):
        print(f"Your Balance = {self.balance}")
 
    def Savings_enquiry(self):
        print(f"Your Balance = {self.savings} ")

    def add_to_savings(self):
        number=int(input("How much do you want to transfer to Savings Account? "))
        if(number>self.balance):
            print('Insufficient Balance!')
        else:
            self.balance -= number
            self.savings += number
            db.cur.execute("SELECT * FROM Account")
            db.cur.execute("UPDATE Account SET Checkings = ? WHERE Name = ?", (self.balance, self.name))
            db.con.commit()
            db.cur.execute("UPDATE Account SET Savings = ? WHERE Name = ?", (self.savings, self.name))
            print(f"Your New Savings Balance= {self.savings :.2f}")

account = Account()
