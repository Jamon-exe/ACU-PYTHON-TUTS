#PG 165 Q.16
# year=int(input("Enter a year: "))
# if (year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
#     print(f"In {year} February has 29 days.")
# else:
#     print(f"In {year} February has 28 days.")
# input("Press Enter to continue:")


#PG 165 Q.15 (Time Calculator)
user_seconds=int(input("Enter the number of seconds: "))
#Minutes
if user_seconds>=60 and user_seconds<3600:
    minutes=user_seconds//60
    seconds=user_seconds%60
    print(f"{user_seconds} seconds is equal to {minutes} minutes and {seconds} seconds.")
#Seconds
elif user_seconds<60:
    seconds=user_seconds
    print(f"{user_seconds} seconds is equal to {seconds} seconds.")
    
#Hours
elif user_seconds>=3600 and user_seconds<86400:
    hours=user_seconds//3600
    minutes=(user_seconds%3600)//60
    seconds=(user_seconds%3600)%60
    print(f"{user_seconds} seconds is equal to {hours} hours, {minutes} minutes and {seconds} seconds.")
#Days
elif user_seconds>=86400:
    days=user_seconds//86400
    hours=(user_seconds%86400)//3600
    minutes=((user_seconds%86400)%3600)//60
    seconds=((user_seconds%86400)%3600)%60
    print(f"{user_seconds} seconds is equal to {days} days, {hours} hours, {minutes} minutes and {seconds} seconds.")
input("Press Enter to continue:")