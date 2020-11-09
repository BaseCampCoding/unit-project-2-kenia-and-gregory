class Account:
    def __init__(self):
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

    # def balance(self):
    #     return(self.balance)
account = Account()
