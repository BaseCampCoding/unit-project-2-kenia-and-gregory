import bank_database as db
import buisness_logic as bl
import sqlite3
while True:
    print('"""""""""""""""""""""""""""""')
    print("WELCOME TO BANK OF BASE CAMP!")
    print('"""""""""""""""""""""""""""""')
    bl.account.if_acc()
    while True:
        answer = input(
            """What do you want to do ?
        -Checkings Account
        -Savings Account
        -Deposit
        -Withdraw
        -Transfer
        -Set up a Budget
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

        elif answer == "Budget".lower():
            bl.account.budgets()

        elif answer == "Exit".lower():
            print("Goodbye")
            break
