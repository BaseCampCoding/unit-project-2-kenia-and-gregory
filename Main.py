import bank_database as db
import buisness_logic as bl
import sqlite3
while True:
    print('"""""""""""""""""""""""""""""')
    print("WELCOME TO BANK OF BASE CAMP!")
    print('"""""""""""""""""""""""""""""')
    while True:
        acc_option=input(
            """ Do you have an account?
        -Yes
        -No
        -QUIT
        > """)
        if acc_option=="Yes".lower():
            name=input("Enter your First Name: ")
            db.cur.execute("""SELECT Name FROM Account""")
            db.con.commit()
            acc_names= db.cur.fetchall()
            names=[]
            for i in acc_names:
                names.append(db.cur.fetchall()[0:])
            if name in names:
                break
            else:
                continue
        elif acc_option=="No".lower():
            name=input("Enter your FIRST name: ")
            amount=0 
            savings= 0
            db.cur.execute("INSERT INTO Account Values(?, ?, ?)", (name, amount, savings))
            db.con.commit()
            break
        elif acc_option == "Quit".lower():
            "GOODBYE"
            quit()

    print('"""""""""""""""""""""""""""""')
    while True:
        answer = input(
            """What do you want to do ?
        -Checkings Account
        -Savings Account
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
