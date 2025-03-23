pin = "0"
balance = 0
attempts = 3

while pin != "1234":
    pin = input("Enter Pin: ")
    
    if pin == "1234":
        print("PIN correct\n")
        done = "N"
        
        while done == "N":
            print("Menu:\nC. Check Balance\nD. Deposit Money\nW. Withdraw Money\nE. Exit Program\n")
            choice = input().upper()

            if choice == "C":
                print(f"Your balance {balance}")
            
            elif choice == "D":
                deposit = int(input("Enter amount to deposit: "))
                balance += deposit
                print(f"Deposit successful. New balance: {balance}")

            elif choice == "W":
                withdraw_limit = 100
                while True:
                    if balance == 0:
                        print("Your account is empty")
                        break

                    withdraw = int(input("Enter amount to withdraw: "))

                    if balance < withdraw:
                        print(f"Insufficient Funds. Your balance is: {balance}")
                    elif withdraw > withdraw_limit:
                            print(f"Exceeded withdrawal limit. Your balance is: {balance}")
                    else:
                        balance -= withdraw
                        print(f"Withdrawal successful. Your balance is: {balance}")
                        break

            elif choice == "E":
                print("Exiting Program. Goodbye!")
                break

            else:
                print("Incorrect Input. Try Again")
                continue

            done = input("Are you done Banking! (Y/N)").upper()
    else:
        print("Error. Incorrect Pin")
        attempts -= 1
        print(f"You have {attempts} more attempts left.")
    
    if attempts <= 0:
        print("Too many incorrect attempts. Your account is locked.")
        break
