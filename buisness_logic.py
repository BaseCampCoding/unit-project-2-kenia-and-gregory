class Account:
    def __init__(self): 
        self.savings= 0
        self.balance = 0
        print('Your Account is Created.')

    def deposit(self):
        amount=input('Enter the amount to deposit: ')
        while True:
            if amount.isdigit():
                self.balance+=int(amount)
                print('Your New Balance = %d' %self.balance)
                break
            else:
                print ("please Input a Number")
                amount=input('Enter the amount to deposit: ')

    def withdraw(self):
        amount=(input('Enter the amount to withdraw: '))
        while True:
            if amount.isdigit():
                if(int(amount) >self.balance):
                    print('Insufficient Balance!')
                    break
                else:
                    self.balance-= int(amount)
            else:
                print ("please Input a Number")
                amount=(input('Enter the amount to withdraw: '))

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
