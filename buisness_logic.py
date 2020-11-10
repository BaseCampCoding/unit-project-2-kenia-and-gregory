class Account:
    def __init__(self): 
        self.savings = 0
        self.balance = float(0)
        print('Your Account is Created.')

    def deposit(self):
        amount = input('Enter the amount to deposit: ')
        while True:
            try:
                self.balance += float(amount)
                print(f"Your New Balance = {self.balance:.2f} ")
                break
            except ValueError:
                print ("Please input a number")
                amount = input('Enter the amount to deposit: ')


    def withdraw(self):
        num =input('Enter the amount to withdraw: ')
        while True:
            try:
                if(float(num) > self.balance):
                    print('Insufficient Balance!')
                else:
                    self.balance -= float(num)
                    break
            except ValueError:
                print ("Please input a number")
                amount=input('Enter the amount to withdraw: ')

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
            print(f"Your New Savings Balance= {self.savings}")

account = Account()
