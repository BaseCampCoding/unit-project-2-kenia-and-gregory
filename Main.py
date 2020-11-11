import bank_database as db
import buisness_logic as bl
while True:
    print('"""""""""""""""""""""""""""""')
    print("WELCOME TO BANK OF BASE CAMP!")
    print('"""""""""""""""""""""""""""""')
    bl.account.if_acc()
    while True:
        answer = input(
            """What do you want to do ?
        -[1] Checkings Account
        -[2] Savings Account
        -[3] Deposit
        -[4] Withdraw
        -[5] Transfer
        -[6] Set up a Budget
        -[7] View Budget 
        -[8] View All
        -[9] EXIT
        > """)
        if answer == '1':
            bl.account.enquiry()
        
        elif answer == '2':
            bl.account.Savings_enquiry()

        elif answer == '3':
            bl.account.deposit()

        elif answer == '4':
            bl.account.withdraw()

        elif answer == '5':
            bl.account.add_to_savings()

        elif answer == "6":
            bl.account.budgets()
        
        elif answer == "7":
            bl.account.view_budget()

        elif answer == "8":
            bl.account.view_all()


        elif answer == "9":
            print("Goodbye")
            break
