# userword = input("Enter a word: ").lower()
# holder=0
# for a in userword:
#     if a in "aeiou":
#         holder+=1
# print (f"The number of vowels in {userword} is {holder}.")

userdays = int(input("Enter the number of days: "))
counter = 0
for i in range(1,userdays+1):
    counter+=0.50
print (f"The total amount of money you will have after {userdays} days is ${counter}.")

# print (list(range(-8)))
print (userdays*0.50)