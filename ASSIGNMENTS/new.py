import datetime

# Initialize variables
pin="0"  # Current PIN for comparison
new_pin="1234"  # Default PIN
balance= 0  # Initial account balance
attempts=3  # Number of PIN entry attempts allowed
transactions= []  # List to store transaction history
now = datetime.datetime.now()  # Get current date and time

# Display welcome message with current date and time
print (f"Welcome to the Bank of Python. Today's date is {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Main PIN verification loop
while pin != new_pin:
    pin=input("Enter Pin: ")
    
    if pin == new_pin:
        print ("PIN correct\n")

        # Main banking loop
        condition = "N"
        while condition == "N":
            choice= 0
            # Menu selection loop
            while choice not in ["C", "D", "W", "E", "Z", "T"]:
                # Display menu options
                choice = input("Menu:\nC. Check Balance\nD. Deposit Money\nW. Withdraw Money\nE. Exit Progam\nZ. Change PIN\nT. Check Transaction History \n\n").upper()

                # Check Balance
                if choice == "C":
                    print(f"Your balance {balance}")
                
                # Deposit Money
                elif choice == "D":
                    deposit = int(input("Enter amount to deposit: "))
                    if deposit < 0:
                        print("Invalid amount")
                    else:
                        balance += deposit
                        current_time = datetime.datetime.now()
                        print(f"Deposit successful. New balance: {balance}")
                        # Record transaction
                        d = f"Deposit of {deposit} at {current_time.strftime('%Y-%m-%d %H:%M:%S')}"
                        transactions.append(d)

                # Withdraw Money
                elif choice == "W":
                    withdraw_limit = 100  # Set withdrawal limit
                    while True:
                        # Check if account is empty
                        if balance == 0:
                            print(f"Your account is empty")
                            break

                        withdraw = int(input("Enter amount to withdraw: "))

                        # Validate withdrawal amount
                        if balance < withdraw:
                            print(f"Insufficient Funds. Your balance is: {balance}")
                        elif withdraw < 0:
                            print("Invalid amount")
                        elif withdraw > withdraw_limit:
                            print(f"Exceeded withdrawal limit. Your balance is: {balance}")
                        else:
                            # Process withdrawal
                            balance -= withdraw
                            current_time = datetime.datetime.now()
                            print(f"Withdrawal successful. Your balance is: {balance}")
                            # Record transaction
                            w = f"Withdrawal of {withdraw} at {current_time.strftime('%Y-%m-%d %H:%M:%S')}"
                            transactions.append(w)
                            break
                            
                # Change PIN
                elif choice == "Z":
                    # Verify current PIN
                    while True:
                        prev_pin=input('Enter current pin: ')
                        if prev_pin == pin:
                            print("Pin correct")
                            break
                        else:
                            print("Incorrect pin")
                    # Set new PIN with validation
                    new_pin = input("Enter new pin: ")
                    if new_pin == pin:
                        print("New pin cannot be the same as the old pin")
                    elif len(new_pin) != 4:
                        print("Pin must be 4 digits")
                    elif new_pin != pin and len(new_pin) == 4:
                        pin = new_pin
                        print("Pin changed successfully")
                
                # Exit Program
                elif choice == "E":
                    print("Exiting Program. Goodbye!")
                    break

                # View Transaction History
                elif choice == "T":
                    # Display transactions in reverse chronological order
                    for a in reversed(transactions):
                        print(a)
                    if len(transactions) == 0:
                        print("No transactions yet\n")
                    
                else:
                    print("Incorrect Input.Try Again")
            
            # Ask if user wants to continue banking
            condition= input("Are you done Banking! (Y/N)").upper()
    else:
        # Handle incorrect PIN
        print ("Error. Incorrect Pin")
        attempts -= 1
        print (f"You have {attempts} more attempts left.")
    
    # Lock account after too many failed attempts
    if attempts <= 0:
        print ("Too many incorrect attempts. Your account is locked.")
        break
# In the deposit section (replace the current transactions.append line):


# In the withdrawal section (replace the current transactions.append line):
transactions.append({
    'type': 'Withdrawal',
    'amount': withdraw,
    'balance': balance,
    'time': current_time.strftime('%Y-%m-%d %H:%M:%S')
})
