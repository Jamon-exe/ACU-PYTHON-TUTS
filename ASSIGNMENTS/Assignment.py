#PRINT
name = input("Hey there, what is your name?\n\t")
num1 = int(input(f"Hello {name}!\nPlease enter your first number:\n\t"))
num2 = int(input("Please enter your second number:\n\t"))

#VARIABLES
add = num1 + num2
diff = num1 - num2
prod = num1 * num2
quot = num1 / num2

print(f"Thank you {name}!")
print(f"Sum: {add}, Difference: {diff}, Product: {prod}, Quotient: {quot}")

#

#IF STATEMENTS
if num1 > num2:
    print(f"🎉 Congratulations {name}! Your first number was bigger!")
    print(f"The difference is {num1 - num2}!")
elif num1 < num2:
    print(f"📉 Oh no {name}! Your second number was bigger!")
    print(f"You missed by {num2 - num1}!")
else:
    print(f"🎯 Wow {name}! The numbers are exactly equal!")
    print("What are the chances of that?")
