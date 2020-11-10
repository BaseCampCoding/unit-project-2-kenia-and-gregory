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
        -Quit
        > """)
        if acc_option=="Yes".lower():
            name=input("Enter your First Name: ")
            db.cur.execute("""SELECT Name FROM Account""")
            db.con.commit()
            acc_names= db.cur.fetchall()
            names=[]
            for i in acc_names:
                names.append(i[0])
            print(names)
            if name in names:
                entered_pin=input("Enter your pin: ")
                db.cur.execute("""SELECT Pin FROM Account""")
                db.con.commit()
                pines= db.cur.fetchall()
                pins=[]
                for i in pines: 
                    pins.append(i[0])
                print(pins)
                if entered_pin in pins:
                    break
                else:
                    print("Incorrrect Pin")

            else:
                print("Incorrect Account Name! Please make account")
                continue
            
        elif acc_option=="No".lower():
            name=input("Enter your FIRST name: ")
            amount=0 
            savings= 0
            pin=input("Create a 4 digit pin: ")
            db.cur.execute("INSERT INTO Account Values(?, ?, ?, ? )", (name, amount, savings, pin))
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
