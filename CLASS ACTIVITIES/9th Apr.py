'''name= "HELLO"
print(name.isalnum()) # True because it contains only letters and numbers
print(name.isalpha()) # True because it contains only letters
print(name.isdigit()) # False because it contains letters
print(name.islower()) # False because it contains uppercase letters
print(name.isupper()) # True because it contains uppercase letters
print(name.isnumeric()) # False because it contains letters
print(name.isprintable()) # True because it contains printable characters
print(name.isascii()) # True because it contains only ASCII characters
print(name.isdecimal()) # False because it contains letters
print(name.isspace()) # False because it contains letters

name = " he llo n "
lowercase = name.lower() # Convert to lowercase
strip_string = name.strip() # Remove leading and trailing whitespace
endswith_n = name.endswith("n") # Check if it ends with "n"
startswith_n = name.startswith("n") # Check if it starts with "n"
rstring = name.rstrip() # Remove trailing whitespace
replace = name.replace(" ", "") # Remove all spaces
print(lowercase) # Output: " hello n"
print(strip_string) # Output: "he llo n"
print(endswith_n) # Output: True
print(startswith_n) # Output: False
print(rstring) # Output: " he llo n"
print(replace) # Output: "hellon"'''

# String formatting
#write a program that asks user for 3 inputs: firstname, lastname, rollnumber in lowecases. Create a unique code for the user using the following. The first four characters of the first name in upper cases. The first 3 characters of the last name in lowercases. The last three digits of the roll number. Ensure that the inputs are not longer than 10.
while True:
    firstname = input("Enter your first name: ")
    lastname = input("Enter your last name: ")
    rollnumber = input("Enter your roll number: ")

    if (len(firstname) <= 10 and len(lastname) <= 10 and len(rollnumber) <= 10) and (rollnumber.isdigit() and firstname.isalpha() and lastname.isalpha()):
        break
    else: 
        if  len(firstname) > 10:
            print("First name cannot contain more than 10 characters")
        if  len(lastname) > 10:
            print("Last name cannot contain more than 10 characters")
        if   len(rollnumber) > 10:
            print("Rollnumber cannot contain more than 10 characters")
        if  not rollnumber.isdigit():
            print("Rollnumber cannot contain letters")
        if  not firstname.isalpha():
            print ("First name cannot contain numbers")
        if  not lastname.isalpha():
            print("Last name cannot contain digits")
        continue

unique_code = firstname[:4].upper() + lastname[:3].lower() + rollnumber[-3:]
print("Your unique code is: ", unique_code)