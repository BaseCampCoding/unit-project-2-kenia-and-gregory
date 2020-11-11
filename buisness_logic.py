import bank_database as db
class Account:
    def __init__(self): 
        self.name= None
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
                name=input("Enter your USERNAME Name: ")
                db.cur.execute("""SELECT Name FROM Account""")
                db.con.commit()
                acc_names= db.cur.fetchall()
                names=[]
                for i in acc_names:
                    names.append(i[0])
                print(names)
                if name in names:
                    entered_pin=input("Enter your pin: ")
                    db.cur.execute("""SELECT Pin FROM Account""")
                    db.con.commit()
                    pines= db.cur.fetchall()
                    pins=[]
                    for i in pines: 
                        pins.append(i[0])
                    print(pins)
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
                db.cur.execute("""SELECT Checkings FROM Account""")
                db.cur.execute('SELECT Name FROM Account')
                db.cur.execute("UPDATE Account set Checkings = ? WHERE Name = ? ", (self.balance, name))
                db.con.commit()
                print(f"Your New Balance = {self.balance:.2f} ")
                break
            except ValueError:
                print ("Please input a number")
                deposits = input('Enter the amount to deposit: ')

    def budgets(self):
        if_budget= input("Do you want to set up a budget for your Checkings account? ")
        if if_budget == "Yes".lower():
            budget_amount=input("What is your limit? ")   
            self.budget= budget_amount

    def view_budget(self):
        print(f"The limit on your account is {self.budget:.2f} ")

    def withdraw(self):
        num =input('Enter the amount to withdraw: ')
        # reason=input("Reason for withdraw: ")
        while True:
            try:
                if(float(num) > self.balance):
                    print('Insufficient Balance!')
                    print(f"Your Balance = {self.balance:.2f} ")
                    num=input('Enter the amount to withdraw: ')
                else:
                    self.balance -= float(num)
                    print(f"Your Balance = {self.balance:.2f} ")
                    break
            
            except ValueError:
                print ("Please input a number")
                num=input('Enter the amount to withdraw: ')

    def enquiry(self):
        db.cur.execute("""SELECT * FROM Account""")
        for row in db.cur.fetchall():
            print(f"Your Balance = {row}")
 
    def Savings_enquiry(self):
        print(f"Your Balance = {self.savings} ")

    def add_to_savings(self):
        number=int(input("How much do you want to transfer to Savings Account? "))
        if(number>self.balance):
            print('Insufficient Balance!')
        else:
            self.balance -= number
            self.savings += number
            print(f"Your New Savings Balance= {self.savings :.2f}")
    
account = Account()
