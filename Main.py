import buisness_logic as bl

print('"""""""""""""""""""""""""""""')
print("WELCOME TO BANK OF BASE CAMP!")
print('"""""""""""""""""""""""""""""')

while True:
    answer = input(
        """What do you want to do?
    -View Checkings Account
    -View Savings Account
    -Deposit
    -Withdraw
    -Transfer
    -QUIT
    > """)
    if answer == 'Check Account'.lower():
       bl.account.enquiry()
    
    elif answer == 'Check Savings'.lower():
        bl.account.Savings_enquiry

    elif answer == 'Deposit'.lower():
        bl.account.deposit()

    elif answer == 'Withdraw'.lower():
        bl.account.withdraw()

    elif answer == "Check Savings".lower():
        bl.account.Savings_enquiry()
        
    elif answer == 'Transfer'.lower():
        bl.account.add_to_savings()

    elif answer == "Quit".lower():
        print("Goodbye")
        break
