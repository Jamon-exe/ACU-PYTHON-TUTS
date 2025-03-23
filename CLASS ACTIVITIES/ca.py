input ()
print ("Temperature Analyser")
user_temp= int(input("Enter the temperature: "))
user_wellness= input("Do you feel well? (Yes or No)")
if user_wellness == "Yes" or user_wellness == "No" or user_wellness == "yes" or user_wellness == "no" or user_wellness == "Y" or user_wellness == "N" :
    if user_temp >= 37:
        print("You might have a fever")
    elif user_temp < 37:
        print("You are okay")
else:
        print("Invalid input")


input()
print("Voting Eligibility Tester")
user_age= int(input("Enter your age: "))
if user_age >= 18:
    print("You are eligible to vote")
else:
     print("You are not eligible to vote yet")

input()
print ("Voter Eligibilty 2")
user_age= int(input("What is your age: "))
if user_age>= 18:
    voter_id_status= input("Do you have a voter ID (Yes/No): ")
    if voter_id_status in ["Yes", "No", "N", "Y", "n", "y", "yes", "no"]:
        if user_age >= 18 and voter_id_status in ["Yes", "Y", "y"]:
            print("You can vote!")
        elif user_age >= 18 and voter_id_status in ["No", "no", "n", "N"]:
            print ("You need a voter ID to vote")
        else:
            print("You cant vote")
    else:
        print("Invalid Input")
else:
    print("You can't vote")

input()
print ("Status")
user_age=int(input("How old are you? "))
day_cat=input("Is it weekend or weekday? (answer with Weekend / Weekday ) ").lower()
if day_cat == "weekend" or day_cat == "weekday":
    if user_age < 18 and day_cat == "weekday":
        print("You should be in school!")
    elif user_age < 18 and day_cat == "weekend":
        print("Enjoy your free time!")
    elif user_age >= 18 and day_cat == "weekday":
        print("You should be at work!")
    elif user_age >= 18 and day_cat == "weekend":
        print("Enjoy your Weekend!")
else:
    print("Invalid Input")
