import bank_database as db
class Account:
    def __init__(self): 
        self.savings = 0
        self.balance = float(0)

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
