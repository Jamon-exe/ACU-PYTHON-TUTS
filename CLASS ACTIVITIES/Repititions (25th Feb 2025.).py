# user_seconds=0
# while user_seconds != 419:
#     user_seconds=int(input("Enter the number of seconds: "))
#     #Minutes
#     if user_seconds>=60 and user_seconds<3600:
#         minutes=user_seconds//60
#         seconds=user_seconds%60
#         print(f"{user_seconds} seconds is equal to {minutes} minutes and {seconds} seconds.")
#     #Seconds
#     elif user_seconds<60:
#         seconds=user_seconds
#         print(f"{user_seconds} seconds is equal to {seconds} seconds.")
        
#     #Hours
#     elif user_seconds>=3600 and user_seconds<86400:
#         hours=user_seconds//3600
#         minutes=(user_seconds%3600)//60
#         seconds=(user_seconds%3600)%60
#         print(f"{user_seconds} seconds is equal to {hours} hours, {minutes} minutes and {seconds} seconds.")
#     #Days
#     elif user_seconds>=86400:
#         days=user_seconds//86400
#         hours=(user_seconds%86400)//3600
#         minutes=((user_seconds%86400)%3600)//60
#         seconds=((user_seconds%86400)%3600)%60
#         print(f"{user_seconds} seconds is equal to {days} days, {hours} hours, {minutes} minutes and {seconds} seconds.")
#         input("Press Enter to continue:")
#         user_seconds=int(input("Enter the number of seconds: "))
        
#Dor the while look, you need an initial value, and the while loop will keep running until the condition is no longer met.

#This code will print numbers from 1 to 5
# a = 1
# while a < 6:
#     print(a)
#     a = a + 1

#Print out even numbers between 1 and 10; including 1 and 10
# a = 1
# while a <= 10:
#     if a % 2 == 0 or a == 1:
#         print(a) 
#     a=a+1
    #NOTE: new state to test the condition should always come last

#All Mutiples of 5 between 1 and hundred
# a = 1
# while a <= 100:
#         print(a) 
#     a = a +1

condition = "YES"
while condition in ["Y","YES"]:
    first_num = int(input(f"Enter your first number: "))
    second_num = int(input(f"Enter your second number: "))
    print (f"Your sum is {first_num+second_num}")
    condition = input(f"Do you want to enter two values (Yes/No):").upper()

