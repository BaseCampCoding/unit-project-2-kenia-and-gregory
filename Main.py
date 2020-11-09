import buisness_logic as bl
print('"""""""""""""""""""""""""""""')
print("WELCOME TO BANK OF BASE CAMP!")
print('"""""""""""""""""""""""""""""')
while True:
    answer=input(
    """What do you want to do?
    -View Checkings Account
    -View Savings Account
    -Deposit
    -Withdraw
    -QUIT
    > """)
    if answer == 'Check Account'.lower():
       bl.account.enquiry()

    elif answer == "Deposit".lower():
        bl.account.deposit()

    elif answer == "Withdraw".lower():
        bl.account.withdraw()
        
    elif answer == "Quit".lower():
        print("Goodbye")
        break
    