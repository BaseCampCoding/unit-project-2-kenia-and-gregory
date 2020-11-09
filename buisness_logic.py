class Account:
    def __init__(self):
        self.balance = 0  
        self.savings= 0
        print('Your Account is Created.')
    def deposit(self):
        amount=int(input('Enter the amount to deposit: '))
        self.balance += amount
        print('Your New Balance= %d' %self.balance)
    def withdraw(self):
        amount=int(input('Enter the amount to withdraw: '))
        if(amount>self.balance):
            print('Insufficient Balance!')
        else:
            self.balance-=amount
    def enquiry(self):
        print('Your Balance = %d' %self.balance)
    def add_to_savings(self):
        number=int(input("How much do you want to transfer to Savings Account?"))
        if(number>self.balance):
            print('Insufficient Balance!')
        else:
            self.balance-=number
            self.savings +=number
            print('Your New Savings Balance= %d' %self.savings)

account = Account()
