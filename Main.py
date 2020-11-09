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
    if answer == 'Check Account':
       bl.account.enquiry()
    elif answer == "Deposit":
        bl.account.deposit()
    elif answer == "Withdraw":
        bl.account.withdraw()
    elif answer == "Quit":
        print("Goodbye")
        break
    