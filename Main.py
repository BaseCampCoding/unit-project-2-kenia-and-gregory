import bank_database as db
import buisness_logic as bl
import sqlite3

print('"""""""""""""""""""""""""""""')
print("WELCOME TO BANK OF BASE CAMP!")
print('"""""""""""""""""""""""""""""')
while True:
    acc_option=input(
        """ Do you have an account?
    -Yes
    -No
    -EXIT
    >""")
    if acc_option=="Yes".lower():
        name=()
        db.cur.execute("""SELECT )
    elif acc_option=="No".lower():
        name=input("Enter your FIRST name: ")
        amount=input("How much do you want to open the account with? ")
        savings= 0
        db.cur.execute("INSERT INTO Account Values(?, ?, ?)", (name, amount, savings))
        db.con.commit()
        break

while True:
    answer = input(
        """What do you want to do ?
    -View Checkings Account
    -View Savings Account
    -Deposit
    -Withdraw
    -Transfer
    -EXIT
    > """)
    if answer == 'Check Account'.lower():
       bl.account.enquiry()
    
    elif answer == 'Check Savings'.lower():
        bl.account.Savings_enquiry()

    elif answer == 'Deposit'.lower():
        bl.account.deposit()

    elif answer == 'Withdraw'.lower():
        bl.account.withdraw()

    elif answer == "Check Savings".lower():
        bl.account.Savings_enquiry()
        
    elif answer == 'Transfer'.lower():
        bl.account.add_to_savings()

    elif answer == "Exit".lower():
        print("Goodbye")
        break
