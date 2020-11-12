import colorama
from colorama import Fore, Style, Back 
colorama.init()
import bank_database as db
import buisness_logic as bl
while True:
    print('"""""""""""""""""""""""""""""')
    print(Fore.BLUE +"WELCOME TO BANK OF BASE CAMP!"+ Style.RESET_ALL)
    print('"""""""""""""""""""""""""""""')
    bl.account.if_acc()

    while True:
        answer = input(Fore.CYAN+
            """What do you want to do ?
        -[1] Checkings Account
        -[2] Savings Account
        -[3] Deposit
        -[4] Withdraw
        -[5] View Withdraws
        -[6] Transfer
        -[7] Set up a Budget
        -[8] View Budget 
        -[9] View All
        -[10] EXIT
        >"""+ Style.RESET_ALL)

        if answer == '1':
            bl.account.enquiry()
        
        elif answer == '2':
            bl.account.Savings_enquiry()

        elif answer == '3':
            bl.account.deposit()

        elif answer == '4':
            bl.account.withdraw()
        
        elif answer == '5':
            bl.account.view_withdraws()

        elif answer == '6':
            bl.account.add_to_savings()

        elif answer == "7":
            bl.account.budgets()
        
        elif answer == "8":
            bl.account.view_budget()

        elif answer == "9":
            bl.account.view_all()

        elif answer == "10":
            print("Goodbye")
            break
