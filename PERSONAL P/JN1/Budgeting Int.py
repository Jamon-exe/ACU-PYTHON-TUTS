#Campus Budgetting App
#This program will allow the user to input their income and expenses and will calculate the amount of money they have left over after expenses.
#The program will also display a message if the user has overspent.

verification = "NO"
while verification not in ["YES", "Y"]:

    #definining variables for the user's income and expenses
    user_income = int(input("Enter your income: "))
    time_period = input("Enter the time period for your income (in days): ")
    user_savings = int(input("Enter the amount of money you want to save: "))
    # ADD A PERCENTAGE FEATURE.
    user_expenses = int(input("Enter your expenses: "))
    
    miscellaneous = int(input("Do you have any other expenses you need to set aside e.g (Project Money/ Business/ Family Obligations): "))
    if miscellaneous in [ "YES", "Y"]:
        miscellaneous = int(input("Enter the amount you want to set aside: "))
    else:
        miscellaneous = 0
    #EXPENSES VERIFICATION SECTION--------------------------------

    user_expenses = user_expenses + miscellaneous
    
    #calculating if user expenses are greater than user income
    if user_expenses > user_income:
        print("You dont heve enough money to cover your expenses")
        continue
    else:
        print ("You have enough money to cover your expenses.")
    #END OF EXPENSES VERIFICATION SECTION----------------------------


    print("Thank You")
    input ("Press Enter to continue")

    #VERIFICATION SECTION-------------------------------------------
    print(f"Your income is {user_income}\n You have {time_period} days to manage your income\n You want to save {user_savings}\n Your total expenses are {user_expenses} (including {miscellaneous})")
    verification = input("Are you sure the information above is accurate? (Yes/No): ").upper()
    #checking if the user has entered the correct information
    
    