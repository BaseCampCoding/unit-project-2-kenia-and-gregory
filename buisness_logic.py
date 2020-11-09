class Account:
    def __init__(self): 
        self.savings = 0
        self.balance = 0
        print('Your Account is Created.')

    def deposit(self):
        amount = input('Enter the amount to deposit: ')
        while True:
            amount = round(float(amount), 2)
            if amount.isdigit():
                self.balance+=float(amount)
                print(f"Your New Balance = {self.balance} ")
                break
            else:
                print ("please Input a Number")
                amount=input('Enter the amount to deposit: ')

    def withdraw(self):
        amount=int(input('Enter the amount to withdraw: '))
        if(amount>self.balance):
            print('Insufficient Balance!')
        else:
            amount = round(amount, 2)
            self.balance-=amount

    def enquiry(self):
        print(f"Your Balance = {self.balance}")

    def Savings_enquiry(self):
        print(f"Your Balance = {self.savings} ")

    def add_to_savings(self):
        number=int(input("How much do you want to transfer to Savings Account? "))
        if(number>self.balance):
            print('Insufficient Balance!')
        else:
            amount = round(amount, 2)
            self.balance-=number
            self.savings +=number
            print(f"Your New Savings Balance= {self.savings}")

account = Account()
