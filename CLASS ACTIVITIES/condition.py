# IF STATEMENTS
# number=int(input("Enter a number\n"))

# if number%2>0:
#     print (f"{number} is an odd number")
# else:
#     print (f"{number} is an even number")

#IF STATEMENTS USING LOGICAL OPERATORS
number=int(input("Enter a number\n"))
if number%2==0:
    print (f"it is even")
    if number >= 13 and number <= 19:
        print("You are a teenager")



"""# Assign initial values
a = 5
b = 7

# Demonstrate different comparison operators
print(f"less than {a<b}")              # Check if a is less than b
print(f"greater than {a>b}")           # Check if a is greater than b
print(f"greater than or equal to {a>=b}")  # Check if a is greater than or equal to b
print(f"less than or equal to {a<=b}")     # Check if a is less than or equal to b
print(f"not equal to {a!=b}")          # Check if a is not equal to b
print(f"equal to {a==b}")              # Check if a equals b

# Arithmetic operations with operator precedence
r = 5 + 4 % 3 / 1    # First 4%3=1, then 1/1=1, finally 5+1=6
print(r)

# Simple arithmetic expression
c = 4 * 2 - 2        # First 4*2=8, then 8-2=6
print(c)

print(type(c)==type(r)) # Check if the two variables are of the same type

# Compare results of r and c
print(r > c)

# Division example (shows floating point result)
print(3//2)"""