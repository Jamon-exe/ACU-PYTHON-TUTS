pin="0"
balance= 0
attempts=3

while pin != "1234":
    pin=input("Enter Pin: ")
    
    if pin == "1234":
        print ("PIN correct\n")

        condition = "N"
        while condition == "N":
            choice= 0
            while choice not in ["C", "D", "W", "E", "Z"]:
                choice = input("Menu:\nC. Check Balance\nD. Deposit Money\nW. Withdraw Money\nE. Exit Progam\nZ. Change PIN\n\n").upper()

                if choice == "C":
                    print(f"Your balance {balance}")
                

                elif choice == "D":
                    deposit = int(input("Enter amount to deposit: "))
                    if deposit < 0:
                        print("Invalid amount")
                    else:
                        balance += deposit
                        print(f"Deposit successful. New balance: {balance}")


                elif choice == "W":
                    withdraw_limit = 100
                    while True:
                        if balance == 0:
                            print(f"Your account is empty")
                            break

                        withdraw = int(input("Enter amount to withdraw: "))

                        if balance < withdraw:
                            print(f"Insufficient Funds. Your balance is: {balance}")
                        elif withdraw < 0:
                            print("Invalid amount")
                        elif withdraw > withdraw_limit:
                            print(f"Exceeded withdrawal limit. Your balance is: {balance}")
                        elif balance > withdraw:
                            balance -= withdraw
                            print(f"Withdrawal successful. Your balance is: {balance}")
                            break
                        
                elif choice == "Z":
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
                    break

                else:
                    print("Incorrect Input.Try Again")
            
            condition= input("Are you done Banking! (Y/N)").upper()
    else:
        print ("Error. Incorrect Pin")
        attempts -= 1
        print (f"You have {attempts} more attempts left.")
    
    if attempts <= 0:
        print ("Too many incorrect attempts. Your account is locked.")
        break