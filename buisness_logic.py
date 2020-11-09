class Account:
    def _init_(self):
        self.balance = 0  
        print('Your Account is Created.')
    def deposit(self):
        amount=int(input('Enter the amount to deposit: '))
        self.balance = amount
        print('Your New Balance= %d' %self.balance)
    def withdraw(self):
        amount=int(input('Enter the amount to withdraw: '))
        if(amount>self.balance):
            print('Insufficient Balance!')
        else:
            self.balance-=amount
    def enquiry(self):
        print('Your Balance = %d' %self.balance)

    # def balance(self):
    #     return(self.balance)
account = Account()
