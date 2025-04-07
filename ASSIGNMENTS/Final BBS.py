import datetime

pin="0"
new_pin="1234"
balance= 0
attempts=3
transactions= []
now = datetime.datetime.now()
break_out = False
print (f"Welcome to the Bank of Python. Today's date is {now.strftime('%Y-%m-%d %H:%M:%S')}")

while pin != new_pin:
    pin=input("Enter Pin: ")
    
    if pin == new_pin:
        print ("PIN correct\n")

        choice= 0
        while choice not in ["C", "D", "W", "E", "Z", "T"]:
            while True:
                choice = input("Menu:\nC. Check Balance\nD. Deposit Money\nW. Withdraw Money\nE. Exit Progam\nZ. Change PIN\nT. Check Transaction History \n\n").upper()

                if choice == "C":
                    print(f"Your balance GH₵{balance}")
                

                elif choice == "D":
                    while True:
                        deposit = input("Enter amount to deposit: ")
                        if deposit.isalpha():
                            print("Invalid amount")
                        elif deposit.isdigit():
                            deposit = int(deposit)
                            break
                        else:
                            print("Invalid amount")

                    if deposit < 0:
                        print("Invalid amount")
                    else:
                        balance += deposit
                        print(f"Deposit successful. New balance: {balance}")
                        d= f"Deposit of GH₵{deposit} at {datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')}"
                        transactions.append(d)


                elif choice == "W":
                    withdraw_limit = 1000  # Set withdrawal limit
                    #add a place to change withdrawal 
                    while True:
                        if balance == 0:
                            print(f"Your account is empty")
                            break
                        while True:
                            withdraw = input("Enter amount to withdraw: ")
                            if withdraw.isalpha():
                                print("Invalid amount")
                            elif withdraw.isdigit():
                                withdraw = int(withdraw)
                                break
                            else:
                                print("Invalid amount")

                        if balance < withdraw:
                            print(f"Insufficient Funds. Your balance is: {balance}")
                        elif withdraw < 0:
                            print("Invalid amount")
                        elif withdraw > withdraw_limit:
                            print(f"Exceeded withdrawal limit. Your withdrawal limit is {withdraw_limit}. Your balance is: {balance}")
                        elif balance > withdraw:
                            balance -= withdraw
                            print(f"Withdrawal successful. Your balance is: {balance}")
                            w = f"Withdrawal of GH₵{withdraw} at {datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')}"
                            transactions.append(w)
                            break
                        
                elif choice == "Z":

                    while True:
                        prev_pin=input('Enter current pin: ')
                        if prev_pin == pin:
                            print("Pin correct")
                            break
                        else:
                            print("Incorrect pin")
                    new_pin = input("Enter new pin: ")
                    if new_pin == pin:
                        print("New pin cannot be the same as the old pin")
                    elif len(new_pin) != 4:
                        print("Pin must be 4 digits")
                    elif new_pin != pin and len(new_pin) == 4:
                        pin = new_pin
                        print("Pin changed successfully")
                
                
                elif choice == "E":
                    print("Exiting Program. Goodbye!")
                    break_out = True
                    break

                elif choice == "T":
                    if len(transactions) == 0:
                        print("No transactions yet\n")
                    elif len(transactions) <= 5:
                        for a in reversed(transactions):
                            print(a)
                    else:
                        print("Last 5 transactions:")
                        for a in reversed(transactions[-5:]):
                            print(a)

                elif break_out == True:
                    break
                else:
                    print("Incorrect Input.Try Again")

                input("\n\t\t\tPress Enter to continue...")
                
    else:
        print ("Error. Incorrect Pin")
        attempts -= 1
        print (f"You have {attempts} more attempts left.")
    
    if attempts <= 0:
        print ("Too many incorrect attempts. Your account is locked.")
        break